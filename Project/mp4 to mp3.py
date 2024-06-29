'''
pip install moviepy
Have to download ffmpeg. https://doa-oh.tistory.com/170 참고하기!
'''
from moviepy.editor import *


# MP4 원본파일 경로
mp4_file = "C:/Users/hjyou/Downloads/1.mp4"  # 예: "/home/user/videos/video.mp4"

# MP3 파일이 저장될 경로와 파일 이름
mp3_file = "C:/Users/hjyou/Downloads/1.mp3"  # 원하는 경로로 변경

# 비디오 파일 불러오기
video = VideoFileClip(mp4_file)

# 오디오 추출 및 저장
video.audio.write_audiofile(mp3_file)

print("변환 완료:", mp3_file)
