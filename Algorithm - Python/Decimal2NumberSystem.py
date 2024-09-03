def decimal_to_NumberSystem(decimal_number, NumberSystem):
    if decimal_number == 0:
        return "0"
    NumberSystem_base = ''
    while decimal_number > 0:
        remainder = decimal_number % NumberSystem
         NumberSystem_base = str(remainder) +  NumberSystem_base
        decimal_number = decimal_number // NumberSystem
    return NumberSystem_base

# 예제
decimal_number = 156
NumberSystem = 8
NumberSytem_number = decimal_to_NumberSystem(decimal_number, NumberSystem)
print(NumberSytem_number)  # 출력: '234'
