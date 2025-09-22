import random
i = 1
cwon = 0
uwon = 0
wastemove = 0
dict1 = {"paperstone": "paper",
         "stonepaper": "paper",
         "scissorstone": "stone",
         "stonescissor": "stone",
         "scissorpaper": "scissor",
         "paperscissor": "scissor"}
while i <= 3:
    list1 = ["stone", "paper", "scissor"]
    comp = random.choice(list1)
    # print("COMPUTER", comp)
    user = input("ENTER YOUR CHOICE:: ")
    # print("USER", user)
    total = comp + user
    # print(total)
    if total in dict1:
        if dict1[total] == comp:
            cwon = cwon + 1
        else:
            uwon = uwon + 1
    elif comp == user:
        print("MATCH DRAW CONTINUE IF YOU HAVE CHANCE!!")
        wastemove = wastemove + 1
    else:
        print("YOU WASTED YOUR MOVE")
        wastemove = wastemove + 1     
    i = i + 1
print("COMPUTER WON", cwon, "times")
print("USER WON", uwon, "times")
print("USER WASTED", wastemove, "times")         
    