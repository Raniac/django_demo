from selenium import webdriver
# start a selenium webdriver to pop up a real firefox browser window
browser = webdriver.Firefox()
# use it to open up a web page which we're expecting to be served from a local PC
browser.get('http://localhost:8000')
# check by making a test assertion that the page has 'django' in its title
assert 'Django' in browser.title