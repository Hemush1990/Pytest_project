import random
import string

import pytest
from selenium.webdriver.chrome import webdriver


@pytest.fixture()
def generate_random_text():
    text = ''.join([random.choice(string.ascii_lowercase) for _ in range(7)])
    return text


@pytest.fixture(params=['Chrome'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    yield driver
    driver.quit()
