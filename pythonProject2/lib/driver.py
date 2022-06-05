from selenium import webdriver
import pytest


def get_driver():
    try:
        return webdriver.Chrome()
    except Exception as error:
        raise Exception(error)