from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class landingPage(object):
    def __init__(self, driver):
        self.driver = driver
        #WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_partial_link_text("Passion").is_visible())

    def navigate_to_checkout(self):
        collectionBtn = self.driver.find_element_by_css_selector("a#wsb-button-00000000-0000-0000-0000-000450914897")
        collectionBtn.click()
        title = self.driver.title
        assert "Menu" in title
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "wsb-button-00000000-0000-0000-0000-000451961556")))
        self.driver.find_element_by_id("wsb-button-00000000-0000-0000-0000-000451961556").click()

    def form_fill(self, email, name, address):
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(email)
        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("address").clear()
        self.driver.find_element_by_id("address").send_keys(address)

    def billing_info(self,cType,cNumber,cName,cvv):
        cTypeDropDown = self.driver.find_element_by_id("card_type")
        #cardDict = ['Visa', 'MasterCard', 'Diners Club', 'American Express']
        Select(cTypeDropDown).select_by_visible_text(cType)
        cNumberElement = self.driver.find_element_by_id("card_number")
        cNumberElement.clear()
        cNumberElement.send_keys(cNumber)
        cNameElement = self.driver.find_element_by_id("cardholder_name")
        cNameElement.clear()
        cNameElement.send_keys(cName)
        cvvElement = self.driver.find_element_by_id("verification_code")
        cvvElement.clear()
        cvvElement.send_keys(cvv)
        submitBtn = self.driver.find_element_by_class_name("btn-primary")
        submitBtn.click()

    def talkTeaForm(self,name,email,subject,message):
        nameField = self.driver.find_element_by_name("name")
        emailField = self.driver.find_element_by_id("email")
        subjectField = self.driver.find_element_by_name("subject")
        messageField = self.driver.find_element_by_name("message")
        submitBtn = self.driver.find_element_by_css_selector("input.form-submit")

        nameField.clear()
        nameField.send_keys(name)
        emailField.clear()
        emailField.send_keys(email)
        subjectField.clear()
        subjectField.send_keys(subject)
        messageField.clear()
        messageField(message)


