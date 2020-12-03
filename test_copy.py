#Choose your own Adventure
from PIL import Image

print ("It is December of 2018. You wake up to a chilly Saturday morning. As the musty smell of rented textbooks infiltrates your nose, you recall your horrible performance on yesterday’s algebra exam. In the sub 50 degrees SF morning weather, you’re shivering under your blankets. You scramble out of bed and prepare a breakfast of instant noodles and a carton of milk you saved from yesterday’s school lunch. Your mom has left you a text asking you to come to visit her in the hospital today and take over her ice cream cart. ")
answer = input("Do you stay at home to study for your test on Monday and risk being evicted from your home the next month, or do you help your mother in a last-ditch effort to avoid being homeless? Yes for studying and No for helping your mother ")
if answer == "yes":
    print("You ignore the text that your mom has sent, and spend the rest of the morning studying for Monday’s test and playing Clash Royale on your phone. As lunch edges closer, your mom has become increasingly worried and texts you again. This time she says, “Dolores, I’m worried about you. My terminal pancreatic cancer has metastasized and in a few days, I’ll no longer be with you to guide you. I’m sorry that I could not provide you a childhood you so longed for.” ")
    answer = input("Do you respond with, “ I want to have an equal shot at an education just like everyone else does in my school”, or do you say, “No need to be sorry mom, I’m coming to visit you right now.” Yes for equal shot for education No for visting mom")
    if(answer == "yes"): # eqaul shot for edu 
        print("You continue to study until the afternoon, losing sense of time as you get caught up in quadratics and logarithms") #result of choice
        answer = input("do you go and take over or not?") #subsequent question
        if(answer == "yes"):
            print("Sure, mom I'll see if can come by today and take over the business")
    if(answer == "no"): # visting mom 
        print 
if answer == "no": # visting mom 
    print("You visit your mom in the hospital. As you walk into her room, you see your mother, frail and deathly pale. She tries to talk, but her voice has betrayed her. You edge a step closer, and she whispers, “Dolores, I haven’t got much time left. Take care of yourself. I’m sorry that I wasn’t able to provide for you so you could continue an education like everyone else.” You tell her, “It’s okay, I won’t let money stop me from going to school. No matter where you go, I promise that I’ll do my very best to go to graduate from high school and go to university.” As you leave the hospital with held-back tears, you start thinking about your future and all the uncertainty that comes with it. ") 
    print("When you get home, you start looking into community colleges. You want to go to a UC or a State university but you know it won't happen with your current grades ")
    answer = input("Type \"Sign up\" for CSF Tutoring to get you grades up to passing " + "Type \"Drop out\" to drop out of school to help your mo with her ice cream cart" ) # for CSF tutoring 
    if answer = "Sign up":
        print("You ignore your mom’s instructions. When you arrive at school on Monday, you go to your guidance counselor, Ms.Dobbs, and ask her for guidance. She tells you that you can ")
    if answer = "Drop Out":
        #stuff 


