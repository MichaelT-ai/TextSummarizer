"""
Text summarization module
"""
import os
from typing import Optional

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class TextSummarizer:
    def __init__(self, api_key: Optional[str] = None, use_ai: bool = True):
        self.use_ai = use_ai and OPENAI_AVAILABLE
        self.client = None
        
        if self.use_ai:
            self.api_key = api_key or os.getenv('OPENAI_API_KEY')
            if self.api_key:
                self.client = OpenAI(api_key=self.api_key)
            else:
                print("Warning: No OpenAI API key found. Using simple summarization.")
                self.use_ai = False
    
    def summarize_text(self, text: str, max_length: int = 100) -> str:
        """
        Summarize the given text
        """
        if not text.strip():
            return ""
        
        if self.use_ai and self.client:
            return self._ai_summarize(text, max_length)
        else:
            return self._simple_summarize(text, max_length)
    
    def _ai_summarize(self, text: str, max_length: int) -> str:
        """
        Use OpenAI API for summarization
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"Summarize the following text in approximately {max_length} characters. Be concise and capture the main points."},
                    {"role": "user", "content": text}
                ],
                max_tokens=150,
                temperature=0.5
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"AI summarization failed: {e}")
            return self._simple_summarize(text, max_length)
    
    def _simple_summarize(self, text: str, max_length: int) -> str:
        """
        Simple sentence-based summarization fallback
        """
        sentences = text.split('. ')
        summary_sentences = []
        current_length = 0
        
        for sentence in sentences:
            if current_length + len(sentence) <= max_length:
                summary_sentences.append(sentence)
                current_length += len(sentence)
            else:
                break
        
        result = '. '.join(summary_sentences)
        if not result.endswith('.'):
            result += '.'
        return result
    
    def summarize_file(self, file_path: str, max_length: int = 100) -> str:
        """
        Summarize text from file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.summarize_text(content, max_length)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading file: {e}")