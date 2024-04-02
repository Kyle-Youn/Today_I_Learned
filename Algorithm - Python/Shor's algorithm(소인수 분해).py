'''
[Shor's algorithm]

양자컴퓨터를 이용한 큐비트 연산 시, 다항 시간안에 소인수 분해를 할 수 있는 양자 알고리즘이다. 피터 쇼어(Peter Shor)가 1994년의 논문에서 제안한 알고리즘이다. 
현재 다항 시간안에 소인수분해를 하는 알고리즘중 가장 빠른 알고리즘이라고 알려져 있다.

쇼어 알고리즘이 중요한 이유는 RSA 암호화와 관련이 있다. 
RSA 암호화는 큰 소수의 합성수를 소인수로 분해하는 문제는 고전 컴퓨터로 다항 시간에 풀 수 없는 문제로 알려져 있다. 
따라서 RSA 암호화 체계는 소인수 분해의 어려움에 기반하여 설계되어 있다고 할 수 있다. 
그래서 쇼어의 양자 알고리즘으로 정수의 소인수 분해 문제를 다항 시간 안에 풀 수 있게 되면, RSA 암호화를 사용하는 모든 서비스가 큰 보안 위협에 처하게 된다.

쇼어 알고리즘은 합동 관계의 주기성을 이용하여 소인수 분해를 한다.
쇼어 알고리즘 자체는 고전 컴퓨터로도 구현할 수 있다. 다만, 고전 컴퓨터로 구현한 쇼어 알고리즘은 여전히 지수적인 시간 복잡도를 가지기 때문에, 다항 시간에 소인수 분해를 하려면 양자 컴퓨터를 이용해야 한다.





[쇼어 소인수분해 방법]

입력: 두 개의 소수 p, q의 곱으로 만들어진 합성수 N=p*q
출력: N의 소인수 p, q

절차:
1. 1보다 크고 N보다 작은 임의[arbitrary]의 정수 a를 선택한다.

2. 만일 N과 a의 최대공약수 gcd가 1이 아니면, 운이 좋게 소인수 p를 발견한 것이다. 따라서 p=gcd, q=N//gcd를 반환하고 종료한다.

3. 함수 f(x)=a^x (mod N)의 주기 r을 찾는다. 여기서 찾은 주기 r이 짝수가 아니라면, 1번 단계부터 다시 시작한다.

4. 주기 r로부터 두 개의 최대공약수 gcd1=gcd(N, a^(r//2)) + 1), gcd2=gcd(N, a^(r//2)) - 1)를 찾는다.

5. 여기서 찾은 두 개의 수 gcd1, gcd2 중 하나라도 1이거나 N이라면 1번 단계부터 다시 시작한다. 아니라면, 마침내 소인수들을 찾았으므로 gcd1, gcd2를 반환하고 종료한다.
'''


# Shor's algorithm - python

import random 
import math 

import random
import math

def mod_pow(a, x, N):
    y = 1
    while (x > 0):
        if ((x & 1) == 1):
            y = (y * a) % N
        x = x >> 1
        a = (a * a) % N
    return y

def findPeriodByModPow(N, a):
    for x in range(1, N):
        if (mod_pow(a, x, N) == 1):
            return x
    return -1

def factorizeByShor(N):
    while(True):
        a = random.randint(2, N - 1)
        gcd = math.gcd(N, a)
        if (gcd != 1):
            return gcd, N // gcd
        r = findPeriodByModPow(N, a)
        if (r % 2 != 0 or mod_pow(a, r//2, N) == N - 1):
            continue
        gcd1 = math.gcd(N, mod_pow(a, r//2, N) + 1)
        gcd2 = math.gcd(N, mod_pow(a, r//2, N) - 1)
        if (gcd1 != 1 and gcd1 != N) or (gcd2 != 1 and gcd2 != N):
            return gcd1, gcd2
