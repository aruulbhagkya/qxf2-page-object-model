"""
This is an example automated test to help you learn Qxf2's framework
Our automated test will do the following:
    #Open Qxf2 interview scheduler application
    #Fill the details of jobs section.

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

        # Turn on the highlighting feature
        test_obj.turn_on_highlight()
        
        #1.Get the test details from the conf file
        email = conf.email
        password=conf.password
        jobrole = conf.jobrole
        interviewers = conf.interviewers
        search = conf.search
        
        #2.get the login button
        try_again_button= test_obj.click_try_again()
        sign_in_button=test_obj.click_sign_in()
        
        time.sleep(3)
        
        #3. set the email
        email_text = test_obj.set_email(email)
        test_obj.log_result(email_text,
                            positive="Email was successfully set to: %s\n"%email,
                            negative="Failed to set Email: %s \nOn url: %s\n"%(email,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #4. click the next button
        button=test_obj.click_nxt_button()
        time.sleep(3)

        #5.set the password
        password_text = test_obj.set_password(password)
        test_obj.log_result(password_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #6.click the next button 
        next_button=test_obj.click_nxt_button()

        #7.click jobs 
        jobs_button=test_obj.click_jobs_button()
        time.sleep(2)
        
        #8.set search input box
        search_text = test_obj.set_search_button(search)
        test_obj.log_result(search_text,
                            positive="passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 

        #9.click delete button
        delete_button= test_obj.click_delete_button()
       
        #10.click remove button
        remove_button= test_obj.click_remove_button()
       
        #11.click close button
        close_button=test_obj.click_close_button()
       
        #12.click add button
        add_button=test_obj.click_add_button()

        #13.set the job role
        job_role_text = test_obj.set_job_role(jobrole)
        test_obj.log_result(job_role_text,
                            positive="Passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #14. set the interviewers
        interviewers_text = test_obj.set_interviewers(interviewers)
        test_obj.log_result(interviewers_text,
                            positive="Passed\n" ,
                            negative="Failed\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #15. click the submit button
        submit_button= test_obj.click_submit_button()
       
        #16.Accept ok button
        ok_button=test_obj.ok_button()
        ok_button.accept()        
       
        #17. Print out the result
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
