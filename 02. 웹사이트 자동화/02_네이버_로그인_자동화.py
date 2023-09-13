from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyperclip
import pyautogui


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# import pyperclip
# import pyautogui
# # 크롬 드라이버 자동 업데이트
# from webdriver_manager.chrome import ChromeDriverManager


# # 브라우저 꺼짐 방지 옵션
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)



# 웹페이지 해당 주소 이동
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
driver.maximize_window() # 화면 최대화

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR,"#id")
#id.send_keys("komin126")
id.click()
pyperclip.copy('komin126')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR,"#pw")
#pw.send_keys("12345678")
pw.click()
pyperclip.copy('12345678')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼
driver.find_element(By.CSS_SELECTOR,"#log\.login").click()
