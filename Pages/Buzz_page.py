
from Pages.Base import Base


class Buzz_Page(Base):
    def __init__(self,driver):
        loc_file_name = 'buzz_page_loc.json'
        super().__init__(driver,loc_file_name)


    def verify_header_is_displayed(self):
        return self.verify_element_is_displayed('BUZZ_HEADER')
    
    def get_header_text(self):
        return self.get_element_text('BUZZ_HEADER')