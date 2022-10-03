import datetime


def decorator_func(func):
    now = datetime.datetime.now()
    
    def finish():
        func()
        print(f"Function {func.__name__} was finished in {now}")
    
    return finish


@decorator_func
def notification():
    print("Don't forget, you have some plans!")

@decorator_func
def say_something():
    print("gaegegrdh")


notification()
say_something()