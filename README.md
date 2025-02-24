# TextSummarizer

A simple text summarization tool that helps you quickly generate summaries from articles and documents.

## Features (Planned)

- Support for multiple text formats (.txt, .md, .pdf)
- Configurable summary length
- Multiple summarization modes
- Command-line interface
- Batch file processing

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Summarize a file
python main.py example.txt

# Summarize from stdin
echo "Your text here..." | python main.py -

# Set custom summary length
python main.py example.txt --length 150

# Show help
python main.py --help
```

## Example

```bash
python main.py example.txt
```

## Requirements

- Python 3.8+
- OpenAI API key (set as OPENAI_API_KEY environment variable)

## Status

✅ Basic CLI functionality complete