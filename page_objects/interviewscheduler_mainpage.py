"""
This class models the interviewscheduler_mainpage page.

"""
from .Base_Page import Base_Page
from .interviewscheduler_object_page import Interviewscheduler_Object_Page

class Interviewscheduler_Mainpage(Base_Page,Interviewscheduler_Object_Page):
    "Page Object for the weather shopper main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'jobs'
        self.open(url)
