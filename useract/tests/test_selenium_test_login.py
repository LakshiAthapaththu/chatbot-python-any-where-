from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(r"C:/Users/Lakshi Athapaththu/chromedriver_win32/chromedriver.exe")
        #self.selenium = webdriver.Chrome()
        super(LoginTestCase, self).setUp()
        self.selenium.implicitly_wait(50000)

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/useract/login/')
        # find the form element
        username = selenium.find_element_by_name('username')
        pw = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_name('submit')

        # Fill the form with data
        username.send_keys('Lakshi')
        pw.send_keys('Dinu+0929')
        # submitting the form
        submit.send_keys(Keys.RETURN)
        # check the returned

        link1 = selenium.find_element_by_id('h3pb')
        link1.click()

        link2 = selenium.find_element_by_id("home")
        link2.click()

        link1 = selenium.find_element_by_id('h3pb')
        link1.click()

        link2 = selenium.find_element_by_id("editDetails")
        link2.click()

        link2 = selenium.find_element_by_id("home")
        link2.click()

        link2 = selenium.find_element_by_id("editDetails")
        link2.click()

        link2 = selenium.find_element_by_id("home")
        link2.click()

        link2 = selenium.find_element_by_id("editDetails")
        link2.click()

        link2 = selenium.find_element_by_id("viewhistory")
        link2.click()

        link2 = selenium.find_element_by_id("home")
        link2.click()

        link2 = selenium.find_element_by_id("editDetails")
        link2.click()

        link2 = selenium.find_element_by_id("userguide")
        link2.click()

        link2 = selenium.find_element_by_id("home")
        link2.click()

        link2 = selenium.find_element_by_id("userguide")
        link2.click()

        link2 = selenium.find_element_by_id("home")
        link2.click()

        link2 = selenium.find_element_by_id("userguide")
        link2.click()

        link2 = selenium.find_element_by_id("viewhistory")
        link2.click()

        link2 = selenium.find_element_by_id("home")
        link2.click()

        link2 = selenium.find_element_by_id("userguide")
        link2.click()

        link2 = selenium.find_element_by_id("editDetails")
        link2.click()

        link2 = selenium.find_element_by_id("home")
        link2.click()

    def test_register_1(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/useract/login/')
        # find the form element
        username = selenium.find_element_by_name('username')
        pw = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_name('submit')

        # Fill the form with data
        username.send_keys('Laks')
        pw.send_keys('Dinu+0929')
        # submitting the form
        submit.send_keys(Keys.RETURN)
        # check the returned

    def test_register_2(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/useract/login/')
        # find the form element
        username = selenium.find_element_by_name('username')
        pw = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_name('submit')

        # Fill the form with data
        username.send_keys('Lakshi')
        pw.send_keys('Dinu+09')
        # submitting the form
        submit.send_keys(Keys.RETURN)
        # check the returned

    def test_register_3(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/useract/login/')
        # find the form element
        username = selenium.find_element_by_name('username')
        submit = selenium.find_element_by_name('submit')

        # Fill the form with data
        username.send_keys('Lakshi')
        # submitting the form
        submit.send_keys(Keys.RETURN)
        # check the returned

    def test_register_4(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/useract/login/')
        # find the form element
        username = selenium.find_element_by_name('username')
        pw = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_name('submit')

        # Fill the form with data
        pw.send_keys('Dinu+0929')
        # submitting the form
        submit.send_keys(Keys.RETURN)
        # check the returned

    def test_register_5(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/useract/login/')
        # find the form element
        username = selenium.find_element_by_name('username')
        submit = selenium.find_element_by_name('submit')

        # Fill the form with data
        username.send_keys('Laks')
        # submitting the form
        submit.send_keys(Keys.RETURN)
        # check the returned

    def test_register_6(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/useract/login/')
        # find the form element
        username = selenium.find_element_by_name('username')
        pw = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_name('submit')

        # Fill the form with data
        pw.send_keys('Dinu')
        # submitting the form
        submit.send_keys(Keys.RETURN)
        # check the returned






























