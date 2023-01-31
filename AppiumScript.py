from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "AndroidEmulator",
    "app": "C://Users//Stanislav//PycharmProjects//pythonProject//app//base.apk"
  }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

driver.implicitly_wait(5) #неявное ожидание 5 сек

driver.find_element(By.ID, '').click()

element = driver.find_element(By.ID, '')
element.clear()
element.send_keys('some text')

text = driver.find_element(By.ID, '').text

assert 'Text' in text, f'not found in {text}'
