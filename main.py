#!/usr/bin/env python3
"""
TextSummarizer - A simple text summarization tool
"""
import sys
import argparse
from summarizer import TextSummarizer


def main():
    parser = argparse.ArgumentParser(description='TextSummarizer - Generate summaries from text')
    parser.add_argument('input', help='Input file path or "-" for stdin')
    parser.add_argument('-l', '--length', type=int, default=200, 
                       help='Maximum length of summary (default: 200)')
    parser.add_argument('--version', action='version', version='TextSummarizer 0.1.0')
    
    args = parser.parse_args()
    
    try:
        summarizer = TextSummarizer()
        
        if args.input == '-':
            # Read from stdin
            text = sys.stdin.read()
            summary = summarizer.summarize_text(text, args.length)
        else:
            # Read from file
            summary = summarizer.summarize_file(args.input, args.length)
        
        print("Summary:")
        print("=" * 50)
        print(summary)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()