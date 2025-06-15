# TextCleaner for Tigrinya

## Purpose

**TextCleaner** is a robust text cleaning and preprocessing tool designed for Tigrinya, a low-resource language. It simplifies the process of sanitizing and preparing text data for NLP tasks, including text classification and information retrieval. The tool supports handling both **CSV** and **TXT** files, and allows for the removal of unwanted characters, HTML tags, and alphanumeric content, while preserving specific words or punctuation as required by the user.

## Features

- **Multi-file support**: Can process both **TXT** and **CSV** files.
- **Customizable cleaning**: Remove HTML tags, alphanumeric characters, and unwanted punctuation while preserving specific words and characters.
- **Configurable settings**: Easily configure which punctuation and words to preserve, using the **config.json** file.
- **Command-line interface (CLI)**: Run the tool with various input files and configurations directly from the command line.
- **Flexible output**: Cleaned text can be saved to a user-defined directory and filename.
- **IDF-based stopword generation**: Generate stopwords based on **IDF (Inverse Document Frequency)** scores to improve NLP tasks.
- **Visualization**: Plot IDF curves to visualize word importance and filter non-informative words.

## Installation

### Prerequisites

Make sure you have **Python 3.x** installed. This project also requires several dependencies, which can be installed via **pip**.

### Steps to Install

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/text_cleaner.git

2. Navigate to the project directory:
   ```bash
   cd text_cleaner

3. Install required dependencies:

   ```bash 
   pip install -r requirements.txt 

4. (Optional) If you want to run tests, you can install **pytest**:
   ```bash 
   pip install pytest
  

## Usage

### Command-Line Interface (CLI)
   
To clean a text file, use the following command:

   ```bash
   python text_cleaner.py input.txt -c config.json -o cleaned_data -f output.txt
   ```

    - input.txt: Path to the input file (either a .txt or .csv file).
    - -c config.json: (Optional) Path to the configuration file. Default is config.json.
    - -o cleaned_data: (Optional) Directory where the cleaned text will be saved. Default is  cleaned_data.
    - -f output.txt: (Optional) Filename for the output cleaned text. Default is cleaned_text txt.output.txt

### Configuration

You can customize the cleaning process by editing the config.json file. This allows you to:

   - Specify characters to keep during sanitization.
   - Define a list of preserved words that should not be cleaned.
   - Customize the output directory and filename.

**Example** config.json:
```bash
{
    "keep_punctuation": ["-","'","."],
    "preserve_words": ["category", "headline"],
    "output_dir": "cleaned_data",
    "output_filename": "cleaned_text.txt"
}
```

### Example Usage

1. Cleaning a Text File:

   ```bash

python text_cleaner.py data/input.txt -o output -f cleaned_text.txt

2. Running with Custom Configurations:

If you want to use a custom configuration:

  ```bash 
python text_cleaner.py data/input.txt -c config.json -o output -f cleaned_text.txt
```

3. IDF Stopword Generation:

You can use the TextCleaner class to generate stopwords based on IDF (Inverse Document Frequency) and visualize the distribution of word importance. The tool generates a plot of IDF values and saves stopwords based on a user-defined threshold.

## Tests
To ensure the tool works correctly, unit tests are provided. You can run the tests using pytest:

```bash
 pytest
```
This will run all the tests defined in the tests/ directory, ensuring that the tool functions as expected.

## License
This tool is open-source and free to use for research purposes under the MIT License.

## Contributing
Contributions are welcome! If you have improvements, bug fixes, or new features to contribute, feel free to fork this repository, make your changes, and submit a pull request.

## Acknowledgements
Thanks to the NLP community for open-source contributions and resources that helped guide the development of this tool.
Special thanks to contributors and researchers working on Tigrinya language resources, whose work helped shape this project.

