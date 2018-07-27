from unittest import TestCase
from blog.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        new_blog = Blog("Ian Kowalsky", "Cookies Time")

        self.assertEqual("Ian Kowalsky", new_blog.author)
        self.assertEqual("Cookies Time", new_blog.title)
    #   self.assertListEqual([], new_blog.posts)
        self.assertEqual(0, len(new_blog.posts))

    def test_repr_none_post(self):
        none_post_blog = Blog("Ian Kowalsky", "Cookies Time")

        self.assertEqual('Cookies Time by Ian Kowalsky (0 posts available)',
                         none_post_blog.__repr__())

    def test_repr_one_post(self):
        single_post_blog = Blog("Ian Kowalsky", "Cookies Time")
        single_post_blog.posts = ["One"]

        self.assertEqual('Cookies Time by Ian Kowalsky (1 post available)',
                         single_post_blog.__repr__())

    def test_repr_many_posts(self):
        many_posts_blog = Blog("Ian Kowalsky", "Cookies Time")
        many_posts_blog.posts = ["One", "Two", "Three"]

        self.assertEqual('Cookies Time by Ian Kowalsky (3 posts available)',
                         many_posts_blog.__repr__())

