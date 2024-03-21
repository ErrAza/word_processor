from word_processor import preprocess_word_list, replace_words


def main():
    """
    Preprocess word list into hash table, then begin user interaction loop.
    """
    file_path: str = "../data/words_alpha.txt"
    organized_words: {} = preprocess_word_list(file_path)

    print(
        "\n\t**********************************************"
        "\n\t     ***  Scrabble Word Processor  ***"
        "\n\t      ***  Scrabble Your Words!  ***"
        "\n\t**********************************************"
    )

    while True:
        sentence = input("Input your sentence (or type 'exit' to quit): ")
        if sentence.lower() == "exit":
            break
        replaced_sentence = replace_words(sentence, organized_words)
        print(f"Scrabbled Sentence: {replaced_sentence}")


if __name__ == "__main__":
    main()
