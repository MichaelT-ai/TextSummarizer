"""
Batch processing functionality for TextSummarizer
"""
import os
import glob
from typing import List, Dict
from summarizer import TextSummarizer


class BatchProcessor:
    """Handle batch processing of multiple files"""
    
    def __init__(self, summarizer: TextSummarizer):
        self.summarizer = summarizer
    
    def process_directory(self, directory: str, pattern: str = "*.txt", 
                         max_length: int = 200) -> Dict[str, str]:
        """
        Process all files in a directory matching the pattern
        
        Args:
            directory: Directory path to process
            pattern: File pattern to match (default: *.txt)
            max_length: Maximum length for summaries
            
        Returns:
            Dictionary mapping file paths to summaries
        """
        if not os.path.isdir(directory):
            raise ValueError(f"Directory not found: {directory}")
        
        search_pattern = os.path.join(directory, pattern)
        files = glob.glob(search_pattern)
        
        if not files:
            print(f"No files found matching pattern: {search_pattern}")
            return {}
        
        results = {}
        for file_path in files:
            try:
                print(f"Processing: {file_path}")
                summary = self.summarizer.summarize_file(file_path, max_length)
                results[file_path] = summary
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                results[file_path] = f"Error: {e}"
        
        return results
    
    def process_file_list(self, file_paths: List[str], 
                         max_length: int = 200) -> Dict[str, str]:
        """
        Process a list of specific files
        
        Args:
            file_paths: List of file paths to process
            max_length: Maximum length for summaries
            
        Returns:
            Dictionary mapping file paths to summaries
        """
        results = {}
        for file_path in file_paths:
            try:
                print(f"Processing: {file_path}")
                summary = self.summarizer.summarize_file(file_path, max_length)
                results[file_path] = summary
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                results[file_path] = f"Error: {e}"
        
        return results
    
    def save_results(self, results: Dict[str, str], output_file: str) -> None:
        """
        Save batch processing results to a file
        
        Args:
            results: Dictionary of file paths to summaries
            output_file: Path to output file
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("# Batch Summarization Results\n\n")
                for file_path, summary in results.items():
                    f.write(f"## {os.path.basename(file_path)}\n")
                    f.write(f"**File:** {file_path}\n\n")
                    f.write(f"{summary}\n\n")
                    f.write("---\n\n")
            
            print(f"Results saved to: {output_file}")
        except Exception as e:
            print(f"Error saving results: {e}")