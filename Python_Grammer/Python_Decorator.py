def my_decorator(func):
    def wrapper():
        print("함수가 시작됩니다.")
        func()
        print("함수가 종료되었습니다.")
    return wrapper

@my_decorator
def say_hello():
    print("안녕하세요!")

# 데코레이터가 적용된 함수 호출
say_hello()


def decorator(func):
    def new_func(*args, **kwargs):
        print("새로운 함수 실행")
        return func(*args, **kwargs)
    return new_func()

@decorator
def original_function():
    print("원래 함수 실행")
    return "반환값"

result = original_function
print(result)
