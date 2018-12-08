from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from web.views import home_page
from django.template.loader import render_to_string
from web.models import Item, List

# Create your tests here.

# unit tests are really about testing logic, flow control, and configuration.
# using templates is a good solution to deal with HTML.
# refactoring impoves the code without changing its functionality.
# unit tests make sure that refactoring is behavior preserving.
# when refactoring, work on either the code or the tests, but not both at once.

# only methods that begin with test_ will get run as tests

class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        # instead of testing constants
        # we're now testing our implementation
        self.assertTemplateUsed(response, 'home.html')

# class ItemModelTest(TestCase):
class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/web/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)
        
        response = self.client.get(f'/web/{correct_list.id}/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list 1')
        self.assertNotContains(response, 'other list 2')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/web/{correct_list.id}/')
        # response.context represents the context to pass into 
        # the render function
        self.assertEqual(response.context['list'], correct_list)

class NewListTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        # the urls with no trailing slash are action urls which modify the database
        self.client.post(
            f'/web/{correct_list.id}/add_item', 
            data={'item_text': 'A new item for an existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            f'/web/{correct_list.id}/add_item', 
            data={'item_text': 'A new list item'}
        )
        
        self.assertRedirects(response, f'/web/{correct_list.id}/')
