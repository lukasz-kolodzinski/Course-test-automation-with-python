from store_app.models.store import StoreModel
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