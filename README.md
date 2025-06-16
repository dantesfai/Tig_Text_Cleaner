# TextCleaner for Tigrinya

##  Purpose

**TextCleaner** is a robust preprocessing tool tailored for **Tigrinya**, a low-resource language. It streamlines the process of cleaning, normalizing, and preparing text data for NLP tasks such as classification, clustering, and information retrieval.

The tool supports both `.txt` and `.csv` files, removes noise (like HTML, punctuation, or alphanumerics), and allows customization to **preserve important terms or punctuation** relevant to your dataset.

- **Multi-file support**: Can process both **TXT** and **CSV** files.
- **Customizable cleaning**: Remove HTML tags, alphanumeric characters, and unwanted punctuation while preserving specific words and characters.
- **Configurable settings**: Easily configure which punctuation and words to preserve, using the **config.json** file.
- **Command-line interface (CLI)**: Run the tool with various input files and configurations directly from the command line.
- **Flexible output**: Cleaned text can be saved to a user-defined directory and filename.
- **Package-ready**: Can be installed via `setup.py` and used as a module or CLI tool.

## Installation

###  Prerequisites

- Python 3.6 or higher
- `pip` package installer


###  Setup Instructions

1. Clone the repository to your local machine Clone the repository and install the required packages:
   ```bash
   git clone https://github.com/dantesfai/Tig_text_cleaner.git
 

2. Navigate to the project directory:

   ```bash 
   cd text_cleaner

3. 
```bash 
   pip install -r requirements.txt
```
### OR Install via Source

   Clone the repository and install using `setup.py`:

   ```bash
      git clone https://github.com/dantesfai/Tig_text_cleaner.git
      cd text_cleaner
      pip install .
   ```
This will install the tool and make the CLI command textcleaner available globally.

### (Optional) Install Pytest for Running Tests If you want to run unit tests: 
   
   ```bash 
         pip install pytest
   ```  
After installation, you can use text-cleaner as a CLI command (if included as entry point in setup.py).

### Option 2: Install Dependencies Manually

   If you're running without installing the full package:
      ```bash 
         pip install -r requirements.txt 
      ```
 
## Usage

### Command-Line Interface (CLI)

After installation, you can run the tool using:

   ```bash 
   textcleaner input.txt -c config.json -o cleaned_data -f output.txt 
   ```

   
Or if using the script directly:

   ```bash
   python text_cleaner.py input.txt -c config.json -o cleaned_data -f output.txt
   ```

To clean a specific column from a CSV:
   ```bash
   python text_cleaner.py input.csv --csv_column text -o cleaned_data -f cleaned_output.csv
   ```

<b>Arguments</b>:
    - input.txt: Path to the input file (either a .txt or .csv file).
    - -c config.json: (Optional) Path to the configuration file. Default is config.json.
    - -o cleaned_data: (Optional) Directory where the cleaned text will be saved. Default is  cleaned_data.
    - -f output.txt: (Optional) Filename for the output cleaned text. Default is cleaned_text txt.output.txt


### Configuration

You can customize the cleaning process by editing the <code>config.json</code> file. This allows you to:

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
  
## Tests
   Unit tests are provided to ensure the tool works correctly. You can run the tests using pytest:

   ```bash
      pytest
   ```
   This will run all the tests defined in the tests/ directory, ensuring that the tool functions as expected.

## License
This tool is open-source and free to use for research purposes under the <b>MIT License</b>.

## Contributing
Contributions are welcome! If you have improvements, bug fixes, or new features to contribute, feel free to fork this repository, make your changes, and submit a pull request.

## Acknowledgements
Thanks to the NLP community for open-source contributions and resources that helped guide the development of this tool.

