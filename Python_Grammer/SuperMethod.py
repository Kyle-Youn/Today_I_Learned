class Parent:
    def __init__(self, value):
        self.value = value

    def show(self):
        print("Parent Value:", self.value)

class Child(Parent):
    def __init__(self, value, child_value):
        super().__init__(value)  # 부모 클래스의 __init__ 호출
        self.child_value = child_value

    def show(self):
        super().show()  # 부모 클래스의 show 메서드 호출
        print("Child Value:", self.child_value)

# 객체 생성 및 메서드 호출
child_instance = Child(10, 20)
child_instance.show()
