import conf.add_articles_locators_conf as locators
class Addarticles_Object_Page:
    # get home button locator
    home=locators.home
    # get the add articles locator
    add_articles=locators.add_articles
    # get the url  locator
    url=locators.url
    # get the title locator
    title=locators.title
    # get the description locator
    description=locators.description
    # get the time locator
    time =locators.time 
    # get the category locator
    category =locators.category
    # get the add_article locator
    submit =locators.submit
    # get the add_another_article locator 
    add_another_articles=locators.add_another_articles
   
    def click_home_button(self):
     home_button=self.click_element(self.home)
     return home_button

    def click_addarticle_button(self):
     add_button=self.click_element(self.add_articles)
     return add_button
    
    def set_url_button(self,url_1):
        result_flag = self.set_text(self.url,url_1)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%url_1,
            negative='Failed to set the url in the form',
            level='debug')      
    def set_url_button(self,url_2):
        result_flag = self.set_text(self.url,url_2)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%url_2,
            negative='Failed to set the url in the form',
            level='debug')                

    def set_url_button(self,url_3):
        result_flag = self.set_text(self.url,url_3)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%url_3,
            negative='Failed to set the url in the form',
            level='debug')       
    
    def set_url_button(self,url_4):
        result_flag = self.set_text(self.url,url_4)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%url_4,
            negative='Failed to set the url in the form',
            level='debug')      

    def set_url_button(self,url_5):
        result_flag = self.set_text(self.url,url_5)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%url_5,
            negative='Failed to set the url in the form',
            level='debug')              
    
    def set_title_button(self,title_1):
        result_flag = self.set_text(self.title,title_1)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%title_1,
            negative='Failed to set the url in the form',
            level='debug')

    def set_title_button(self,title_2):
        result_flag = self.set_text(self.title,title_2)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%title_2,
            negative='Failed to set the url in the form',
            level='debug')

    def set_title_button(self,title_3):
        result_flag = self.set_text(self.title,title_3)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%title_3,
            negative='Failed to set the url in the form',
            level='debug')        

    def set_title_button(self,title_4):
        result_flag = self.set_text(self.title,title_4)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%title_4,
            negative='Failed to set the url in the form',
            level='debug')

    def set_title_button(self,title_5):
        result_flag = self.set_text(self.title,title_5)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%title_5,
            negative='Failed to set the url in the form',
            level='debug')

    def set_description_button(self,description_1):
        result_flag = self.set_text(self.description,description_1)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%description_1,
            negative='Failed to set the url in the form',
            level='debug') 

    def set_description_button(self,description_2):
        result_flag = self.set_text(self.description,description_2)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%description_2,
            negative='Failed to set the url in the form',
            level='debug')       

    def set_description_button(self,description_3):
        result_flag = self.set_text(self.description,description_3)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%description_3,
            negative='Failed to set the url in the form',
            level='debug') 

    def set_description_button(self,description_4):
        result_flag = self.set_text(self.description,description_4)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%description_4,
            negative='Failed to set the url in the form',
            level='debug')                                                    

    def set_description_button(self,description_5):
        result_flag = self.set_text(self.description,description_5)
        self.conditional_write(result_flag,
            positive='Set the description to: %s'%description_5,
            negative='Failed to set the description in the form',
            level='debug')        
     
    def set_time_button(self,runtime_1):
        result_flag = self.set_text(self.time,runtime_1)
        self.conditional_write(result_flag,
            positive='Set the time to: %s'%runtime_1,
            negative='Failed to set the time in the form',
            level='debug')

    def set_time_button(self,runtime_2):
        result_flag = self.set_text(self.time,runtime_2)
        self.conditional_write(result_flag,
            positive='Set the time to: %s'%runtime_2,
            negative='Failed to set the time in the form',
            level='debug')

    def set_time_button(self,runtime_3):
        result_flag = self.set_text(self.time,runtime_3)
        self.conditional_write(result_flag,
            positive='Set the time to: %s'%runtime_3,
            negative='Failed to set the time in the form',
            level='debug')

    def set_time_button(self,runtime_4):
        result_flag = self.set_text(self.time,runtime_4)
        self.conditional_write(result_flag,
            positive='Set the time to: %s'%runtime_4,
            negative='Failed to set the time in the form',
            level='debug')

    def set_time_button(self,runtime_5):
        result_flag = self.set_text(self.time,runtime_5)
        self.conditional_write(result_flag,
            positive='Set the time to: %s'%runtime_5,
            negative='Failed to set the time in the form',
            level='debug')                                

    def set_category_button(self,category_1):
        result_flag = self.select_dropdown_option(self.category,category_1)
        self.conditional_write(result_flag,
            positive='Set the category to: %s'%category_1,
            negative='Failed to set the category in the form',
            level='debug') 

    def set_category_button(self,category_2):
        result_flag = self.select_dropdown_option(self.category,category_2)
        self.conditional_write(result_flag,
            positive='Set the category to: %s'%category_2,
            negative='Failed to set the category in the form',
            level='debug') 

    def set_category_button(self,category_3):
        result_flag = self.select_dropdown_option(self.category,category_3)
        self.conditional_write(result_flag,
            positive='Set the category to: %s'%category_3,
            negative='Failed to set the category in the form',
            level='debug') 

    def set_category_button(self,category_4):
        result_flag = self.select_dropdown_option(self.category,category_4)
        self.conditional_write(result_flag,
            positive='Set the category to: %s'%category_4,
            negative='Failed to set the category in the form',
            level='debug') 

    def set_category_button(self,category_5):
        result_flag = self.select_dropdown_option(self.category,category_5)
        self.conditional_write(result_flag,
            positive='Set the category to: %s'%category_5,
            negative='Failed to set the category in the form',
            level='debug') 

                                                           
    # click the close button
    def click_article_button(self):
     submit_button=self.click_element(self.submit)
     return submit_button
            
    def click_addanother_article_button(self):
     add_another_article_button=self.click_element(self.add_another_articles)
     return add_another_article_button
                        