'''
pip install pycaw
'''

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

def set_volume(level):
    # 오디오 디바이스를 초기화합니다.
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # 볼륨을 설정합니다 (-65.25은 최소 볼륨, 0.0은 최대 볼륨입니다).
    # 예를 들어, level이 0.5라면 중간 볼륨으로 설정합니다.
    volume.SetMasterVolumeLevelScalar(level, None)

if __name__ == "__main__":
    # 사용자로부터 볼륨 레벨을 입력받습니다 (0.0 ~ 1.0 사이).
    level = float(input("볼륨 레벨을 입력하세요 (0.0 최소, 1.0 최대): "))
    set_volume(level)
    print(f"볼륨이 {level * 100}%로 설정되었습니다.")