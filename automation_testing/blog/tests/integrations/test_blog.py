from unittest import TestCase
from blog.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Author', b.author)
        self.assertListEqual([], b.posts)