import pyautogui
import pyperclip

# 1. 키보드 입력 (문자)
# pyautogui.write('Mocha',interval=0.1)

# 2. 키보드 입력 (키)
# pyautogui.press('enter')
# pyautogui.press('up')

# 3. 키보드 입력 (여러개 동시에)
# pyautogui.hotkey('ctrl', 'c') # mac = 'command', 'c'

# 4. 한글 입력 방법
pyperclip.copy('한글 입력')
pyautogui.hotkey('ctrl', 'v')


