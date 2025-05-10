import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

def get_driver(browser = 'chrome'):
    if browser.lower() == 'chrome':
        driver_path = os.path.join('drivers','chromedriver') 
        option = ChromeOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--disable-extensions")

        driver = webdriver.Chrome(service=ChromeService(driver_path),options=option)
        driver.implicitly_wait(10) 
    
    elif browser.lower() == 'firefox':
        geckodriver_path = os.path.join(os.getcwd(), 'drivers', 'geckodriver')
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized") 
        driver = webdriver.Firefox(service=FirefoxService(geckodriver_path), options=firefox_options)
        driver.implicitly_wait(10) 

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver
        

