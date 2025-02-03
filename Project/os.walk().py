# os.walk() 함수: 디렉터리 트리를 순회(traverse)하며 하위 디렉터리와 파일 목록을 재귀적으로 가져오는 데 사용되는 파이썬의 함수

import os

for root, dirs, files in os.walk(path, topdown=True):
  # root: 현재 탐색 중인 디렉터리 경로
  # dirs: 현재 디렉터리 안의 하위 디렉터리 목록
  # files: 현재 디렉터리 안의 파일 목록
  print(f"현재 디렉터리: {root}")
  print(f"하위 디렉터리: {dirs}")
  print(f"파일: {files}")
