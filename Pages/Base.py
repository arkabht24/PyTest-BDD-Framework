import os

from utils.Json_Reader_Loc import load_locators
from selenium.webdriver import ActionChains


class Base:
    def __init__(self,driver,loc_file_name):
        self.driver = driver
        locator_path = str(os.path.join(os.getcwd(),"locators",loc_file_name))
        print("Locator path ---> ",locator_path)
        self.locators = load_locators(locator_path)
    

    def click_element(self,element_key):
        try:
            self.driver.find_element(*self.locators[element_key]).click()
        except:
            action = ActionChains(self.driver) 
            action.click(self.driver.find_element(*self.locators[element_key])).perform()   
    

    def insert_text(self,element_key,text):
        element = self.driver.find_element(*self.locators[element_key])
        try:
            element.send_keys(text)
        except:
            self.driver.execute_script("arguments[0].value = arguments[1];",element,text)


    
    def verify_element_is_displayed(self, element_key):
        try:
            if self.driver.find_element(*self.locators[element_key]).is_displayed():
                print("Element is present in UI")
                return True
            else:
                print("Element is NOT present in UI but is hidden.")
                return False
        except:
            print("Element is NOT present in UI")
            return False
        


    def get_element_text(self,element_key):
        try:
            text = self.driver.find_element(*self.locators[element_key]).text
            print('Text from UI ---> ',text)
            return text
        
        except:
            print('No Text foind in UI ---> ')
            return ''
