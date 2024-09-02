def decimal_to_nine(decimal_number):
    if decimal_number == 0:
        return "0"
    nine_base = ''
    while decimal_number > 0:
        remainder = decimal_number % 9
        nine_base = str(remainder) + nine_base
        decimal_number = decimal_number // 9
    return nine_base

# 예제
decimal_number = 156
nine_base_number = decimal_to_nine(decimal_number)
print(nine_base_number)  # 출력: '192'
