from store_app.models.store import StoreModel
from store_app.tests.integration.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store_with_no_items(self):
        store = StoreModel("test")

        self.assertListEqual(store.items.all(), [])
        