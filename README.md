# TextCleaner for Tigrinya

##  Purpose

**TextCleaner** is a robust preprocessing tool tailored for **Tigrinya**, a low-resource language. It streamlines the process of cleaning, normalizing, and preparing text data for NLP tasks such as classification, clustering, and information retrieval.

The tool supports both `.txt` and `.csv` files, removes noise (like HTML, punctuation, or alphanumerics), and allows customization to **preserve important terms or punctuation** relevant to your dataset.

---

##  Features

- **Supports TXT and CSV** formats
- **Removes HTML tags**, alphanumeric characters, and non-Tigrinya symbols
- **Preserves words/punctuation** based on user configuration
-  **Character normalization** (e.g., `ፀ` → `ጸ`)
-  **Flexible output** saving to custom folders/filenames
-  **JSON-based configuration**
-  **Command-Line Interface (CLI)** and importable Python class

---

## Installation

###  Prerequisites

- Python 3.6+
- Pip

###  Setup Instructions

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

5. (Optional) If you want to run tests, you can install pytest:
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


## Tests
Unit tests are provided to ensure the tool works correctly. You can run the tests using pytest:

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

