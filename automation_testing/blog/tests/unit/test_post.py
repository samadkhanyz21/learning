from unittest import TestCase
from blog.post import Post


class PostTest(TestCase):
    def test_create_post(self):

        """For testing a post"""
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):

        """For testing dictionary converts to JSON or not"""
        p = Post('Test', 'Test Content')
        expected = {
            'title': 'Test',
            'content': 'Test Content'
        }

        self.assertDictEqual(expected, p.json())

