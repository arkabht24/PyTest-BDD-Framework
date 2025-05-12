
from Pages.Base import Base


class Landing_Page(Base):
    
    def __init__(self,driver):
        loc_file_name = 'landing_page_loc.json'
        super().__init__(driver,loc_file_name)
    

    
    def verify_Buzz_is_displayed(self):
        return self.verify_element_is_displayed('BUZZ')

    
    def click_on_Buzz(self):
        self.click_element('BUZZ_CLICK')