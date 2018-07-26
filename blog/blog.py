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



