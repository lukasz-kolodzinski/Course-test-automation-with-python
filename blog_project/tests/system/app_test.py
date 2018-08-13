from unittest import TestCase
import blog_project.app
from unittest.mock import patch
from blog_project.blog import Blog
from blog_project.post import Post

class AppTest(TestCase):
    def test_menu_user_input(self):
        with patch('builtins.input') as mocked_input:
            blog_project.app.menu()
            #mocked_input.assert_called_with('Enter "c" to create new blog; "l" to list blogs; "r" to read one, "p" to create post; "q" to quit')
            mocked_input.assert_called_with(blog_project.app.MENU_PROMPT)

    def test_menu_call_print_blogs(self):
        with patch('blog_project.app.print_blogs') as mocked_print_blogs:
             with patch('builtins.input'):
                blog_project.app.menu()
                mocked_print_blogs.assert_called_with()

    def test_print_blogs(self):
        blog = Blog('Test Author', 'Test')
        blog_project.app.blogs = {'Test Author' : blog}
        with patch('builtins.print') as mocked_print:
            blog_project.app.print_blogs()
            mocked_print.assert_called_with('Test by Test Author (0 posts available)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test title', 'Fake Author')
            blog_project.app.ask_create_blog()
            self.assertIsNotNone(blog_project.app.blogs.get('Test title'))

    def test_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        blog_project.app.blogs = {'Test': blog}
        with patch('builtins.input', return_value = 'Test'):
            with patch('blog_project.app.print_posts') as mocked_print_posts:
                blog_project.app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog('Test', 'Test Author')
        blog_project.app.blogs = {'Test': blog}
        blog.create_new_post('Test Title', 'Test Content')
        with patch('blog_project.app.print_post') as mocked_print_post:
            blog_project.app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Test Title', 'Test Content')
        expected_print = '''
    >>>Test Title<<<<

    Test Content

    '''
        with patch('builtins.print') as mocked_print:
            blog_project.app.print_post(post)

            mocked_print.assert_called_with(expected_print)