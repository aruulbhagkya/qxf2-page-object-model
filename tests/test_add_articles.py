"""
This is an example automated test to help you learn Qxf2's framework
Our automated test will do the following:
    #Open Qxf2 newsletter generator application
    #Fill the details of add articles section.

"""
import os,sys,time
from turtle import title
from typing_extensions import runtime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.mail_conf as conf
import conf.adding_articles as conf
import pytest


@pytest.mark.GUI
def test_newsletter_page(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
        # Create a test object for add articles 
        test_obj = PageFactory.get_page_object("addarticles main page")
        #Set start_time with current time
        start_time = int(time.time())
        test_obj.turn_on_highlight()
        
        #Get the test details from the conf file
        email = conf.email
        password=conf.password
        
        #get the try again button
        try_button= test_obj.click_try_again()
        
        
        #get the sign button 
        sign_button=test_obj.click_sign_in()
        time.sleep(3)
        
        #set the email
        email_text = test_obj.set_email(email)
        test_obj.log_result(email_text,
                            positive="Email was successfully set to: %s\n"%email,
                            negative="Failed to set Email: %s \nOn url: %s\n"%(email,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        time.sleep(3)
        
        #click the next button
        nxt_button=test_obj.click_nxt_button()
        time.sleep(3)

        #set the password
        password_text = test_obj.set_password(password)
        test_obj.log_result(password_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        # click the next button
        nxt_button=test_obj.click_nxt_button()
        
        # click the hamburger button
        hamburger_button=test_obj.click_hamburger_button()
        
        # click the add_articles button
        add_button=test_obj.click_addarticle()
       
        #3.Get the test details from the conf file and fill the forms
        article_list = conf.article_list
        article_number = 1		#Initalize form counter  
        
        # Collect form data
        for article in article_list:
            url = article['URL']
            title = article['TITLE']
            description = article['DESCRIPTION']
            runtime = article['RUNTIME']
            category=article['CATEGORY']
            submit_button=test_obj.click_submit()
            add_another_article=test_obj.click_addanother_article()
           
            
            msg ="\nReady to fill article number %d"%article_number
            test_obj.write(msg)
           
            #  Visit main page again
            test_obj = PageFactory.get_page_object("addarticles main page")
            article_number = article_number + 1

         #a. Set and submit the article in one go
            result_flag = test_obj.submit_article(url,title,description,runtime,category)
            test_obj.log_result(result_flag,
                                positive="Successfully submitted the article number %d\n"%article_number,
                                negative="Failed to submit the article number %d \nOn url: %s"%(article_number,test_obj.get_current_url()),
                                level="critical")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
 
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__


#---START OF SCRIPT
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()

    #Run the test only if the options provided are valid
    if options_obj.check_options(options):
        test_obj = PageFactory.get_page_object("Zero",base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)

        #Setup TestRail reporting
        if options.testrail_flag.lower()=='y':
            if options.test_run_id is None:
                test_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                options.testrail_flag = 'N'
            if options.test_run_id is not None:
                test_obj.register_testrail()
                test_obj.set_test_run_id(options.test_run_id)

        if options.tesults_flag.lower()=='y':
            test_obj.register_tesults()

        test_newsletter_page(test_obj)

     #teardowm
        test_obj.wait(3)
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())
