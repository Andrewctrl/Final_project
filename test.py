#Choose your own Adventure

game_start = "yes"

while game_start == "yes":
    print ("You wake up to a chilly Saturday morning shivering in your blankets, the alarm starts ringing. Do you get out of bed or stay?")
    answer_1 = input("Yes or No? ")
    
    if answer_1 == "yes":
        print("You get out of bed and prepare a breakfast of instant noodles with the carton of milk you saved from yesterday’s school lunch, you also get a text from mother do you look?")
    else:
        print("You continue to sleep and drift off into your dreams")
        #while  == "yes":
            #print("Hello, Son/Daughter I hoped you enjoyed your breakfeast do you mind visiting me at the hospitial and taking over the ice cream cart business for today, do you go and take over or not?")
            #answer_2 = input("Yes or No?")
        
            #if answer_2 == "yes":
                #print("Sure, mom I'll see if can come by today and take over the business")
            #else:
                #print("You ignore the text that your mom has sent, and spend the rest of the morning studying for Monday’s test and playing on your phone.")
    
    game_start = input("Would you like to start over?")
