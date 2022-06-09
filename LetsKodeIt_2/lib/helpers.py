from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Helpers():
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator),
                                                   message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locator),
                                                   message=f"Can't find elements by locator {locator}")

    def check_elem_doesnt_present(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator),
                                                   message=f"Element is present and visible by locator: {locator}")

    def find_and_click(self, locator):
        elem = self.find_element(locator)
        elem.click()

    def find_and_send_keys(self, locator, text):
        elem = self.find_element(locator)
        elem.send_keys(text)

    def go_to_page(self, url, new_window=False):
        if new_window:
            self.driver.execute_script(f"window.open('{url}');")
        else:
            self.driver.get(url)
            self.driver.maximize_window()

    def sql_query(self,id_text, course, value):
        sql_query = ("INSERT INTO Courses_Table_Hemush("
                     "ID, course_name, course_count)"
                     f"VALUES ({id_text}, {course}, {value});")
        return sql_query