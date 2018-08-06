from unittest import TestCase
import blog_project.app
from unittest.mock import patch
from blog_project.blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test Author', 'Test')
        blog_project.app.blogs = {'Test Author' : blog}
        with patch('builtins.print') as mocked_print:
            blog_project.app.print_blogs()
            mocked_print.assert_called_with('Test by Test Author (0 posts available)')

    def test_menu_user_input(self):
        with patch('builtins.input') as mocked_input:
            blog_project.app.menu()
            #mocked_input.assert_called_with('Enter "c" to create new blog; "l" to list blogs; "r" to read one, "p" to create post; "q" to quit')
            mocked_input.assert_called_with(blog_project.app.MENU_PROMPT)

