def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Pre-processing
        print("Before the function call")
        result = func(*args, **kwargs)
        # Post-processing
        print("After the function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


'''
Before the function call
Hello, Alice!
After the function call
'''
