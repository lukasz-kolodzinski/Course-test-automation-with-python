from course_application.tests.system.test_base import BaseTest
import json

class TestHome (BaseTest):
    def test_home(self):
        with self.app() as homesite:
            response = homesite.get("/")

            self.assertEqual(response.status_code, 200)

    def test_home_response_json(self):
        with app.test_client() as homesite:
            response = homesite.get("/")

            self.assertEqual(json.loads(response.get_data()),
                             {'message': 'Hello world'})