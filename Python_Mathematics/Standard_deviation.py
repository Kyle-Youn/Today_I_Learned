import math

def mean(numbers):
    """
    산술평균 (Arithmetic Mean):
    모든 숫자의 합을 숫자의 개수로 나눈 값
    수학적 표현: μ = (Σx) / n
    여기서 Σx는 모든 x의 합, n은 숫자의 개수
    """
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    중앙값 (Median):
    정렬된 데이터에서 중앙에 위치한 값
    홀수 개의 데이터: 중앙에 있는 값
    짝수 개의 데이터: 중앙에 있는 두 값의 평균
    """
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        return (sorted_numbers[length//2 - 1] + sorted_numbers[length//2]) / 2
    else:
        return sorted_numbers[length//2]

def variance(numbers):
    """
    분산 (Variance):
    각 데이터 포인트와 평균의 차이를 제곱한 값들의 평균
    수학적 표현: σ² = Σ(x - μ)² / n
    여기서 x는 각 데이터 포인트, μ는 평균, n은 데이터의 개수
    """
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    """
    표준편차 (Standard Deviation):
    분산의 제곱근
    수학적 표현: σ = √(σ²)
    분산의 제곱근을 취함으로써 원래 데이터와 같은 단위를 가지게 됨
    """
    return math.sqrt(variance(numbers))

# 예시 데이터
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"평균: {mean(data)}")
print(f"중앙값: {median(data)}")
print(f"분산: {variance(data)}")
print(f"표준편차: {standard_deviation(data)}")
