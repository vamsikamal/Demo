import pyautogui
import time
import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
url = 'https://facebook.com'
webbrowser.get(chrome_path).open(url)

groups=['347600576442111','934147667109661','763466607836290']

print("Click on browser")
time.sleep(10)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in range(len(groups)):
    link = 'https://www.facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')

    print('Waiting for 45 seconds\n')
    time.sleep(60)

    pyautogui.typewrite('p')
    time.sleep(5)
    print('Writting  post\n')
    pyautogui.typewrite('Hello All, I have created the new group for my program testing purpose')
    time.sleep(10)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

    time.sleep(10)

    pyautogui.write(['f6'])
    time.sleep(1)