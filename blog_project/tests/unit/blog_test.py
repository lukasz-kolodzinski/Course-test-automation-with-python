from unittest import TestCase
from blog_project.blog import Blog

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

    def test_create_new_post_verify_posts_amount(self):
        blog_with_post = Blog ("Ian Kowalsky", "Cookies Time")
        blog_with_post.create_new_post("Something delicious", "We love sweets and so on")

        self.assertEqual(1, len(blog_with_post.posts))

    def test_create_new_post_verify_post_title(self):
        blog_with_post = Blog ("Ian Kowalsky", "Cookies Time")
        blog_with_post.create_new_post("Something delicious", "We love sweets and so on")

        self.assertEqual("Something delicious", blog_with_post.posts[0].title)

    def test_create_new_post_verify_post_content(self):
        blog_with_post = Blog ("Ian Kowalsky", "Cookies Time")
        blog_with_post.create_new_post("Something delicious", "We love sweets and so on")

        self.assertEqual("We love sweets and so on", blog_with_post.posts[0].content)

    def test_create_json_blog(self):
        new_blog = Blog ("Ian Kowalsky", "Cookies Time")
        new_blog.create_new_post("Something delicious", "We love sweets and so on")
        expected_json = {
            "author" : "Ian Kowalsky",
            "title" : "Cookies Time",
            "posts" : [{
                "title" : "Something delicious",
                "content" : "We love sweets and so on" }]
        }

        self.assertDictEqual(expected_json, new_blog.create_json())
