'''
프로그래머스 '주사위 게임3'
https://school.programmers.co.kr/learn/courses/30/lessons/181916


#문제 설명
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 
네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.

네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.


# 제한사항
a, b, c, d는 1 이상 6 이하의 정수입니다.


# 입출력 예
a	b	c	d	result
2	2	2	2	2222
4	1	4	4	1681
6	3	3	6	27
2	5	2	6	30
6	4	2	5	2
'''


def solution(a, b, c, d):
    answer = 0
    dice_list = [a, b, c, d]
    dice_set = {a, b, c, d}
    
    if len(dice_set) == 1:
        answer = 1111 * dice_set.pop()
    elif len(dice_set) == 4:
        answer = min(dice_set)
    elif len(dice_set) == 3:
        for x in dice_set:
            if dice_list.count(x) == 2:
                dice_set.remove(x)
                answer = dice_set.pop() * dice_set.pop() 
                break
    elif len(dice_set) == 2:
        p = dice_set.pop()
        q = dice_set.pop()
        if dice_list.count(p) == 2:
            answer = (p + q) * abs(p - q)
        elif dice_list.count(p) == 3:
            answer = (10 * p + q) ** 2
        else:
            answer = (10 * q + p) ** 2
    return answer


def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)