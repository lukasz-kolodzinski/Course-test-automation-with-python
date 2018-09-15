from starter_code.models.item import ItemModel
from starter_code.tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_create_item(self):
        with self.app_context():
            item_test = ItemModel('salt', 3.50)
            item_test.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('salt'))
