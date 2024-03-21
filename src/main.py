from word_processor import preprocess_word_list, replace_words


def main():
    # Adjust the file path as necessary to point to your word list
    file_path = "../data/words_alpha.txt"
    organized_words = preprocess_word_list(file_path)

    print("Enter a sentence to replace its words with others of the same initial letter and length:")
    while True:
        sentence = input("Input your sentence (or type 'exit' to quit): ")
        if sentence.lower() == 'exit':
            break
        replaced_sentence = replace_words(sentence, organized_words)
        print("Replaced Sentence:", replaced_sentence)


if __name__ == "__main__":
    main()
