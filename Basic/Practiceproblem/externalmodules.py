import pyautogui
import  time
# pyautogui.alert(text='hi', title='bye', button='OK')
# im1 = pyautogui.screenshot()
time.sleep(2)

for i in range(1,5):
    time.sleep(2)
    pyautogui.write('I love phirtron!',interval=0.25)

    pyautogui.press('enter')

