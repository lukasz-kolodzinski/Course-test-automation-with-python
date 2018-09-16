from store_app.models.store import StoreModel
from store_app.models.item import ItemModel
from store_app.tests.integration.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store_with_no_items(self):
        store = StoreModel("test")

        self.assertListEqual(store.items.all(), [])

    def test_save_store_into_db(self):
        with self.app_context():
            store = StoreModel("test")
            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name("test"))

    def test_save_item_into_store(self):
        with self.app_context():
            store = StoreModel("test")
            store.save_to_db()
            item = ItemModel("salt", 3.20, 1)
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel("test")
            store.save_to_db()
            item = ItemModel("sugar", 4.50, 1)
            item.save_to_db()
            expected_json = {
                "name": "test",
                    "items": [{"name": "sugar", "price": 4.50}]
            }

            self.assertDictEqual(expected_json, store.json())