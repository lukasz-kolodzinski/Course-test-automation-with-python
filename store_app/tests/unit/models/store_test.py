from store_app.models.store import StoreModel
from store_app.tests.unit.models.unit_base_test import *

class StoreTest(TestBase):
    def test_create_store(self):
        store = StoreModel("test")

        self.assertEqual(store.name, "test")