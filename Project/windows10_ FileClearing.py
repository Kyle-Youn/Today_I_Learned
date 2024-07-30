import os

# 모든 파일을 삭제할 폴더 경로 선언
becleared_directory = '폴더 경로 입력'

# 해당 폴더에 모든 파일 삭제
for filename in os.listdir(becleared_directory):
    file_path = os.path.join(becleared_directory, filename)
    os.remove(file_path)  # 파일'만' 삭제!!(폴더는 X)