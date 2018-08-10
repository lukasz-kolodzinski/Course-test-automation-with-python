from blog_project.blog import Blog

MENU_PROMPT = 'Enter "c" to create new blog; "l" to list blogs; "r" to read one, "p" to create post; "q" to quit'
blogs = dict()
POST_TEMPLATE = '''
    >>>{}<<<<

    {}

    '''

def menu():
    print_blogs ()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection =input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print("{}".format(blog))
        print(blog)

def ask_create_blog():
    title = input('Please, provide blog title: ')
    author = input('Please, enter author name: ')
    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Please, provide blog title: ')

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
     pass
