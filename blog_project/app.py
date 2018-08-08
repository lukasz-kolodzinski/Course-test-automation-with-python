MENU_PROMPT = 'Enter "c" to create new blog; "l" to list blogs; "r" to read one, "p" to create post; "q" to quit'
blogs = dict()

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

def ask_create_blog():
    pass

def ask_read_blog():
    pass

def ask_create_post():
    pass
