"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. weathershopper main page
2. moisturizer main page
3. sunscreen  main page
"""
 

from page_objects.zero_page import Zero_Page
from page_objects.newsletter_main_page import Newsletter_Mainpage
from page_objects.editarticles_main_page import Editarticles_Mainpage
from page_objects.deletearticles_main_page import Deletearticles_Mainpage
import conf.base_url_conf


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name in ["zero","zero page","agent zero"]:
            test_obj = Zero_Page(base_url=base_url)
        elif page_name == "newsletter main page":
            test_obj = Newsletter_Mainpage(base_url=base_url)  
        elif page_name == "editarticles main page":
            test_obj = Editarticles_Mainpage(base_url=base_url)  
        elif page_name == "deletearticles main page":
            test_obj = Deletearticles_Mainpage(base_url=base_url)             
        return test_obj

    get_page_object = staticmethod(get_page_object)