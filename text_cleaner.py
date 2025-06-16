import re
import os
import string
import json
import logging
import argparse
import pandas as pd

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class TextCleaner:
    """
    Class to clean and sanitize text data.
    """

    def __init__(self, config_file="config.json"):
        """
        Initialize the TextCleaner with configuration options.
        Args:
            config_file (str): Path to the configuration file.
        """
        # Load the configuration settings
        self.config = self._load_config(config_file)
        self.keep_chars = self.config.get("keep_punctuation", None)
        self.preserve_words = self.config.get("preserve_words", [])
        self.char_map = self._create_char_map()

    def _load_config(self, config_file):
        """Load configuration from a JSON file."""
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Config file {config_file} not found.")
        
        with open(config_file, "r", encoding='UTF-8') as f:
            return json.load(f)

    def _remove_html_tags(self, text):
        """Remove HTML tags from the input text."""
        return re.sub(r'<.*?>', '', text)

    def _remove_extra_whitespace(self, text):
        """Remove extra whitespace from the input text."""
        return re.sub(r'\s+', ' ', text).strip()

    def _sanitize_text(self, text):
        """Sanitize text by removing unwanted characters."""
        default_punctuation = set(string.punctuation)
        custom_punctuation = {"።", "፡","፣", "፤", "፧", "፥", "፦", "“", "”", "‘", "‘‘", "’’", "…", "•"}
        all_punctuation = default_punctuation.union(custom_punctuation)

        if self.keep_chars:
            all_punctuation -= set(self.keep_chars)

        sanitized_text = re.sub(f"[{''.join(re.escape(c) for c in all_punctuation)}]", " ", text)
        return sanitized_text.strip()

    def _remove_alphanumeric(self, text):
        """Remove alphanumeric characters, preserving specific words."""
         
        words = text.split()
        cleaned_words = []

        for word in words:
            if word in self.preserve_words:
                cleaned_words.append(word)
            else:
                cleaned_words.append(re.sub(r"[A-Za-z0-9]", " ", word))

        return " ".join(cleaned_words)

    def _create_char_map(self):
        """Creates a character translation dictionary for efficient text normalization (This can be considered as a light normalization)."""
        char_replacements = {
            "ሠ": "ሰ", "ሡ": "ሱ", "ሢ": "ሲ", "ሣ": "ሳ", "ሤ": "ሴ", "ሥ": "ስ", "ሦ": "ሶ",
            "ፀ": "ጸ", "ፁ": "ጹ", "ፂ": "ጺ", "ፃ": "ጻ", "ፄ": "ጼ", "ፅ": "ጽ", "ፆ": "ጾ"
        }
        return str.maketrans(char_replacements)

    def clean_text(self, text, output_dir="cleaned_data", output_filename="cleaned_text.txt"):
        """
        Clean and sanitize input text data.
        """
        text = text.translate(self.char_map)  # Normalize characters
        text = self._remove_html_tags(text)
        text = self._sanitize_text(text)
        text = self._remove_alphanumeric(text)
        text = self._remove_extra_whitespace(text)

        # Save cleaned text to file if output_dir is specified
        if output_dir:
            self._save_to_file(text, output_dir, output_filename)

        return text

    def _save_to_file(self, cleaned_data, output_dir, output_filename):
        """Save cleaned data to a file."""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        output_path = os.path.join(output_dir, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_data)
        logging.info(f"Cleaned data saved to {output_path}")

def main():
    """Command-line interface for the text cleaner."""
    parser = argparse.ArgumentParser(description="Clean Tigrinya text data")
    parser.add_argument("input_file", help="Path to the input text or CSV file")
    parser.add_argument("-c", "--config", help="Path to configuration file (JSON)", default="config.json")
    parser.add_argument("-o", "--output_dir", help="Directory to save cleaned text", default="cleaned_data")
    parser.add_argument("-f", "--filename", help="Output filename", default="cleaned_text.txt")
    parser.add_argument("--csv_column", help="If input is CSV, specify which column to clean", default=None)
    args = parser.parse_args()

    cleaner = TextCleaner(config_file=args.config)

    if args.input_file.lower().endswith(".csv") and args.csv_column:
        # Load and clean CSV column
        df = pd.read_csv(args.input_file)
        if args.csv_column not in df.columns:
            raise ValueError(f"Column '{args.csv_column}' not found in CSV file.")
        
        df[args.csv_column] = df[args.csv_column].astype(str).apply(lambda x: cleaner.clean_text(x, output_dir=None))
        
        os.makedirs(args.output_dir, exist_ok=True)
        output_path = os.path.join(args.output_dir, args.filename)
        df.to_csv(output_path, index=False)
        print(f"Cleaned CSV saved to {output_path}")
    else:
        # Treat as plain text
        with open(args.input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        cleaned_text = cleaner.clean_text(text, output_dir=args.output_dir, output_filename=args.filename)
        print(f"Cleaned text saved to {args.output_dir}/{args.filename}")

if __name__ == "__main__":
    main()
    
