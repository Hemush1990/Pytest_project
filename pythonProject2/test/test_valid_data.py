import string
import time
from random import random

from pages import main_page
from test_data import test_data1
from lib import test_loger, helpers, driver


def test_valid_recorder(generate_random_text):
    helpers.go_to_page(test_data1.url)
    main_page.type_input(generate_random_text)
    main_page.get_characters_count()
    main_page.get_characters_without_symbol()
    main_page.get_words_count()
    main_page.get_sentences()
    test_loger.logger("The valid test is passed")


def test_actions(generate_random_text):
    helpers.go_to_page(test_data1.url)
    main_page.type_input(generate_random_text, clear=True)
    main_page.get_sentences()
    main_page.get_words_count()
    main_page.get_characters_count()
    main_page.get_characters_without_symbol()
    test_loger.logger("The test with actions is passed")
