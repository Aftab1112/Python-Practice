def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{key} - {value}" for key, value in kwargs.items())
        print(
            f"Calling : {func.__name__}() function with arguments as ({args_value}) and key value arguments as ({kwargs_value})"
        )

        return func(*args, **kwargs)

    return wrapper


@debug
def hello():
    return "hello"


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


hello()
greet("Aftab", greeting="Hi")
