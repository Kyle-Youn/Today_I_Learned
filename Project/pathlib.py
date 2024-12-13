from pathlib import Path

p = Path('/home/user') / 'documents' / 'file.txt'
print(p)  # /home/user/documents/file.txt

p = Path('/home/user/documents/file.txt')
print(p.name)        # 'file.txt'
print(p.stem)        # 'file'
print(p.suffix)      # '.txt'
print(p.parent)      # '/home/user/documents'


p = Path('example.txt')

# 존재 여부 확인
if p.exists():
    print("파일이 존재합니다.")

# 파일 생성 (빈 파일)
p.touch()

# 디렉토리 생성
d = Path('new_directory')
d.mkdir(exist_ok=True)  # 이미 존재해도 예외 발생 안 함

# 파일 삭제
p.unlink()  # 파일 삭제
d.rmdir()   # 빈 디렉토리 삭제
