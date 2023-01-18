from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

list = []

def launchBrowser():
    options = Options()
    options.headless = True
    options.add_argument('log-level=3')
    options.add_argument("--window-size=1920,1200")
    DRIVER_PATH = './chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
    driver.get('https://my.brain.fm/focus')
    time.sleep(5)
    return driver

def signIn(driver):
    emailInput = driver.find_element(By.ID, 'email')
    emailInput.send_keys('horamak536@nevyxus.com')
    passwordInput = driver.find_element(By.ID, 'password')
    passwordInput.send_keys('horamak536@nevyxus.com')

    signInButton = driver.find_element(By.XPATH, '//button[@type="submit"]')
    signInButton.click()
    time.sleep(7)

def closePopup(driver):
    popup = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/button')
    popup.click()
    time.sleep(5)

def openFocusPage(driver):
    focus = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div')
    focus.click()
    time.sleep(5)
    
def downloadAudio(driver):
    audioLinks = driver.find_elements(By.TAG_NAME, 'audio') # getting all audio links
    time.sleep(10)
    
    if (len(list) == 0):
        for link in audioLinks:
            list.append(link.get_attribute('src'))
            time.sleep(7)
    
    #checking the link already
    for link in audioLinks:
        if ((link.get_attribute('src') in list)&(len(list) > 1)):
            print(list)
        else:
            if (len(list) > 0):
                print('entering')
                for link in audioLinks:
                    list.append(link.get_attribute('src'))
                    time.sleep(5)
            skip = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/button[3]/div')
            skip.click()
            time.sleep(5)
            print(list)
            downloadAudio(driver)
            
driverAPI = launchBrowser()
signIn(driverAPI)
closePopup(driverAPI)
openFocusPage(driverAPI)
downloadAudio(driverAPI)
