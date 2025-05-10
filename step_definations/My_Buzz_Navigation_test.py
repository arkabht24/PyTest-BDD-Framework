


from pytest_bdd import given, scenarios
from pytest_bdd import parsers

from Pages.Login_page import Login_Page
from utils.Dot_Env_Reader import BASE_URL

scenarios('/Users/arkabhattacharyya/Desktop/PytestBDD/PyTest BDD/features/My Buzz Navigation.feature')


@given(parsers.parse('user enters "{username}" and "{password}" and clicks on login button'))
def login(username,password,driver):
    print(username+" "+password+" ")
    driver.get(BASE_URL)
    login_page = Login_Page(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_on_login_button()