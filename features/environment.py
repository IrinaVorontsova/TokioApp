from appium import webdriver

def before_scenario(context, scenario):
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "AndroidEmulator",
        "app": "C://Users//Stanislav//PycharmProjects//pythonProject//app//base.apk"
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

    driver.implicitly_wait(5)


def after_scenario(context, scenario):
    context.driver.quit()
