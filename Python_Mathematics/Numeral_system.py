def convert_to_base(number, base):
    digits = '0123456789ABCDEF'
    result = ''
    while number > 0:
        number, remainder = divmod(number, base)
        result = digits[remainder] + result
    return result

# 예시: 45를 2진수로 변환
binary = convert_to_base(45, 2)
print(f"2진수: {binary}")
# 출력: 2진수: 101101
