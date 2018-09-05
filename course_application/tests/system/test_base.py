from unittest import TestCase
from course_application.app import app

class BaseTest(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()