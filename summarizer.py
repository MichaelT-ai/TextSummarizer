"""
Text summarization module
"""
import os
from typing import Optional


class TextSummarizer:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key is required")
    
    def summarize_text(self, text: str, max_length: int = 100) -> str:
        """
        Summarize the given text
        """
        if not text.strip():
            return ""
        
        # For now, return a simple truncated version
        # Will implement AI summarization later
        sentences = text.split('. ')
        summary_sentences = []
        current_length = 0
        
        for sentence in sentences:
            if current_length + len(sentence) <= max_length:
                summary_sentences.append(sentence)
                current_length += len(sentence)
            else:
                break
        
        return '. '.join(summary_sentences)
    
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