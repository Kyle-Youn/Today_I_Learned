'''
# Readme
pip install pytube
video_url 변수에 유튜브 동영상 주소 복사해서 넣기!
save_path 변수에 Downloads폴더 경로 복사해서 넣기!
'''

'''
# notice
확인해보니 720p까지만 다운로드 되는 듯!
'''

from pytube import YouTube

def download_video(url, save_path):
    # YouTube 객체 생성
    yt = YouTube(url)

    # 가장 높은 해상도의 스트림 선택
    stream = yt.streams.get_highest_resolution()

    # 동영상 다운로드
    stream.download(save_path)

    print(f"Downloaded '{yt.title}' to {save_path}")

# 사용 예
video_url = 'https://www.youtube.com/watch?v=yAHGIigymtg'
save_path =  'C:/Users/hjyou/Downloads'
download_video(video_url, save_path)
