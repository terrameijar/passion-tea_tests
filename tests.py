from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from pageobjects import *
import unittest
import time


class PassionTeaTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.practiceselenium.com/"
        #global cust_form = landingPage(driver)

    '''def test_checkout(self):
        driver = self.driver
        driver.get

        # 1 click on tea item
        # 2 click on checkout button
        # 3 call form_fill and billing_info methods
        '''


    def test_checkout(self):
        driver = self.driver
        driver.get(self.base_url)
        cust_form = landingPage(driver)
        cust_form.navigate_to_checkout()
        cust_form.form_fill("terrameijar@gmail.com","Terra","Paradise Lane\nBulawayo\nZimbabwe")
        cust_form.billing_info("American Express","4111 1111 1111 1111","Jane Doe", 342)
        time.sleep(5)



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
