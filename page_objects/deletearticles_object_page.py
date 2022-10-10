

import conf.delete_articles_locators as locators
class Deletearticles_Object_Page:
    
    # get the hamburger locator
    hamburger=locators.hamburger
    # get the manage articles locator
    manage_article=locators.manage_article
    # get the search locator
    search =locators.search
    # get the delete locator
    delete =locators.delete
    
    def click_hamburger_button(self):
     hamburger_button=self.hover(self.hamburger)
     return hamburger_button    

    def click_managearticle_button(self):
     manage_button=self.click_element(self.manage_article)
     return manage_button

    def set_search_button(self,search):
        result_flag = self.set_text(self.search,search)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%search,
            negative='Failed to set the url in the form',
            level='debug')

    
    def click_delete_button(self):
     add_button=self.click_element(self.delete)
     return add_button 

    def ok_button(self,OK):
     ok_button=self.switch_page(self.OK,OK)   
     return ok_button 

            
     