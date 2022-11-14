import pyautogui

import time

pyautogui.alert('O código vai começar. Não user nada do seu computador enquanto o código está rodando')

pyautogui.PAUSE = 0.5

pyautogui.press('winleft')

pyautogui.write('chrome')

pyautogui.press('enter')

time.sleep(1)

pyautogui.write('https://drive.google.com/drive/u/1/folders/1hPq9EPXPwW-2cJ9duwC3R9PQ-LOZOhYh')

pyautogui.press('enter')

pyautogui.hotkey('winleft', 'd')

pyautogui.position()

pyautogui.moveTo(136, 421)

pyautogui.mouseDown()

#abrindo o google drive, aondes de soltar o arquivo
pyautogui.moveTo(1026, 536)

pyautogui.hotkey('alt', 'tab')
time.sleep(1)

pyautogui.mouseUp()

time.sleep(5)

pyautogui.alert('O código está finalizado.')