from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EditDetailsTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(r"C:/Users/Lakshi Athapaththu/chromedriver_win32/chromedriver.exe")
        #self.selenium = webdriver.Chrome()
        super(EditDetailsTestCase, self).setUp()
        #self.selenium.implicitly_wait(50000)

    #def tearDown(self):
        #self.selenium.quit()
        #super(EditDetailsTestCase, self).tearDown()

    def test_edit_details_get(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/useract/edit/')
        #username = selenium.find_element_by_id('abc')
        #pw = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_name('sub')

        # Fill the form with data
        #username.send_keys('Lakshi')
        #pw.send_keys('Dinu+0929')
        # submitting the form
        submit.send_keys(Keys.RETURN)
        # check the returned
