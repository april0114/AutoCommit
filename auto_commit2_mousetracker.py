import pyautogui
import time

print("좌표 추적을 시작합니다. 마우스를 원하는 위치로 이동시키세요. 종료하려면 Ctrl + C를 누르세요.")

try:
    while True:
        x, y = pyautogui.position()  # 현재 마우스 좌표 가져오기
        print(f"현재 마우스 좌표: ({x}, {y})", end='\r')  
        time.sleep(0.1)  
except KeyboardInterrupt:
    print("\n좌표 추적을 종료합니다.")