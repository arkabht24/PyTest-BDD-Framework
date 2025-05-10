


from Pages.Base import Base


class Login_Page(Base):
    def __init__(self,driver):
        loc_file_name = 'login_page_loc.json'
        super().__init__(driver,loc_file_name)


    def enter_username(self,username):
        self.insert_text("USERNAME_INPUT",username)


    def enter_password(self,password):
        self.insert_text("PASSWORD_INPUT",password)


    def click_on_login_button(self):
        self.click_element("LOGIN_BUTTON")