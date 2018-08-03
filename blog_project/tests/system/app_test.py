from unittest import TestCase
import blog_project.app
from unittest.mock import patch, MagicMock
from blog_project.blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test Author', 'Test')
        blog_project.app.blogs = {'Test Author' : blog}
        with patch('builtins.print') as mocked_print:
            blog_project.app.print_blogs()
            mocked_print.assert_called_with('Test by Test Author (0 posts available)')


