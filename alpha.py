import equal_shot

def chose_yes():
    print("You ignore the text that your mom has sent, and spend the rest of the morning studying for Monday’s test and playing Clash Royale on your phone. As lunch edges closer, your mom has become increasingly worried and texts you again. This time she says, “Dolores, I’m worried about you. My terminal pancreatic cancer has metastasized and in a few days, I’ll no longer be with you to guide you. I’m sorry that I could not provide you a childhood you so longed for.” ")
    answer = input("Do you respond with, “ I want to have an equal shot at an education just like everyone else does in my school”, or do you say, “No need to be sorry mom, I’m coming to visit you right now.” Yes for equal shot for education No for visting mom")
    if(answer == "yes"): # eqaul shot for edu 
        print("You continue to study until the afternoon, losing sense of time as you get caught up in quadratics and logarithms") #result of choice
        answer = input("do you go and take over or not?") #subsequent question
        if(answer == "yes"):
            print("Sure, mom I'll see if can come by today and take over the business")
    if(answer == "no"): # visting mom 
        print 