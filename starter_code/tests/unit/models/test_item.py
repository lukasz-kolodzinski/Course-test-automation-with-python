from unittest import TestCase
from starter_code.models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        test_item = ItemModel("salt", 3.20)

        self.assertEqual(test_item.name, "salt")
        self.assertEqual(test_item.price, 3.20)

    def test_create_json(self):
        test_item = ItemModel("salt", 3.20)
        expected_json = {
            "name": "salt",
            "price": 3.20
        }

        self.assertEqual(expected_json, test_item.json())