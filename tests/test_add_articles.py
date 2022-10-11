"""
This is an example automated test to help you learn Qxf2's framework
Our automated test will do the following:
    #Open Qxf2 interview scheduler application
    #Fill the details of jobs section.

"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.mail_conf as conf
import conf.add_articles_conf as conf
import pytest


@pytest.mark.GUI
def test_newsletter_page(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
        # Create a test object for moisturizer button
        test_obj = PageFactory.get_page_object("addarticles main page")
        #Set start_time with current time
        start_time = int(time.time())
        test_obj.turn_on_highlight()
        
        #Get the test details from the conf file
        email = conf.email
        password=conf.password
        url_1=conf.url_1
        title_1 = conf.title_1
        description_1 = conf.description_1
        run_1=conf.runtime_1
        category_1=conf.category_1
        url_2=conf.url_2
        title_2 = conf.title_2
        description_2 = conf.description_2
        run_2=conf.runtime_2
        category_2=conf.category_2
        url_3=conf.url_3
        title_3 = conf.title_3
        description_3 = conf.description_3
        run_3=conf.runtime_3
        category_3=conf.category_3
        url_4=conf.url_4
        title_4 = conf.title_4
        description_4 = conf.description_4
        run_4=conf.runtime_4
        category_4=conf.category_4
        url_5=conf.url_5
        title_5= conf.title_5
        description_5 = conf.description_5
        run_5=conf.runtime_5
        category_5=conf.category_5
        
        #get the try again button
        try_button= test_obj.click_try_again()
        # time.sleep(3)
        
        #get the sign button 
        sign_button=test_obj.click_sign_in()
        # time.sleep(3)
        
        #set the email
        email_text = test_obj.set_email(email)
        test_obj.log_result(email_text,
                            positive="Email was successfully set to: %s\n"%email,
                            negative="Failed to set Email: %s \nOn url: %s\n"%(email,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
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
        add_button=test_obj.click_addarticle_button()
        
        
        # set the url_text button
        url_text = test_obj.set_url_button(url_1)
        test_obj.log_result(url_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))     
        
        # set the title_text button
        title_text = test_obj.set_title_button(title_1)
        test_obj.log_result(title_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 
         
        # set the description_text button
        description_text = test_obj.set_description_button(description_1)
        test_obj.log_result(description_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
         
        # set the time button
        time_text = test_obj.set_time_button(run_1)
        test_obj.log_result(time_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        # set the category button  
        category_text = test_obj.set_category_button(category_1)
        test_obj.log_result(category_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 

        # click submit button  
        submit_button=test_obj.click_article_button()

        # click add another article button
        add_another_article=test_obj.click_addanother_article_button()

         # set the url_text button
        url_text = test_obj.set_url_button(url_2)
        test_obj.log_result(url_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))     
        
        # set the title_text button
        title_text = test_obj.set_title_button(title_2)
        test_obj.log_result(title_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 
         
        # set the description_text button
        description_text = test_obj.set_description_button(description_2)
        test_obj.log_result(description_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
         
        # set the time button
        time_text = test_obj.set_time_button(run_2)
        test_obj.log_result(time_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        # set the category button  
        category_text = test_obj.set_category_button(category_2)
        test_obj.log_result(category_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 

        # click submit button  
        submit_button=test_obj.click_article_button()

        # click add another article button
        add_another_article=test_obj.click_addanother_article_button()

         # set the url_text button
        url_text = test_obj.set_url_button(url_3)
        test_obj.log_result(url_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))     
        
        # set the title_text button
        title_text = test_obj.set_title_button(title_3)
        test_obj.log_result(title_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 
         
        # set the description_text button
        description_text = test_obj.set_description_button(description_3)
        test_obj.log_result(description_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
         
        # set the time button
        time_text = test_obj.set_time_button(run_3)
        test_obj.log_result(time_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        # set the category button  
        category_text = test_obj.set_category_button(category_3)
        test_obj.log_result(category_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 

        # click submit button  
        submit_button=test_obj.click_article_button()

        # click add another article button
        add_another_article=test_obj.click_addanother_article_button()

         # set the url_text button
        url_text = test_obj.set_url_button(url_4)
        test_obj.log_result(url_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))     
        
        # set the title_text button
        title_text = test_obj.set_title_button(title_4)
        test_obj.log_result(title_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 
         
        # set the description_text button
        description_text = test_obj.set_description_button(description_4)
        test_obj.log_result(description_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
         
        # set the time button
        time_text = test_obj.set_time_button(run_4)
        test_obj.log_result(time_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        # set the category button  
        category_text = test_obj.set_category_button(category_4)
        test_obj.log_result(category_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 

        # click submit button  
        submit_button=test_obj.click_article_button()

        # click add another article button
        add_another_article=test_obj.click_addanother_article_button()

         # set the url_text button
        url_text = test_obj.set_url_button(url_5)
        test_obj.log_result(url_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))     
        
        # set the title_text button
        title_text = test_obj.set_title_button(title_5)
        test_obj.log_result(title_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 
         
        # set the description_text button
        description_text = test_obj.set_description_button(description_5)
        test_obj.log_result(description_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
         
        # set the time button
        time_text = test_obj.set_time_button(run_5)
        test_obj.log_result(time_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        # set the category button  
        category_text = test_obj.set_category_button(category_5)
        test_obj.log_result(category_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 

        # click submit button  
        submit_button=test_obj.click_article_button()

        # Print out the result
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
        #print(option_obj.print_usage())
