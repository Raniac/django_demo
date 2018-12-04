from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    # only methods that begin with test_ will get run as tests
    
    def setUp(self):
        # start a selenium webdriver to pop up a real firefox browser window
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # use it to open up a web page which we're expecting to be served from a local PC
        # Edith has heard about a cool new online to-do app
        # she goes to check out its homepage
        self.browser.get(self.live_server_url)

        # check by making a test assertion that the page has 'django' in its title
        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she types "buy peacock feathers" into a text box
        # Edith's hobby is trying fly-fishing lures
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter, the page updates, and now the page lists
        # "1: buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER) # hit Enter and the page refreshes
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # there is still a text box inviting her to add another item
        # she enters "use peacock feathers to make a fly" (she is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        # the page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list
        # then she sees that the site has generated a unique URL for her
        # there is some explanatory text to that effect
        self.fail('Finish the test!')

        # she visites the URL - her to-do list is still there

        # satisfied, she goes back to sleep