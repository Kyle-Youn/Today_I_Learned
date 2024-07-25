'''
pip install keyboard
'''

import keyboard
import time

key_to_monitor = 'a'  # 감지하고 싶은 키
count_duration = 1.0  # 지속 시간 (초)
start_time = None
key_press_count = 0

def on_key_event(event):
    global key_press_count, start_time
    if event.event_type == 'down' and event.name == key_to_monitor:
        current_time = time.time()
        if start_time is None:
            start_time = current_time  # 최초 키 누름 시간을 기록
        elif current_time - start_time < count_duration:
            key_press_count += 1
        else:
            print(f"{key_to_monitor} key was pressed {key_press_count} times in 1 second.")
            keyboard.unhook_all()
            return
        print(f"{key_to_monitor} key pressed {key_press_count} times.")

keyboard.hook(on_key_event)
keyboard.wait()
