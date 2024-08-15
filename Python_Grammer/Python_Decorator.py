def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@log_decorator
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

display_info("John", 25)
