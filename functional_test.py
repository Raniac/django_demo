from selenium import webdriver
import unittest

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
        self.fail('Finish the test!')

        # she is invited to enter a to-do item straight away

        # she types "buy peacock feathers" into a text box
        # Edith's hobby is trying fly-fishing lures

        # when she hits enter, the page updates, and now the page lists
        # "1: buy peacock feathers" as an item in a to-do list

        # there is still a text box inviting her to add another item
        # she enters "use peacock feathers to make a fly" (she is very methodical)

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