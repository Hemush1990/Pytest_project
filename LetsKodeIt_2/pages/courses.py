import time

import pytest
from selenium.webdriver.common.by import By
from LetsKodeIt_2.lib.helpers import Helpers
import pymssql

conn = pymssql.connect(server='sqllearn.volo.local',
                       user='pythonuser',
                       password='cA7BHCrLBEGh4CmZ',
                       database='AdventureWorks2019')

all_courses_btn = (By.XPATH, "//a[normalize-space()='ALL COURSES']")
search_fld = (By.XPATH, "//input[@name='course']")
search_btn = (By.XPATH, "//button[@type='submit']")
search_result = (By.XPATH, "//div[@id='course-list']//div[@class = 'col-lg-4 col-md-4 col-sm-6 col-xs-12']")


class MainPage(Helpers):

    def create_db_table(driver, sql_query):
        cursor = conn.cursor()
        cursor.execute(sql_query)
        conn.commit()
        cursor.close()

    def search_courses(self, courses):
        self.find_and_click(all_courses_btn)
        self.find_and_send_keys(search_fld, courses)
        self.find_and_click(search_btn)
        time.sleep(2)
        results = self.find_elements(search_result)
        return len(results)
