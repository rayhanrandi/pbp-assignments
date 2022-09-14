from django.test import TestCase
from katalog.models import CatalogItem

# Create your tests here.
class CatalogTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name='Test',
            item_price=10000000,
            item_stock=1,
            description='Unit Test',
            rating=5,
            item_url='https://github.com/rayhanrandi/pbp-assignments')
        
        CatalogItem.objects.create(
            item_name='Pessi',
            item_price=10,
            item_stock=1,
            description='Goat',
            rating=10,
            item_url='https://github.com/rayhanrandi/pbp-assignments'
        )
    
    def test_if_item_exists(self):
        test = CatalogItem.objects.get(item_name='Test')
        goat = CatalogItem.objects.get(item_name='Pessi')
        self.assertEqual(test.item_name, 'Test')
        self.assertEqual(goat.item_name, 'Pessi')
        