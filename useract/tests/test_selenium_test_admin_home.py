from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AdminHomeTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(r"C:/Users/Lakshi Athapaththu/chromedriver_win32/chromedriver.exe")
        #self.selenium = webdriver.Chrome()
        super(AdminHomeTestCase, self).setUp()
        #self.selenium.implicitly_wait(50000)

    #def tearDown(self):
        #self.selenium.quit()
        #super(EditDetailsTestCase, self).tearDown()

    def test_view_report(self):
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

        date = selenium.find_element_by_name('date')
        date.send_keys('24/04/2018')
        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Ceylon Transport Board']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        link2 = selenium.find_element_by_id("home")
        link2.click()

        date = selenium.find_element_by_name('date')
        date.send_keys('24/04/2018')
        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Sri Lanka Railways']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        link2 = selenium.find_element_by_id("home")
        link2.click()

        date = selenium.find_element_by_name('date')
        date.send_keys('24/05/2018')
        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Ceylon Transport Board']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        link2 = selenium.find_element_by_id("home")
        link2.click()

        date = selenium.find_element_by_name('date')
        date.send_keys('24/05/2018')
        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Sri Lanka Railways']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        link2 = selenium.find_element_by_id("home")
        link2.click()


    def test_view_report_2(self):
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
        date = selenium.find_element_by_name('date')
        date.send_keys('24-04-2018')
        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Sri Lanka Railways']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        #link2 = selenium.find_element_by_id("hom")
        #link2.click()

    def test_view_report_3(self):
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
        date = selenium.find_element_by_name('date')
        date.send_keys('24-04-2018')
        #this format is not acceptable
        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Sri Lanka Railways']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        date = selenium.find_element_by_name('date')
        date.send_keys('7/09/2017')
        #this format is acceptable
        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Sri Lanka Railways']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        link2 = selenium.find_element_by_id("home")
        link2.click()

        date = selenium.find_element_by_name('date')
        date.send_keys('32/09/2017')
        # this format is acceptable have correct it.
        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Sri Lanka Railways']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        link2 = selenium.find_element_by_id("home")
        link2.click()

        date = selenium.find_element_by_name('date')
        date.send_keys('3/9/2017')
        #this format is acceptable

        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Sri Lanka Railways']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        link2 = selenium.find_element_by_id("home")
        link2.click()

        date = selenium.find_element_by_name('date')
        date.send_keys('3/9/201995')
        # this format is acceptable

        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Sri Lanka Railways']").click()

        submit = selenium.find_element_by_id('view')

        submit.send_keys(Keys.RETURN)

        link2 = selenium.find_element_by_id("home")
        link2.click()

        date = selenium.find_element_by_name('date')
        date.send_keys('343/9/201995')
        # this format is not acceptable

        selenium.find_element_by_xpath("//select[@name='authority']/option[text()='Sri Lanka Railways']").click()

        submit = selenium.find_element_by_id('view')
        submit.send_keys(Keys.RETURN)

        link2 = selenium.find_element_by_id("home")
        link2.click()













