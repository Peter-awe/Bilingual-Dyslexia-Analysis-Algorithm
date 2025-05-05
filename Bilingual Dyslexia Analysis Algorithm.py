import re

# English vowel pronunciation rules dictionary
english_vowel_rules = {
    'a': ['æ', 'eɪ', 'ɑː', 'ɔː', 'ə'],
    'e': ['e', 'iː', 'ə'],
    'i': ['ɪ', 'aɪ'],
    'o': ['ɒ', 'əʊ', 'ɔː', 'uː'],
    'u': ['ʌ', 'juː', 'uː']
}

# French letter combination pronunciation rules dictionary
french_letter_combination_rules = {
    'eau': 'o'
}


def analyze_english_errors(word, correct_pronunciation):
    """
    Analyze pronunciation errors in English words
    :param word: English word
    :param correct_pronunciation: Correct pronunciation
    :return: Error information, or None if there is no error
    """
    for vowel in english_vowel_rules:
        pattern = re.compile(rf'{vowel}')
        matches = pattern.findall(word)
        for match in matches:
            # Simple example, just check if the vowel pronunciation is in the rule list
            if match in correct_pronunciation and correct_pronunciation[correct_pronunciation.index(match)] not in english_vowel_rules[match]:
                return f"English vowel {match} pronunciation error, the correct pronunciation rules may be {english_vowel_rules[match]}"
    return None


def analyze_french_errors(word, correct_pronunciation):
    """
    Analyze pronunciation errors in French words
    :param word: French word
    :param correct_pronunciation: Correct pronunciation
    :return: Error information, or None if there is no error
    """
    for combination in french_letter_combination_rules:
        if combination in word:
            if french_letter_combination_rules[combination] not in correct_pronunciation:
                return f"French letter combination {combination} pronunciation error, the correct pronunciation should be {french_letter_combination_rules[combination]}"
    return None


def generate_assessment_report(reading_data):
    """
    Generate a personalized assessment report
    :param reading_data: Reading data, formatted as [(language, word, correct_pronunciation, actual_pronunciation), ...]
    :return: Assessment report
    """
    report = []
    for language, word, correct_pronunciation, actual_pronunciation in reading_data:
        if language == 'English':
            error = analyze_english_errors(word, correct_pronunciation)
            if error:
                report.append(f"English word {word} error: {error}")
        elif language == 'French':
            error = analyze_french_errors(word, correct_pronunciation)
            if error:
                report.append(f"French word {word} error: {error}")
    return report


# Example reading data
reading_data = [
    ('English', 'pint', 'paɪnt', 'pɪnt'),
    ('French', 'beau', 'bo', 'bɛau')
]

# Generate the assessment report
assessment_report = generate_assessment_report(reading_data)
for error in assessment_report:
    print(error)
    