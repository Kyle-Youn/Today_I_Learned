import os

def find_files(directory, extension):
    """
    지정된 디렉토리에서 특정 확장자를 가진 파일들의 목록을 반환
    :param directory: 파일들을 검색할 디렉토리의 경로
    :param extension: 찾고자 하는 파일의 확장자
    :return: 찾아진 파일들의 경로 목록
    """
    matched_files = []
    # os.walk를 사용하여 디렉토리와 하위 디렉토리를 모두 탐색
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matched_files.append(os.path.join(root, file))
    return matched_files

if __name__ == "__main__":
    dir_path = input("검색할 디렉토리 경로를 입력하세요: ")
    file_ext = input("찾고자 하는 파일 확장자를 입력하세요 (예: .txt): ")
    files = find_files(dir_path, file_ext)
    print("찾은 파일들:")
    for file in files:
        print(file)
