from django.test import TestCase
from .models import Category, Items
from .forms import CategoryForm, ItemForm

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Beverages", slug="beverages")
        self.assertEqual(category.name, "Beverages")
        self.assertEqual(category.slug, "beverages")

class ItemModelTest(TestCase):
    def test_create_item(self):
        category = Category.objects.create(name="Beverages", slug="beverages")
        item = Items.objects.create(
            title="Coffee", sku="COF123", Category=category, selling_price=5.99
        )
        self.assertEqual(item.title, "Coffee")
        self.assertEqual(item.Category.name, "Beverages")

class CategoryFormTest(TestCase):
    def test_valid_category_form(self):
        form = CategoryForm(data={'name': 'Beverages', 'slug': 'beverages'})
        self.assertTrue(form.is_valid())

class ItemFormTest(TestCase):
    def test_valid_item_form(self):
        category = Category.objects.create(name="Beverages", slug="beverages")
        form = ItemForm(data={
            'title': 'Coffee', 'sku': 'COF123', 'Category': category.id, 'selling_price': 5.99
        })
        self.assertTrue(form.is_valid())