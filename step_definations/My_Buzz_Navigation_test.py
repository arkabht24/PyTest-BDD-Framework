


import time
from pytest_bdd import given, scenarios, then, when
from pytest_bdd import parsers

from Pages.Buzz_page import Buzz_Page
from Pages.Landing_page import Landing_Page
from Pages.Login_page import Login_Page
from utils.Dot_Env_Reader import BASE_URL

scenarios('/Users/arkabhattacharyya/Desktop/PytestBDD/PyTest BDD/features/My Buzz Navigation.feature')

check = False

@given(parsers.parse('user enters "{username}" and "{password}" and clicks on login button'))
def login(username,password,driver):
    print(username+" "+password+" ")
    driver.get(BASE_URL)
    login_page = Login_Page(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_on_login_button()


@when('Verify Buzz is displayed or not')
def verify_Buzz_is_present(driver):
    global check
    landing_page = Landing_Page(driver)
    check = landing_page.verify_Buzz_is_displayed()
    print(f"check is {check}")
    assert check
    


@when('I will navigate to the Buzz section')
def navigate_to_Buzz(driver):
    print(f"check is {check}")
    if check == True:
        landing_page = Landing_Page(driver)
        print('Proceeding to click on Buzz')
        landing_page.click_on_Buzz()
    print('Clicked on Buzz')



@then(parsers.parse('I will validate the Page header "{pageHeader}"'))
def validate_page_header(pageHeader,driver):
    buzz_page = Buzz_Page(driver)
    assert buzz_page.verify_header_is_displayed() and buzz_page.get_header_text()==pageHeader
