
def attempt(n=5):

    def decorator(func):
        def wraps(*args, **kwargs):
            print("******************")
            print(n)
            func(*args, **kwargs)
            print("******************")
            return
        return wraps
    return decorator


@attempt(n=5)
def my_print(name):
    print(f"Hello everybody {name}")
@attempt(n=5)
def my_print1():
    print("Hello every")
@attempt(n=5)
def my_print2(name):
    print(f"Hello body {name}")
@attempt(n=5)
def my_print3(name):
    print(f"Hello qitti {name}")
@attempt(n=5)
def my_print4(name):
    print("Hello ebony")

my_print(name = 'Kamadzi')
my_print1()
my_print2(name = 'Faseless')
my_print3(name = 'Tikiro')
my_print4(name = 'Kamadzi')