"""
This class models the interviewscheduler_mainpage page.

"""
from .Base_Page import Base_Page
from .mail_object_page import Mail_Object_Page
from .add_articles_object_page import Addarticles_Object_Page

class Newsletter_Mainpage(Base_Page, Mail_Object_Page, Addarticles_Object_Page):
    "Page Object for the weather shopper main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'articles'
        self.open(url)
