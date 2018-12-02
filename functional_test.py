from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        # start a selenium webdriver to pop up a real firefox browser window
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # use it to open up a web page which we're expecting to be served from a local PC
        # Edith has heard about a cool new online to-do app
        # she goes to check out its homepage
        self.browser.get('http://localhost:8000')

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
        time.sleep(1) # explicit wait

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr') # return a list that may be empty
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # there is still a text box inviting her to add another item
        # she enters "use peacock feathers to make a fly" (she is very methodical)
        self.fail('Finish the test!')

        # the page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list
        # then she sees that the site has generated a unique URL for her
        # there is some explanatory text to that effect

        # she visites the URL - her to-do list is still there

        # satisfied, she goes back to sleep

if __name__ == "__main__":
    # launch the unittest runner, which will automatically find test
    # classes and methods in the file and run them
    unittest.main(warnings='ignore')