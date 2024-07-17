def count_messages(filename):
    # 딕셔너리를 초기화합니다.
    message_count = {}
    
    # 파일을 열고 각 줄을 읽습니다.
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # 닉네임이 포함된 줄을 찾습니다.
            if line.startswith('[') and ']' in line:
                # 닉네임을 추출합니다.
                end_index = line.find(']')
                nickname = line[1:end_index]
                
                # '오픈채팅봇' 메시지는 카운트하지 않습니다.
                if nickname != '오픈채팅봇':
                    # 메시지 카운트를 업데이트합니다.
                    if nickname in message_count:
                        message_count[nickname] += 1
                    else:
                        message_count[nickname] = 1
    
    # 완성된 딕셔너리를 반환합니다.
    return message_count

def save_message_counts(message_counts, output_filename):
    # 닉네임을 한글, 알파벳 순서로 명시적으로 정렬합니다.
    sorted_nicks = sorted(message_counts.items(), key=lambda item: (item[0]))

    # 결과를 파일에 쓰기
    with open(output_filename, 'w', encoding='utf-8') as file:
        for nickname, count in sorted_nicks:
            file.write(f"{nickname}: {count}\n")
    print(f"Data has been saved to {output_filename}")

# 파일 경로는 실제 파일 위치로 대체하여 사용
input_file_path = 'C:/Users/hjyou/Desktop/KakaoTalk_20240716_2133_23_139_group.txt'
output_file_path = 'C:/Users/hjyou/Desktop/sorted_message_counts.txt'

# 메시지 카운트 함수 실행
result = count_messages(input_file_path)
print("Message counts:", result)

# 결과를 파일에 저장
save_message_counts(result, output_file_path)
