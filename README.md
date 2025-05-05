# Bilingual Dyslexia Analysis Tool

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python tool for analyzing pronunciation errors in English-French bilingual children with dyslexia.

## Features

- 🎯 **English Error Analysis**: Detects vowel pronunciation errors using IPA rules
- 🥖 **French Error Analysis**: Identifies mispronounced letter combinations
- 📊 **Personalized Reports**: Generates detailed error reports for each child
- 🔧 **Extensible Rules**: Easy to add new pronunciation rules

## Installation

```bash
git clone https://github.com/Peter-awe/bilingual-dyslexia-analysis.git
cd bilingual-dyslexia-analysis
```

## Usage

1. Prepare your data in this format:
```python
reading_data = [
    ('English', 'pint', 'paɪnt', 'pɪnt'),  # (language, word, correct_pronunciation, actual_pronunciation)
    ('French', 'beau', 'bo', 'bɛau')
]
```

2. Run the analysis:
```python
from bilingual_dyslexia_analysis import generate_assessment_report

report = generate_assessment_report(reading_data)
for error in report:
    print(error)
```

## Example Output
```
English word pint error: English vowel i pronunciation error, the correct pronunciation rules may be ['ɪ', 'aɪ']
French word beau error: French letter combination eau pronunciation error, the correct pronunciation should be o
```

## Customization

### Add English Rules
```python
english_vowel_rules = {
    'a': ['æ', 'eɪ', 'ɑː', 'ɔː', 'ə'],
    # Add more rules...
}
```

### Add French Rules  
```python
french_letter_combination_rules = {
    'eau': 'o',
    # Add more rules...
}
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

Developed by [Peter-awe](https://github.com/Peter-awe)
