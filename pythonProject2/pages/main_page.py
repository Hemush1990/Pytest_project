from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from lib import helpers, driver

# Locators

input_field = (By.ID, "counter")
char_count_recorder = (By.XPATH, "//p[@title='Characters']//following-sibling::p")
char_without_spaces_recorder = (By.XPATH, "//p[@title='Characters Without Spaces']//following-sibling::p")
words_recorder = (By.XPATH, "//p[@title='Words']//following-sibling::p")
sentences_recorder = (By.XPATH, "//p[@title='Words']//following-sibling::p")


def type_input(text, clear = ""):
    helpers.find_and_send_keys(input_field, text)
    global size
    if clear:
        helpers.delete_chars(input_field)
        size = len(text)-1
    else:
        size = len(text)
    return size



def get_characters_count():
    count = helpers.find(char_count_recorder, get_text=True)
    print(count)
    assert int(count) == size, f"The characters count isn't equal to {count}"


def get_characters_without_symbol():
    count = helpers.find(char_without_spaces_recorder, get_text=True)
    assert int(count) == size, f"The characters without spaces count isn't equal to {count}"


def get_words_count():
    count = helpers.find(words_recorder, get_text=True)
    assert int(count) == 1, f"The words count isn't equal to {count}"


def get_sentences():
    count = helpers.find(sentences_recorder, get_text=True)
    assert int(count) == 1, f"The sentences count isn't equal to {count}"
