from unittest import TestCase
from course_application.app import app
import json

class TestHome (TestCase):
    def test_home(self):
        with app.test_client() as homesite:
            response = homesite.get("/")

            self.assertEqual(response.status_code, 200)

    def test_home_response_json(self):
        with app.test_client() as homesite:
            response = homesite.get("/")

            self.assertEqual(json.loads(response.get_data()),
                             {'message': 'Hello world'})