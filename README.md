# Scrabble Word Processor

**Scrabble Word Processor** is a Python console application written to assist with those that are very serious about [Scrabble](https://en.wikipedia.org/wiki/Scrabble).

Makes use of the word list found here, containing **370,000** words: https://github.com/dwyl/english-words/blob/master/words_alpha.txt

Given the sentence **lightly fried fish are delicious**, the program may return **likable frier frog arm delegated**. Running it again may yield **lenient fuses foam any digressed**.

## Installation & Setup

Ensure you have **Python** **>= 3.12** installed on your system, if not, it can be found here: https://www.python.org/downloads/

1. Either clone the project using [Git](https://git-scm.com/downloads), or alternatively, download the project directly from GitHub as a zip file. _Ensure you unzip this file_
2. Check the repository [releases](https://github.com/ErrAza/word_processor/releases) for the latest tagged releases and download the **zip** or **tar.gz** depending on operating system/preference.

## Usage

Open a terminal/console window, change your working directory to that of where you downloaded the project.

### Example:

In your system's console/terminal, make use of the following commands:

```bash
cd path/to/downloaded/project/src
```

Once you are inside the project's **src** directory, use **python** to run the application:

```bash
python main.py
```

### Console Output

```code
**********************************************
	***  Scrabble Word Processor  ***
	***   Scrabble Your Words!    ***
**********************************************
Input your sentence (or type 'exit' to quit): lightly fried fish are delicious
Scrabbled Sentence: lactary funli fete ave deligated
Input your sentence (or type 'exit' to quit): lightly fried fish are delicious
Scrabbled Sentence: lousily fairy falx awn disinhume
Input your sentence (or type 'exit' to quit): lightly fried fish are delicious
Scrabbled Sentence: langaha flyer fiar ave diplumbic
Input your sentence (or type 'exit' to quit):
```

## Basic Project Overview

```bash
word_processor/
│
├── data/
│   └── words_alpha.txt        # Text file containing the word list
│
├── src/
│   ├── __init__.py            # Makes src a Python package
│   ├── word_processor.py      # Contains functions for processing words
│   └── main.py                # Entry point of the application, handles user interaction
│
├── test/
│   └── test_scrabbler.py      # Basic pytest suite for the application
│
├── requirements.txt           # Required Packages to be installed for development
│
└── README.md                  # Documentation explaining the application, usage, etc.
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

