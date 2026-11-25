def outer_message():
    message="hello from outer"
    def inner_message():
        print(message)
    inner_message()
outer_message()
