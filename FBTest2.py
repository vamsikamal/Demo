import pyautogui
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

usr= input('Enter Email Id:')
pwd= input('Enter Password:')


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password entered")

login_box = driver.find_element_by_name('login')
login_box.click()

#print ("Done")
#input('Press anything to quit')
#driver.quit()
#print("Finished")
#comment_box = driver.find_element_by_class_name('_1mf _1mj')
comment_box = driver.find_element_by_id('placeholder-c8bdr')


comments = ['hi','checking my python skills','How are you','Hope all good']

sleep(5)

for i in range(3):

    comment_box.send_keys(comments[i%7])
    pyautogui.typewrite('\n')
    sleep(2)