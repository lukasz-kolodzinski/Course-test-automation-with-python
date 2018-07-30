from blog_project.post import Post

class Blog:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.posts = []

    def __repr__(self):
        return '{} by {} ({} post{} available)'.format(self.title,
                                             self.author,
                                             len(self.posts),
                                            's' if len(self.posts) != 1 else '')

    def create_new_post(self, title, content):
        self.posts.append(Post(title, content))
        print((self.posts[0]))

    def create_json(self):
        return {
            "author" : self.author,
            "title" : self.title,
            "posts" : [post.create_json() for post in self.posts]
        }
