'''
# 문제 설명
온라인 서비스를 이용하기 위해서 닉네임이 필요합니다. 이때 닉네임이 될 수 있는 조건은 다음과 같습니다.

닉네임의 길이가 4자 이상 8자 이하여야합니다.
닉네임에는 소문자 l과w, 대문자 O와 W를 사용할 수 없습니다.
이외의 영어 대소문자와 숫자는 모두 사용이 가능합니다.
주어진 solution 함수는 사용할 수 없는 닉네임 nickname을 받아 사용할 수 있는 닉네임으로 바꿔주는 함수입니다. 이때 닉네임을 변경하는 규칙은 다음과 같으며 첫 번째 규칙부터 순서대로 적용합니다.

소문자 l을 대문자 I로 변경합니다.
소문자 w를 두 개의 소문자 v, 즉 vv로 변경합니다.
대문자 W를 두 개의 대문자 V, 즉 VV로 변경합니다.
대문자 O를 숫자 0으로 변경합니다.
수정된 닉네임의 길이가 4 미만일 경우 뒤에 소문자 o를 길이가 4가 될때까지 이어붙입니다.
수정된 닉네임의 길이가 8보다 클 경우 8번째 문자까지만 사용합니다.
주어진 solution 함수에는 위의 규칙 중 올바르게 적용되지 않는 것이 있습니다. solution 함수가 올바르게 작동하도록 한 줄을 수정해주세요.

# 제한사항
1 ≤ nickname의 길이 ≤ 10
nickname은 영어 대소문자와 숫자로만 이루어져있습니다.

# 입출력 예
nickname	result
"WORLDworld"	"VV0RLDvv"
"GO"	"G0oo"

#입출력 예 설명
입출력 예 #1
닉네임 "WORLDworld"는 1, 2, 3, 4, 6 단계를 거쳐 "VV0RLDvv"가 됩니다.
"WORLDworld" -> "WORLDworId" -> "WORLDvvorId" -> "VVORLDvvorId" -> "VV0RLDvvorId" -> "VV0RLDvv"
입출력 예 #2
닉네임 "GO"는 4, 5 단계를 거쳐 "G0oo"가 됩니다.
"GO" -> "G0" -> "G0oo"
'''


def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    while len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer
