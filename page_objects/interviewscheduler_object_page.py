import conf.interviewscheduler_locators_conf as locators
class Interviewscheduler_Object_Page:
    "Page Object for the interview scheduler main page"
    # get the try_again locator
    try_again=locators.try_again
    # get the sign_in locator
    sign_in=locators.sign_in
     # get the hamburger_menu locator
    hamburger_menu= locators.hamburger_menu
    # get the jobs locator
    jobs=locators.jobs
    # get the add_button locator
    add_button=locators.add_button
    # get the job_role locator
    job_role=locators.job_role
    # get the interviewers locator
    interviewers= locators.interviewers
    # get the submit_button locator
    submit_button=locators.submit_button
    # set the mail locator
    setting_mail=locators.setting_mail
    # set password locator
    password=locators.password
    # get nxt button locator
    nxt_button=locators.nxt_button
    # get the delete_button locator
    # get the search_button locator
    search_button=locators.search_button

    delete_button=locators.delete_button
    # get the remove_button locator
    remove_button=locators.remove_button
    close_button=locators.close_button
    
    # click the try again button
    def get_try_again(self):
     Button=self.click_element(self.try_again)
     return Button

    #click the sign in button
    def get_sign_in(self):
     Button=self.click_element(self.sign_in)
     return Button
    
    # set the email 
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.setting_mail,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')
   
    #click the next button
    def get_nxt_button(self):
     Button=self.click_element(self.nxt_button)
     return Button 
    def set_password(self,password):
        result_flag = self.set_text(self.password,password)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%password,
            negative='Failed to set the email in the form',
            level='debug')

    def set_search_button(self,search):
        result_flag = self.set_text(self.search_button,search)
        self.conditional_write(result_flag,
            positive='Set the jobrole to: %s'%search,
            negative='Failed to set the jobrole in the form',
            level='debug')
     

    def get_delete_button(self):
     Button=self.click_element(self.delete_button)
     return Button

    def get_remove_button(self):
     Button=self.click_element(self.remove_button)
     return Button

    def get_close_button(self):
     Button=self.click_element(self.close_button)
     return Button
    
    
    # click the hamburger menu 
    # def get_hamburger_menu(self):
    #  Button=self.click_element(self.hamburger_menu)
    #  return Button
    
    # click the jobs button
    def get_jobs(self):
     Button=self.click_element(self.jobs)
     return Button 

    # click the add button 
    def get_add_button(self):
     Button=self.click_element(self.add_button)
     return Button     

    # set the job role     
    def set_job_role(self,jobrole):
        result_flag = self.set_text(self.job_role,jobrole)
        self.conditional_write(result_flag,
            positive='Set the jobrole to: %s'%jobrole,
            negative='Failed to set the jobrole in the form',
            level='debug')
    
    # set the interviewers
    def set_interviewers(self,interviewers):
        result_flag = self.set_text(self.interviewers,interviewers)
        self.conditional_write(result_flag,
            positive='Set the interviewers to: %s'%interviewers,
            negative='Failed to set the interviewers in the form',
            level='debug')
    
    #click submit button 
    def get_submit_button(self):
     Button=self.click_element(self.submit_button)
     return Button  


     
 
    


