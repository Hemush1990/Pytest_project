import pytest
from selenium import webdriver

from LetsKodeIt_2.pages.courses import conn
from LetsKodeIt_2.lib.helpers import Helpers
from test_data import test_data


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def open_url(driver):
    Helpers.go_to_page(driver, test_data.main_url)


@pytest.fixture()
def create_table():
    sql_query = ("CREATE TABLE Courses_HP("
                 "id INT IDENTITY(1,1) PRIMARY KEY",
                 "course_name VARCHAR(50)",
                 "course_count int"
                 ");")
    return sql_query


@pytest.fixture()
def unique_id_generator():
    i=10
    for i in range(50):
        i += 1
    return i
