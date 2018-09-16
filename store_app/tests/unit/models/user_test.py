from store_app.models.user import UserModel
from store_app.tests.unit.models.unit_base_test import TestBase

class UserTest(TestBase):
    def test_create_user(self):
        user = UserModel("test", "zxcv")

        self.assertEqual(user.ussername,"test")
        self.assertEqual(user.password,"zxcv")