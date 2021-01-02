#Choose your own Adventure
#from PIL import Image
import alpha, beta
#starting_Image = Image.open("Starting_room.png")
#starting_Image.show()
print ("It is December of 2018. You wake up to a chilly Saturday morning. As the musty smell of rented textbooks infiltrates your nose, you recall your horrible performance on yesterday’s algebra exam. In the sub 50 degrees SF morning weather, you’re shivering under your blankets. You scramble out of bed and prepare a breakfast of instant noodles and a carton of milk you saved from yesterday’s school lunch. Your mom has left you a text asking you to come to visit her in the hospital today and take over her ice cream cart. ")
answer = input("Do you stay at home to study for your test on Monday and risk being evicted from your home the next month, or do you help your mother in a last-ditch effort to avoid being homeless? Yes for studying and No for helping your mother ")
if answer == "Yes":
    alpha.chose_yes()
if answer == "No": # visting mom
    beta.chose_no() 



