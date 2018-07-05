from unittest import TestCase
from blog.post import Post

class PostTest(TestCase):
    def test_create_post(self):
        new_post = Post("New", "Lorem ipsum")

        self.assertEqual("New", new_post.title)
        self.assertEqual("Lorem ipsum", new_post.content)


