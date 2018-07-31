from unittest import TestCase
from blog_project.app import *
from unittest.mock import patch
from blog_project.blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        new_blog = Blog ("Ian Rankin", "Dark Stories")
        
        with patch ('builtins.print') as mocked_print:
            print_blogs()
            mocked_print.assert_called_with()

