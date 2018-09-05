from unittest import TestCase
from course_application.app import app

class TestHome (TestCase):
    def test_home(self):
        with app.test_client() as homesite:
            response = homesite.get("/")

            self.assertEqual(response.status_code, 200)