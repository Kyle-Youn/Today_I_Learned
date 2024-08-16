class Dog:
    # 클래스 변수
    species = "Canis familiaris"

    # 초기화 메서드 (생성자)
    def __init__(self, name, age):
        # 인스턴스 변수
        self.name = name
        self.age = age

    # 인스턴스 메서드
    def description(self):
        return f"{self.name}은(는) {self.age}살입니다."

    # 인스턴스 메서드
    def speak(self, sound):
        return f"{self.name}이(가) {sound}라고 말합니다."

# 인스턴스 생성
dog1 = Dog("멍멍이", 3)
dog2 = Dog("왈왈이", 5)

# 인스턴스 메서드 호출
print(dog1.description())  # 출력: 멍멍이은(는) 3살입니다.
print(dog2.description())  # 출력: 왈왈이은(는) 5살입니다.

# 클래스 변수 접근
print(Dog.species)  # 출력: Canis familiaris

# 인스턴스 메서드 호출
print(dog1.speak("왈왈"))  # 출력: 멍멍이이(가) 왈왈라고 말합니다.
print(dog2.speak("멍멍"))  # 출력: 왈왈이이(가) 멍멍라고 말합니다.
