import pyautogui
import time

# # 1. 화면 크기 출력
# print(pyautogui.size())

# # 2. 마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position())


# # 3. 마우스 이동
# pyautogui.moveTo(17,217)
# pyautogui.moveTo(17,217,1)

# # 4. 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval=1) # 1초마다 3번 클릭


# 5. 마우스 드래그
# 119,49 -> 265,51
pyautogui.moveTo(355,47,1)
pyautogui.dragTo(514,49,1)
pyautogui.dragTo(355,47,1)