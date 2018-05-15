from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AdminHomeAddSentencesTestCase(LiveServerTestCase):

        def setUp(self):
            self.selenium = webdriver.Chrome(r"C:/Users/Lakshi Athapaththu/chromedriver_win32/chromedriver.exe")
            #self.selenium = webdriver.Chrome()
            super(AdminHomeAddSentencesTestCase, self).setUp()

        def test_add_sentences_1(self):
            selenium = self.selenium
            selenium.get('http://127.0.0.1:8000/useract/login/')
            # find the form element
            username = selenium.find_element_by_name('username')
            pw = selenium.find_element_by_name('password')
            submit = selenium.find_element_by_name('submit')

            # Fill the form with data
            username.send_keys('LakshiAtha')
            pw.send_keys('Dinu+0929')
            # submitting the form
            submit.send_keys(Keys.RETURN)
            # check the returned

            sentence = selenium.find_element_by_name('sentence')
            sentence.send_keys('bus going fast')
            selenium.find_element_by_xpath(
                "//select[@name='layer']/option[text()='Layer 1']").click()
            selenium.find_element_by_xpath(
                "//select[@name='class']/option[text()='bus']").click()

            selenium.find_element_by_xpath(
                "//select[@name='parent']/option[text()='inquiry']").click()

            submit = selenium.find_element_by_name('from')

            submit.send_keys(Keys.RETURN)

            #sentence = selenium.find_element_by_name('sentenc')

        def test_add_sentences_2(self):
            selenium = self.selenium
            selenium.get('http://127.0.0.1:8000/useract/login/')
            # find the form element
            username = selenium.find_element_by_name('username')
            pw = selenium.find_element_by_name('password')
            submit = selenium.find_element_by_name('submit')

            # Fill the form with data
            username.send_keys('LakshiAtha')
            pw.send_keys('Dinu+0929')
            # submitting the form
            submit.send_keys(Keys.RETURN)
            # check the returned

            sentence = selenium.find_element_by_name('sentence')
            sentence.send_keys('train going fast')
            selenium.find_element_by_xpath(
                "//select[@name='layer']/option[text()='Layer 1']").click()
            selenium.find_element_by_xpath(
                "//select[@name='class']/option[text()='train']").click()

            selenium.find_element_by_xpath(
                "//select[@name='parent']/option[text()='inquiry']").click()

            submit = selenium.find_element_by_name('from')

            submit.send_keys(Keys.RETURN)

            sentence = selenium.find_element_by_name('sentenc')



        def test_add_sentences_3(self):
            selenium = self.selenium
            selenium.get('http://127.0.0.1:8000/useract/login/')
            # find the form element
            username = selenium.find_element_by_name('username')
            pw = selenium.find_element_by_name('password')
            submit = selenium.find_element_by_name('submit')

            # Fill the form with data
            username.send_keys('LakshiAtha')
            pw.send_keys('Dinu+0929')
            # submitting the form
            submit.send_keys(Keys.RETURN)
            # check the returned

            sentence = selenium.find_element_by_name('sentence')
            sentence.send_keys('bus going fast')
            selenium.find_element_by_xpath(
                "//select[@name='layer']/option[text()='Layer 2']").click()
            selenium.find_element_by_xpath(
                "//select[@name='class']/option[text()='bus itself']").click()

            selenium.find_element_by_xpath(
                "//select[@name='parent']/option[text()='bus']").click()

            submit = selenium.find_element_by_name('from')

            submit.send_keys(Keys.RETURN)

            sentence = selenium.find_element_by_name('sentenc')







