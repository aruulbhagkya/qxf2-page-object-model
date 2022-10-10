import conf.mail_locators_conf as locators
class Mail_Object_Page:
    "Page Object for the interview scheduler main page"
    # get the try_again locator
    try_again=locators.try_again
    # get the sign_in locator
    sign_in=locators.sign_in
    # set the mail locator
    setting_mail=locators.setting_mail
    # set password locator
    password=locators.password
    # get nxt button locator
    nxt_button=locators.nxt_button
    
    # click the try again button
    def click_try_again(self):
     try_again_button=self.click_element(self.try_again)
     return try_again_button

    #click the sign in button
    def click_sign_in(self):
     sign_in_button=self.click_element(self.sign_in)
     return sign_in_button
    
    # set the email 
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.setting_mail,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')
   
    #click the next button
    def click_nxt_button(self):
     Button=self.click_element(self.nxt_button)
     return Button 
    
    # set the password
    def set_password(self,password):
        result_flag = self.set_text(self.password,password)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%password,
            negative='Failed to set the email in the form',
            level='debug')

    