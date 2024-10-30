try:
    # 사용자로부터 두 숫자 입력 받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 나눗셈 결과 계산
    result = num1 / num2
except ZeroDivisionError:
    # 0으로 나누려고 했을 때 처리
    print("오류: 0으로 나눌 수 없습니다.")
else:
    # 예외가 발생하지 않았을 경우 결과 출력
    print("결과:", result)
finally:
    # 마지막에 항상 실행
    print("계산 시도가 완료되었습니다.")



try:
    userData = int(input())
    result = int(10 / userData)
except:
    print('sorry~~')
else:
    print('예외발생 X')
finally:
    print('예외발생 여부와 상관없이 실행되는 코드입니다.')
