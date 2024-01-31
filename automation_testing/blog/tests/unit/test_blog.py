from unittest import TestCase
from blog.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Author', b.author)
        self.assertListEqual([], b.posts)

    # Testing for 1 post
    def test_repr(self):
        b = Blog('Test', 'Author')
        b2 = Blog('My Day', 'Abdul')

        self.assertEqual(b.__repr__(), "Test by Test Author (0 posts)")
        self.assertEqual(b2.__repr__(), "My Day by Abdul(0 posts)")

    # Testing for multiple posts
    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Author')
        b.posts = ['test']
        b2 = Blog('My Day', 'Abdul')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), "Test by Test Author (1 post)")
        self.assertEqual(b2.__repr__(), "My Day by Abdul (2 posts)")

    def test_create_post_in_blog(self):
        b = Blog('Test', 'Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')