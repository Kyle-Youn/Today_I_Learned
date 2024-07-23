'''
pip install keyboard
'''

import keyboard
import time

# 'a' 키를 프로그래밍 방식으로 누르기
keyboard.press_and_release('a')

# 문자열 "hello"를 프로그래밍 방식으로 타이핑
keyboard.write('hello')

# Ctrl+C 를 프로그래밍 방식으로 타이핑
keyboard.press_and_release('ctrl+c')

# 'shift' 키를 0.5초 동안 누르고 있기
keyboard.press('shift')
time.sleep(0.5)
keyboard.release('shift')