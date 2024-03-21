from word_processor import preprocess_word_list, replace_words


def main():
    """
    Preprocess word list into hash table, then begin user interaction loop.
    """
    file_path = "../data/words_alpha.txt"
    organized_words = preprocess_word_list(file_path)

    print("\t**********************************************")
    print("\t***  Scrabble Word Processor  ***")
    print("\t***  Scrabble Your Words!  ***")
    print("\t**********************************************")
    while True:
        sentence = input("Input your sentence (or type 'exit' to quit): ")
        if sentence.lower() == 'exit':
            break
        replaced_sentence = replace_words(sentence, organized_words)
        print("Scrabbled Sentence:", replaced_sentence)


if __name__ == "__main__":
    main()
