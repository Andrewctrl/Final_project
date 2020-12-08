import Visting_mom_ending 
import Getting_help
def choice():
    print("You get dressed up quicky as you rush out to visit your mom in the hospital. " + "You visit your mom in the hospital, she is doing well. But you have a pile of bills. You get a job working at In-and-Out. Balancing work and school is hard, your grades are dropping.")
    answer = input("Do you quit school and work full time, or do you try to get help with school, therefore maintaining your job and school." + "Type \"Quit School\" to quit school, \"Get help\" to get help with school.") # question for dropping out or getting help with school
    if answer == "Quit School":
        Visting_mom_ending.final()
    if answer == "Get Help":
        Getting_help.got_help()