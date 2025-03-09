#!/usr/bin/env python3
"""
TextSummarizer - A simple text summarization tool
"""
import sys
import os
import argparse
from summarizer import TextSummarizer
from batch import BatchProcessor
from config import Config


def main():
    parser = argparse.ArgumentParser(description='TextSummarizer - Generate summaries from text')
    parser.add_argument('input', nargs='?', help='Input file path, directory, or "-" for stdin')
    parser.add_argument('-l', '--length', type=int, 
                       help='Maximum length of summary')
    parser.add_argument('-b', '--batch', action='store_true',
                       help='Batch process directory (input should be directory path)')
    parser.add_argument('-p', '--pattern', default='*.txt',
                       help='File pattern for batch processing (default: *.txt)')
    parser.add_argument('-o', '--output', 
                       help='Output file for batch results')
    parser.add_argument('--no-ai', action='store_true',
                       help='Disable AI summarization, use simple method')
    parser.add_argument('--version', action='version', version='TextSummarizer 0.2.0')
    
    args = parser.parse_args()
    
    # Load configuration
    config = Config()
    max_length = args.length or config.get('default_length', 200)
    use_ai = not args.no_ai and config.get('use_ai', True)
    
    try:
        summarizer = TextSummarizer(use_ai=use_ai)
        
        if args.batch:
            if not args.input or not os.path.isdir(args.input):
                print("Error: Batch mode requires a valid directory path", file=sys.stderr)
                sys.exit(1)
            
            processor = BatchProcessor(summarizer)
            results = processor.process_directory(args.input, args.pattern, max_length)
            
            if args.output:
                processor.save_results(results, args.output)
            else:
                print("\n" + "=" * 60)
                print("BATCH PROCESSING RESULTS")
                print("=" * 60)
                for file_path, summary in results.items():
                    print(f"\n📄 {os.path.basename(file_path)}")
                    print("-" * 40)
                    print(summary)
                    
        elif args.input == '-':
            # Read from stdin
            text = sys.stdin.read()
            summary = summarizer.summarize_text(text, max_length)
            print("Summary:")
            print("=" * 50)
            print(summary)
            
        elif args.input:
            # Read from file
            summary = summarizer.summarize_file(args.input, max_length)
            print("Summary:")
            print("=" * 50)
            print(summary)
        else:
            parser.print_help()
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()