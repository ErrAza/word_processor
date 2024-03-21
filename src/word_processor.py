import random


def preprocess_word_list(file_path):
    """
    Organize words into a dictionary where the key is a tuple of
    (first letter, length of the word), and the value is a list of words
    that match these criteria.
    """
    organized_words = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()  # Remove any leading/trailing whitespace
            if word:  # Make sure the line isn't empty
                key = (word[0], len(word))
                if key not in organized_words:
                    organized_words[key] = [word]
                else:
                    organized_words[key].append(word)
    return organized_words


def replace_words(sentence, organized_words):
    """
    Replace words in the sentence using the preprocessed word list
    and return the new generated sentence.
    """
    def find_replacement(word):
        """
        Finds a replacement for a given word, using the preprocessed word list
        and returns either the replacement, or the original word itself.
        """
        key = (word[0], len(word))
        replacements = organized_words.get(key, [])
        if replacements:
            # Exclude the original word from the list of potential replacements, if present
            filtered_replacements = [w for w in replacements if w != word]
            if filtered_replacements:
                # Randomly choose a replacement from the filtered list
                return random.choice(filtered_replacements)
        return word

    replaced_words = [find_replacement(word) for word in sentence.split()]
    return ' '.join(replaced_words)
