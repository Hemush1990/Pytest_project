import random
import string

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Automation_05_22.lib.driver import get_driver
from Automation_05_22.lib.test_logger import logger
from selenium.webdriver.support.ui import Select

driver = get_driver()


def go_to_page(url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}');")
    else:
        driver.get(url)
        driver.maximize_window()


def find_and_click(loc, timeout=10):
    elem = find(loc, timeout)
    elem.click()


def find_and_send_keys(loc, inp_text, timeout=10):
    elem = find(loc, timeout)
    elem.send_keys(inp_text)


def find(loc, timeout=20, should_exist=True, get_text="", get_attribute=""):
    try:
        elem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located(loc),
                                                    message=f"Element '{loc}' not found!")
    except Exception as e:
        logger(e, error=True)
        if should_exist:
            raise Exception(e)
        return False
    if get_text:
        return elem.text
    elif get_attribute:
        return elem.get_attribute(get_attribute)
    return elem


def find_all(loc, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_all_elements_located(loc),
                                                        message=f"Elements '{loc}' not found!")
    except Exception as e:
        logger(e, error=True)
        return False
    return elements


def wait_element_disappear(loc, timeout=10):
    WebDriverWait(driver, timeout).until_not(expected_conditions.presence_of_element_located(loc))


def wait_for_page(page="", not_page="", timeout=10):
    if page:
        WebDriverWait(driver, timeout).until(expected_conditions.url_contains(page))
    elif not_page:
        WebDriverWait(driver, timeout).until_not(expected_conditions.url_contains(not_page))


def random_string(symbols_count):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=symbols_count))


def write_to_file(path_to_file, written_data):
    with open(path_to_file, 'a+') as f:
        f.write(written_data)


def select_1(loc, valu):
    select = Select(find(loc))
    select.select_by_value(valu)


def find_by_id_and_send_keys(loc, inp_text):
    elem = driver.find_element_by_id(loc)
    elem.send_keys(inp_text)


def scroll_the_page():
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")


def delete_chars(loc):
    elem = find(loc)
    elem.send_keys(Keys.BACK_SPACE)


