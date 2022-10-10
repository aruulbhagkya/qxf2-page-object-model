import conf.add_articles_locators_conf as locators
class Addarticles_Object_Page:
    
    # get the hamburger locator
    hamburger=locators.hamburger
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
   
    def click_hamburger_button(self):
     hamburger_button=self.hover(self.hamburger)
     return hamburger_button    

    def click_home_button(self):
     home_button=self.click_element(self.home)
     return home_button

    def click_addarticle_button(self):
     add_button=self.click_element(self.add_articles)
     return add_button
    
    def set_url_button(self,url):
        result_flag = self.set_text(self.url,url)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%url,
            negative='Failed to set the url in the form',
            level='debug')        

    def set_title_button(self,title):
        result_flag = self.set_text(self.title,title)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%title,
            negative='Failed to set the url in the form',
            level='debug')

    def set_description_button(self,description):
        result_flag = self.set_text(self.description,description)
        self.conditional_write(result_flag,
            positive='Set the description to: %s'%description,
            negative='Failed to set the description in the form',
            level='debug')        
     
          
    
    def set_time_button(self,runtime):
        result_flag = self.set_text(self.time,runtime)
        self.conditional_write(result_flag,
            positive='Set the time to: %s'%runtime,
            negative='Failed to set the time in the form',
            level='debug')

    def set_category_button(self,category):
        result_flag = self.select_dropdown_option(self.category,category)
        self.conditional_write(result_flag,
            positive='Set the category to: %s'%category,
            negative='Failed to set the category in the form',
            level='debug')                
      
    # click the close button
    def click_article_button(self):
     submit_button=self.click_element(self.submit)
     return submit_button
            
    
                        