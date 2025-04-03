def setup_teardown(func):
    def wrapper():
        print("it starts now")
        func()
        print("it ends now")

    return wrapper


@setup_teardown
def betw():
    print("hello world")
    print("hello boss")


betw()

