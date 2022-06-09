import pytest

from LetsKodeIt_2.lib.helpers import Helpers
from LetsKodeIt_2.pages.courses import MainPage
from LetsKodeIt_2.test_data import test_data


@pytest.mark.parametrize("courses", ['python', 'selenium', 'java'])
def test_check_count(driver, courses):
    lib = Helpers(driver)
    main = MainPage(driver)
    lib.open_url(test_data.main_url)
    course_count = main.search_courses(courses)
    main.create_db_table(sql_query=("INSERT INTO Courses_HP("
                                    "course_name, course_count)"
                                    f"VALUES ('{courses}', {course_count});"))
