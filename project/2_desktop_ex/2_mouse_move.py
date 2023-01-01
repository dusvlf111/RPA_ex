import pyautogui

#pyautogui.moveTo(200,100) # 지정한 위치 가로 세로로 마우스 이동
pyautogui.moveTo(500,200, duration=5) # 지정한 위치 가로 세로로 5초 마우스 이동


pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveTo(200, 200, duration=0.25) # 100
pyautogui.moveTo(300, 300, duration=0.25) # 100

pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.move(100, 100, duration=0.25) # 100, 100 기준으로 +100 +100