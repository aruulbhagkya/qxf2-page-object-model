"""
This class models the interviewscheduler_mainpage page.

"""
from .Base_Page import Base_Page
from .mail_object_page import Mail_Object_Page
from .manage_articles_object_page import Managearticles_Object_Page
from .hamburger_object_page import Hamburger_Object_Page

class Managearticles_Mainpage(Base_Page, Mail_Object_Page, Hamburger_Object_Page, Managearticles_Object_Page):
    "Page Object for the weather shopper main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'manage-articles'
        self.open(url)
