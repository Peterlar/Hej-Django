from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    def test_item_name_is_requried(self):
        form = Itemform {{'name': ''}}
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0],'This field is required.')