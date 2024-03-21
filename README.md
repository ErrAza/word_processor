# Scrabble Word Processor

Scrabble Word Processor is a Python console application written to assist with those that are very serious about [Scrabble](https://en.wikipedia.org/wiki/Scrabble).

Makes use of the word list found here: https://github.com/dwyl/english-words/blob/master/words_alpha.txt

Given the sentence **lightly fried fish are delicious**, the program may return **likable frier frog arm delegated**. Running it again may yield **lenient fuses foam any digressed**.


## Installation

1. Ensure you have **Python** 3.12 installed on your system, if not, it can be found here: https://www.python.org/downloads/
2. Either clone the repository using [Git](https://git-scm.com/downloads), or alternatively download the project directly from GitHub as a zip file.

## Usage

Open a terminal/console window, change your working directory to that of where you downloaded the project.

### Example:

Open your system's console/terminal shell and use the following commands:

```bash
cd path/to/downloaded/project/src
```

```bash
python main.py
```

## Overview

```bash
word_replacer_app/
│
├── data/
│   └── word_list.txt          # Text file containing the word list
│
├── src/
│   ├── __init__.py            # Makes src a Python package
│   ├── word_processor.py      # Contains functions for processing words
│   └── main.py                # Entry point of the application, handles user interaction
│
└── README.md                  # Documentation explaining the application, usage, etc.
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

