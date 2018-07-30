from unittest import TestCase
from blog_project.post import Post

class PostTest(TestCase):
    def test_create_post(self):
        new_post = Post("New", "Lorem ipsum")

        self.assertEqual("New", new_post.title)
        self.assertEqual("Lorem ipsum", new_post.content)

    def test_create_json(self):
        new_post = Post("New", "Lorem ipsum")
        expected_json = {
            "title" : "New",
            "content" : "Lorem ipsum"
        }

        self.assertDictEqual(expected_json, new_post.create_json())


