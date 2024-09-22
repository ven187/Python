import pyperclip
import pyautogui
import time

def write_safe(text):
    text = text.replace('@', '@')  
    pyperclip.copy(text)  
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')  

write_safe("hello@world")
