from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        new_post = Post ('New', "Lorem ipsum")
        