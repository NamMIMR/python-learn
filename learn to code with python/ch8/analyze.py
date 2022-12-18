import logging
from typing import List, Tuple

"""
The analyze module uses the Flesch-Kincaid readability test to analyze text and
produce a readability score. This score is then converted into a
grade-based readability category.
"""


def count_words(text: str) -> Tuple[List[str],int]:
    """
    This function counts the number of words in a sting of text 
    using space as delimeter.
    """

    words = text.split()
    total_words = len(words)
    logging.info(str(total_words) +' words in total.')
    return words, total_words

def count_sentences(text: str) -> int:
    """
    This function counts the number of sentences in a string of text 
    using period, semicolon, question mark and exclamation mark as 
    terminals.
    """

    total_sentences = 0
    terminal_char = '.;?!'

    for char in text:
        if char in terminal_char:
            total_sentences += 1

    logging.info(str(total_sentences) + ' sentences in total.')
    return total_sentences

def count_syllables(words: List[str]) -> int:
    """
    This function takes a list of words and returns a total 
    count of syllables across all words in the list.
    """

    total_syllables = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        total_syllables += word_count

    logging.info(str(total_syllables) + ' syllables in total.')


    return total_syllables

def count_syllables_in_word(word: str) -> int:
    """
    This function takes a word in the form of a string 
    and returns the number of syllables. Note this function is 
    a heuristic and may not be 100% accurate.
    """
    
    count = 0

    endings = '.,;!?:'
    last_char = word[-1]

    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]
    
    vowels = "aeiouAEIOU"
    prev_char_was_vowel = False

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count += 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    
    if processed_word[-1] in 'yY':
        count += 1


    return count

# Calculate readability score.
def readability_formula(total_words: int, total_sentences: int, total_syllables: int) -> float:
    """
    This function calculate the readability score using the 
    Flesch-Kincaid readability formula by accept the number 
    of words, sentences, syllables in the same text of string,
    return the score of the readability.
    """
    score = (206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words))
    return score

# Get the readability level by given score.
def readability_level(score: float) -> Tuple[str,...]:
    '''
    This function takes a Flesch-Kincaid score and prints the 
    corresponding reading level.
    '''

    logging.debug(score)
    readability = ''
    note = ''

    if 0.0 <= score <= 30.0:
        readability = 'College Graduate'
        note = 'Very difficult to read. Best understood by university graduates.'
    elif 30.0 < score <= 50.0:
        readability = 'College'
        note = 'Difficult to read.'
    elif 50.0 < score <= 60.0:
        readability = '10th-12th grade'
        note = 'Fairly difficult to read.'
    elif 60.0 < score <= 70.0:
        readability = '8th & 9th grade'
        note = 'Plain English. Easily understood by 13-15 years old'
    elif 70.0 < score <= 80.0:
        readability = '7th grade'
        note = 'Fairly easy to read.'
    elif 80.0 < score <= 90.0:
        readability = '6th grade'
        note = 'Easy to read. Conversational English for consumers.'
    elif 90.0 < score <= 100.0:
        readability = '5th grade'
        note = 'Very easy to read. Easily understood by an average 11-year-old student.'

    # logging.info('Reading level of {0}: {1}'.format(readability, note))


    return readability, note

def compute_readability(text: str):
    """
    This function takes a text string of any length and prints out a 
    grade-based readability score.
    """

    logging.debug(text)

    # Init all local variable we need.
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0.0
    
    words, total_words = count_words(text)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)


    score = readability_formula(total_words, total_sentences, total_syllables)
    readability, note = readability_level(score)
    print('Reading level of', readability + ':', note)


if __name__ == '__main__':
    import ch1text
    logging.basicConfig(level=logging.INFO)
    text = ch1text.text
    compute_readability(text)