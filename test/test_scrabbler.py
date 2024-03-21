import pytest

from src.word_processor import preprocess_word_list, replace_words


class TestScrabbler:
    """Test class for Scrabbler Word Processor module."""

    @pytest.fixture
    def organized_words(self):
        file_path = "data/words_alpha.txt"
        return preprocess_word_list(file_path)

    @staticmethod
    def test_a22(organized_words):
        a22_other_words = [
            "anatomicophysiological",
            "aquopentamminecobaltic",
            "astrospherecentrosomic",
        ]
        a22_word = "alkylbenzenesulfonates"
        output_word = replace_words(a22_word, organized_words)
        assert output_word in a22_other_words

    @staticmethod
    def test_blank(organized_words):
        blank_word = ""
        output_word = replace_words(blank_word, organized_words)
        assert output_word == blank_word

    @staticmethod
    def test_spaces(organized_words):
        two_space_phrase = "two space phrase"
        output_two_space = replace_words(two_space_phrase, organized_words)
        two_space_count = output_two_space.count(" ")
        assert two_space_count == 2
