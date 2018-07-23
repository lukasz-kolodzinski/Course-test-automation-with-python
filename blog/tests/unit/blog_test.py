from unittest import TestCase
from blog.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        new_blog = Blog("Ian Kowalsky", "Cookies Time")

        self.assertEqual("Ian Kowalsky", new_blog.author)
        self.assertEqual("Cookies Time", new_blog.title)
    #   self.assertListEqual([], new_blog.posts)
        self.assertEqual(0, len(new_blog.posts))
        

