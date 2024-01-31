class Post:

    def __init__(self, title, content):

        """Posting a blog in our app"""
        self.title = title
        self.content = content

    def json(self):

        """Converting a post into JSON"""
        return {
            'title': self.title,
            'content': self.content
            }

