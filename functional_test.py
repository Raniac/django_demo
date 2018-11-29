from selenium import webdriver

# start a selenium webdriver to pop up a real firefox browser window
browser = webdriver.Firefox()

# use it to open up a web page which we're expecting to be served from a local PC
# Edith has heard about a cool new online to-do app
# she goes to check out its homepage
browser.get('http://localhost:8000')

# check by making a test assertion that the page has 'django' in its title
# she notices the page title and header mention to-do lists
assert 'Django' in browser.title

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

browser.quit()