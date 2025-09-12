print("Welcome to Divine Intervention") 
print("To make answering simple and crystal clear: This is not a trauma dump for your problems. For most questions please answer either yes or no! Thank you.")
print("Note: Some questions may provide a 'maybe' option. Just because this option exists does NOT mean you can trauma dump!!!!")
print("Second Note: Ignore most of what was just stated (except for not trauma dumping!!) and answer the questions provided!!!")
print("Finally, I decide if you procrastinate, and ultimantly the fate of your grades!!")
print("To begin, do you believe in yourself?")
yourself=input("yes or no? ")
if yourself=="no":
    print("Do your parents beleive in you?")
    you=input("yes or no? ")
    if you=="no":
        print("Oh I am so sorry (not really).")
        print("Well are you interested in staying out of jail now and for the rest of your life?")
        jail=input("yes or no or maybe? ")
        if jail=="no" or jail=="maybe":
            print("Why on God's green Earth could you have any reason to want to be in jail? ")
            print("(It's a rhetorical question.)")
            print("Don't answer this question (Just think about it)")
        elif jail=="yes":
            print("Congratulations!!!")
            print("If you would like to continue staying out of jail then you should probably consider not procrastinating on your homework:)!!!!")
    elif you=="yes":
        print("Maybe you should listen to them.")
        print("Does the assignment impact your life?")
        life=input("yes or no? ")
elif yourself=="yes":
    print("do the gods above call upon you to do something else?")
    now=input("yes or no? ")
    if now=="no":
        print("Do your second divine gods (your parents who believe in you) require you to become preoccupied?")
        preoccupied=input("no or why would you do that? ")
        if preoccupied=="no":
            print("If you have nothing better to do then for the love of those almighty do your freaking homework!!!!!!!!")
        else:
            print("You have reached the point where I can no longer help you. Have a good day!") 
    elif now=="yes":
        print("Then hazzah you can procrastinate and fail your classes!")
