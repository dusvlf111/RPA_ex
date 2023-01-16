import pyautogui 

pyautogui.sleep(3)

# print(pyautogui.position())

# pyautogui.click(64, 17, duration=1) # 1초 동안 64,17 좌표로 이동 후 마우스 클릭

# pyautogui.mouseUp() # 마우스 때기
# pyautogui.mouseDown() # 마우스 클릭 옮길때 사용함

# pyautogui.doubleClick() # 더블 클릭함
# pyautogui.click(clicks=500) # 짧은 시간에 클릭 500번

# pyautogui.moveTo(100, 100)
# pyautogui.mouseDown() # 마우스를 누른상태
# pyautogui.mouseTo(300,300)
# pyautogui.mouseUp()   # 마우스를 뗀상태

# pyautogui.rightClick()
# pyautogui.middleClick()

pyautogui.moveTo(1114, 349)

pyautogui.drag(100, 500, duration= 0.25) # 현재 위치 기준으로 x 100만큼 y 0 만큼 드래그
# 동작이 빨라 수행이 안될때는 duration 값 넣어주기
pyautogui.dragTo()
# 절대좌표 



