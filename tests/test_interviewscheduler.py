"""
This is an example automated test to help you learn Qxf2's framework
Our automated test will do the following:
    #Open Qxf2 selenium-tutorial-main page.
    #Fill the example form.
    #Click on Click me! button and check if its working fine.
"""
import os,sys,time
from re import search
from tkinter.messagebox import OK
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
#from utils.Option_Parser import Option_Parser
import conf.interviewscheduler_conf as conf
#import conf.testrail_caseid_conf as testrail_file
import pytest


@pytest.mark.GUI
def test_interview_scheduler_page(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
        # Create a test object for moisturizer button
        test_obj = PageFactory.get_page_object("interviewscheduler main page")
        #Set start_time with current time
        start_time = int(time.time())
        #1.Get the test details from the conf file
        email = conf.email
        password=conf.password
        jobrole = conf.jobrole
        interviewers = conf.interviewers
        search = conf.search
        
        #2.get the login button
        button= test_obj.get_try_again()
        button=test_obj.get_sign_in()
        
        time.sleep(3)
        
        #3. set the email
        email_text = test_obj.set_email(email)
        test_obj.log_result(email_text,
                            positive="Email was successfully set to: %s\n"%email,
                            negative="Failed to set Email: %s \nOn url: %s\n"%(email,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #4. click the next button
        button=test_obj.get_nxt_button()
        time.sleep(3)

        #5.set the password
        password_text = test_obj.set_password(password)
        test_obj.log_result(password_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #6.click the next button 
        button=test_obj.get_nxt_button()

        #click delete button
        
        button=test_obj.get_jobs()
        time.sleep(2)
        search_text = test_obj.set_search_button(search)
        test_obj.log_result(search_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 

        # button=test_obj.get_delete_button()
        # button=test_obj.get_remove_button()
        # button=test_obj.get_close_button()
        
        #7.click hamburger menu,jobs,add button 
        # button= test_obj.get_hamburger_menu()
        button= test_obj.get_delete_button()
        button= test_obj.get_remove_button()
        button=test_obj.get_close_button()
        #button=test_obj.get_jobs()
        button=test_obj.get_add_button()

        #8.set the job role
        job_role_text = test_obj.set_job_role(jobrole)
        test_obj.log_result(job_role_text,
                            positive="Passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #9. set the interviewers
        interviewers_text = test_obj.set_interviewers(interviewers)
        test_obj.log_result(interviewers_text,
                            positive="Passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #10. click the submit button
        button= test_obj.get_submit_button()
        test_obj.switch_page(OK).accept()
        
        #11. Print out the result
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

        test_interview_scheduler_page(test_obj)

     #teardowm
        test_obj.wait(3)
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        #print(option_obj.print_usage())
