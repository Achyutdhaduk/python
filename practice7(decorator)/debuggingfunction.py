def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(i) for i in args)
        keargs_value = ', '.join(f"{k}={v}"for k,v in kwargs.items())
        print(f"{func.__name__} is called with {args_value} and {keargs_value}")
        return func(*args,**kwargs) 
    return wrapper    


@debug
def hello():
    print("hellooooo")


@debug
def greet(name,greeting = 'hello'):
    print(f"{greeting} {name}")


hello()
greet('achyut', greeting="hanji")    