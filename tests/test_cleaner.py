import pytest
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from text_cleaner import TextCleaner

def test_clean_text():
    cleaner = TextCleaner(config_file="config.json")
    input_text = """ብፍላይ ሰባት ብብዝሒ ኣብ ዝምገብሉ ቦታታት ኣብ መዘናግዒታት፡ ኣብያተ መግቢ፡ ውራያት፡ ኮለጃት፡ መዓስከራት መግቢ ብጥንቃቐ ክዳሎ ክኽእል ይግባእ ። ርሑስ ሓድሽ ዓመት !! category health"""
    cleaned_text = cleaner.clean_text(input_text)
    
    assert "test" not in cleaned_text
    assert "123" not in cleaned_text
    assert "!" in cleaned_text

def test_config_loading():
    cleaner = TextCleaner(config_file="config.json")
    assert cleaner.config["output_dir"] == "cleaned_data"
