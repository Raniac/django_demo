from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from web.views import home_page
from django.template.loader import render_to_string

# Create your tests here.

# unit tests are really about testing logic, flow control, and configuration.
# using templates is a good solution to deal with HTML.
# refactoring impoves the code without changing its functionality.
# unit tests make sure that refactoring is behavior preserving.
# when refactoring, work on either the code or the tests, but not both at once.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     response = self.client.get('/') # pass client.get the url to test
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))

    #     self.assertTemplateUsed(response, "home.html")
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        # instead of testing constants
        # we're now testing our implementation
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')