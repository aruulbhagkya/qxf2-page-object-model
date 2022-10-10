"""
This class models the interviewscheduler_mainpage page.

"""
from .Base_Page import Base_Page
from .mail_object_page import Mail_Object_Page
from .edit_articles_object_page import Editarticles_Object_Page

class Editarticles_Mainpage(Base_Page, Mail_Object_Page, Editarticles_Object_Page):
    "Page Object for the weather shopper main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'manage-articles'
        self.open(url)
