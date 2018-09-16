from store_app.models.user import UserModel
from store_app.tests.base_test import BaseTest

class UserTest(BaseTest):
    def test_create_user(self):
        with self.app_context():
            user = UserModel('test', 'qwerty')
            user.save_to_database()

            self.assertIsNotNone(UserModel.find_by_username('test'))