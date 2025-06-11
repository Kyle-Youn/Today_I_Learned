from pathlib import Path

example_dir = Path("my_directory_path")
for obj in example_dir.rglob('*'):
  print(obj)    # 모든 파일과 디렉토리 반환
