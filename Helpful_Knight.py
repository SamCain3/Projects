# Physics 53 Final Project
# Samuel Cain
# 5-29-20


# Imports

import random
import time
import math
import decimal

#Defining Functions

def Intro():
    print
    print("Initializing... please wait...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(2)
    print
    print("Wake up!")
    print
    time.sleep(2)
    print("It's time to get to work!")
    print("Problems aren't going to solve themselves,")
    print("take this and just choose one,")
    print("I'll take care of the others.")
    print
    time.sleep(5)
    print("*Your fellow knight slaps a paper down on your table*")
    time.sleep(4)
    print("*You roll out of bed and grab the paper*")
    time.sleep(4)
    print
    global name
    name = raw_input("A letter! And it's addressed to me: Sir ")
    time.sleep(1.5)
    print
    print("Brave Sir " + str(name) + "! Congratulations on chasing out the great evil from our country,")
    print("repairs have been going well since your victory. However, we no")
    print("longer have enemies for you to battle, so I would like to request your")
    print("assistance with the problems some citizens have been facing around the")
    print("kingdom. Below is a list, please make haste in addressing them.")
    print("     -Your liege, King Whiteson")
    time.sleep(15)
    print
    print("1. Farmer Todd needs help planning his crops for the season, go give him a hand.")
    # Randomize buy/sell price of seeds/crops as well as size of field, find best profit
    print("2. Lord Donovan's son has gone missing, please help find him.")
    # Kid got stuck across a river, throw a rope to him to save him; randomize distance and weight of anchor
    print("3. Blacksmith Henry has a backlog of orders to work through, help him any way you can.")
    # Randomize temperature of forge, metals he has access to
    # - Ask which metal he should use
    # Randomize object he needs to make, amount of metal per object and metal he has, % of metal lost to melting
    # - Ask how many objects he can make
    time.sleep(8)
    print
    time.sleep(1)
    print





def choosePath():
    path = ""
    while path != "1" and path != "2" and path != "3":
        path = raw_input("Which job will you take today? (1, 2, or 3?): ")

    return path

#_____________________________________________________________________________________
def job1():

# Path 1: Farmer

# Intro

#name = "Filler"

    print
    time.sleep(1)
    print
    time.sleep(1)
    print("*You happen to live very close to Farmer Todd's farm, so your journey isn't long*")
    print
    time.sleep(4)
    print(str(name) + "! Thank you so very much for accepting my request. You see,")
    print("my son is off assisting with the relief efforts, and while I can handle all the sowing")
    print("and harvesting, he would always take care of the planning aspects of our work.")
    print
    time.sleep(10)
    print("I hear the King speaks very highly of your intellect, but I won't be able")
    print("to give you much of a hand at all, so I do hope you're prepared.")
    time.sleep(7)


    fm = 0
    while fm == 0:
        print
        time.sleep(3)
        fmready = raw_input("Are you ready to get started? ")
        if fmready == "Yes" or fmready == "yes" or fmready == "y" or fmready == "Y":
            time.sleep(1)
            print
            print("Wonderful!")
            time.sleep(1)
            print("So here's what I know")
            fm = 1

# Length & Width of Field

    l = decimal.Decimal(random.randrange(30000,60000))/100
#print l
    w = decimal.Decimal(random.randrange(30000,60000))/100
#print w
    area = decimal.Decimal(l*w)
#print area

    time.sleep(1)
    print
    time.sleep(1)
    print
    print("My son mapped out our fields before he left and wrote them down here for me")
    print
    time.sleep(3)
    print("*You check his paper, scrawled hastily are the words '" + str(l) + " feet long' and '" +str(w) + " feet wide'*")
    time.sleep(4)
    print
    time.sleep(2)

# Crops Available (Beet, Cucumber, Strawberry, Honeydew)

    cropsAvailable = random.randint(1,4)
    if cropsAvailable == 1:
        print("The seeds I have available are beets, carrots, and strawberries.")
    elif cropsAvailable == 2:
        print("The seeds I have available are beets, carrots, and honeydew.")
    elif cropsAvailable == 3:
        print("The seeds I have available are beets, strawberries, and honeydew.")
    elif cropsAvailable == 4:
        print("The seeds I have available are carrots, strawberries, and honeydew.")
    time.sleep(4)

# Area each crop needs

    barea = decimal.Decimal(random.randrange(100,300))/100
    carea = decimal.Decimal(random.randrange(70,200))/100
    sarea = decimal.Decimal(random.randrange(50,130))/100
    harea = decimal.Decimal(random.randrange(200,500))/100

    time.sleep(1)
    print
    time.sleep(1)
    if cropsAvailable == 1:
        print("Beets will need "+ str(barea) + " square feet of space to grow properly.")
        print("Carrots will need "+ str(carea) + " square feet of space to grow properly.")
        print("Strawberries will need "+ str(sarea) + " square feet of space to grow properly.")
    if cropsAvailable == 2:
        print("Beets will need "+ str(barea) + " square feet of space to grow properly.")
        print("Carrots will need "+ str(carea) + " square feet of space to grow properly.")
        print("Honeydew will need "+ str(harea) + " square feet of space to grow properly.")
    if cropsAvailable == 3:
        print("Beets will need "+ str(barea) + " square feet of space to grow properly.")
        print("Strawberries will need "+ str(sarea) + " square feet of space to grow properly.")
        print("Honeydew will need "+ str(harea) + " square feet of space to grow properly.")
    if cropsAvailable == 4:
        print("Carrots will need "+ str(carea) + " square feet of space to grow properly.")
        print("Strawberries will need "+ str(sarea) + " square feet of space to grow properly.")
        print("Honeydew will need "+ str(harea) + " square feet of space to grow properly.")
    time.sleep(12)


# Buy price of seeds / Sell price of crop

    bbuy = decimal.Decimal(random.randrange(8,20))/100
    cbuy = decimal.Decimal(random.randrange(4,12))/100
    sbuy = decimal.Decimal(random.randrange(3,8))/100
    hbuy = decimal.Decimal(random.randrange(10,40))/100
    bbuyr = round(bbuy, 2)
    cbuyr = round(cbuy, 2)
    sbuyr = round(sbuy, 2)
    hbuyr = round(hbuy, 2)


    bsell = decimal.Decimal(random.randrange(80,260))/100
    csell = decimal.Decimal(random.randrange(50,150))/100
    ssell = decimal.Decimal(random.randrange(30,100))/100
    hsell = decimal.Decimal(random.randrange(150,400))/100
    bsellr = round(bsell, 2)
    csellr = round(csell, 2)
    ssellr = round(ssell, 2)
    hsellr = round(hsell, 2)


    time.sleep(1)
    print
    time.sleep(1)
    if cropsAvailable == 1:
        print("I can buy beet seeds for $" +str(bbuyr) +" and I should be able to sell them for $"+str(bsellr)+" per unit.")
        print("I can buy carrot seeds for $" +str(cbuyr) +" and I should be able to sell them for $"+str(csellr)+" per unit.")
        print("I can buy strawberry seeds for $" +str(sbuyr) +" and I should be able to sell them for $"+str(ssellr)+" per unit.")
    if cropsAvailable == 2:
        print("I can buy beet seeds for $" +str(bbuyr) +" and I should be able to sell them for $"+str(bsellr)+" per unit.")
        print("I can buy carrot seeds for $" +str(cbuyr) +" and I should be able to sell them for $"+str(csellr)+" per unit.")
        print("I can buy honeydew seeds for $" +str(hbuyr) +" and I should be able to sell them for $"+str(hsellr)+" per unit.")
    if cropsAvailable == 3:
        print("I can buy beet seeds for $" +str(bbuyr) +" and I should be able to sell them for $"+str(bsellr)+" per unit.")
        print("I can buy strawberry seeds for $" +str(sbuyr) +" and I should be able to sell them for $"+str(ssellr)+" per unit.")
        print("I can buy honeydew seeds for $" +str(hbuyr) +" and I should be able to sell them for $"+str(hsellr)+" per unit.")
    if cropsAvailable == 4:
        print("I can buy carrot seeds for $" +str(cbuyr) +" and I should be able to sell them for $"+str(csellr)+" per unit.")
        print("I can buy strawberry seeds for $" +str(sbuyr) +" and I should be able to sell them for $"+str(ssellr)+" per unit.")
        print("I can buy honeydew seeds for $" +str(hbuyr) +" and I should be able to sell them for $"+str(hsellr)+" per unit.")
    time.sleep(15)


# Calculations
    print
    bamount = decimal.Decimal(area/barea)
    bamountr = math.trunc(bamount)
#print bamountr
    camount = decimal.Decimal(area/carea)
    camountr = math.trunc(camount)
#print camountr
    samount = decimal.Decimal(area/sarea)
    samountr = math.trunc(samount)
#print samountr
    hamount = decimal.Decimal(area/harea)
    hamountr = math.trunc(hamount)
#print hamountr
    print

    bprofit = math.trunc((bsell-bbuy)*bamountr)
#print bprofit
    cprofit = math.trunc((csell-cbuy)*camountr)
#print cprofit
    sprofit = math.trunc((ssell-sbuy)*samountr)
#print sprofit
    hprofit = math.trunc((hsell-hbuy)*hamountr)
#print hprofit

    if cropsAvailable == 1:
        hprofit = 0
    if cropsAvailable == 2:
        sprofit = 0
    if cropsAvailable == 3:
        cprofit = 0
    if cropsAvailable == 4:
        bprofit = 0

    profitList = [bprofit, cprofit, sprofit, hprofit]
    profitList.sort()
#print profitList
    bestProfit = profitList[-1]
#print bestProfit


    if bestProfit == bprofit:
        bestAns = "beets"
        bestAns1 = "Beets"
        a = 0
        while a == 0:
            Ans = raw_input("Which crop would bring me the best profit?: ")
            if Ans != bestAns and Ans != bestAns1:
                print
                print("Are you sure about that? Something doesn't seem right there.")
            else:
                a = 1
        print
        print("I'll take your word for it, that sounds good to me.")
        b = 0
        time.sleep(1)
        while b == 0:
            Ans1 = input("How much profit would that be? (Just dollars, no cents):  $")
            if Ans1 == bprofit:
                b = 1
            else:
            #print bprofit
            #print Ans1
                print
                print("That really doesn't sound right to me.")
        print
        c = 0
        time.sleep(1)
        print("Wow! That sounds great!")
        time.sleep(1)
        while c == 0:
            Ans2 = input("How many of them would I have to plant to get that profit?: ")
            if Ans2 == bamountr:
                c = 1
            else:
            #print bamountr
            #print Ans2
                print
                print("No way! I don't think you counted right.")

    if bestProfit == cprofit:
        bestAns = "carrots"
        bestAns1 = "Carrots"
        a = 0
        while a == 0:
            Ans = raw_input("Which crop would bring me the best profit?: ")
            if Ans != bestAns and Ans != bestAns1:
                print
                print("Are you sure about that? Something doesn't seem right there.")
            else:
                a = 1
        print
        print("I'll take your word for it, that sounds good to me.")
        b = 0
        time.sleep(1)
        while b == 0:
            Ans1 = input("How much profit would that be? (Just dollars, no cents):  $")
            if Ans1 == cprofit:
                b = 1
            else:
            #print cprofit
            #print Ans1
                print
                print("That really doesn't sound right to me.")
        print
        c = 0
        time.sleep(1)
        print("Wow! That sounds great!")
        time.sleep(1)
        while c == 0:
            Ans2 = input("How many of them would I have to plant to get that profit?: ")
            if Ans2 == camountr:
                c = 1
            else:
            #print camountr
            #print Ans2
                print
                print("No way! I don't think you counted right.")

    if bestProfit == sprofit:
        bestAns = "strawberries"
        bestAns1 = "Strawberries"
        a = 0
        while a == 0:
            Ans = raw_input("Which crop would bring me the best profit?: ")
            if Ans != bestAns and Ans != bestAns1:
                print
                print("Are you sure about that? Something doesn't seem right there.")
            else:
                a = 1
        print
        print("I'll take your word for it, that sounds good to me.")
        b = 0
        time.sleep(1)
        while b == 0:
            Ans1 = input("How much profit would that be? (Just dollars, no cents):  $")
            if Ans1 == sprofit:
                b = 1
            else:
            #print sprofit
            #print Ans1
                print
                print("That really doesn't sound right to me.")
        print
        c = 0
        time.sleep(1)
        print("Wow! That sounds great!")
        time.sleep(1)
        while c == 0:
            Ans2 = input("How many of them would I have to plant to get that profit?: ")
            if Ans2 == samountr:
                c = 1
            else:
            #print samountr
            #print Ans2
                print
                print("No way! I don't think you counted right.")

    if bestProfit == hprofit:
        bestAns = "honeydew"
        bestAns1 = "Honeydew"
        a = 0
        while a == 0:
            Ans = raw_input("Which crop would bring me the best profit?: ")
            if Ans != bestAns and Ans != bestAns1:
                print
                print("Are you sure about that? Something doesn't seem right there.")
            else:
                a = 1
        print
        print("I'll take your word for it, that sounds good to me.")
        b = 0
        time.sleep(1)
        while b == 0:
            Ans1 = input("How much profit would that be? (Just dollars, no cents):  $")
            if Ans1 == hprofit:
                b = 1
            else:
            #print hprofit
            #print Ans1
                print
                print("That really doesn't sound right to me.")
        print
        c = 0
        time.sleep(1)
        print("Wow! That sounds great!")
        time.sleep(1)
        while c == 0:
            Ans2 = input("How many of them would I have to plant to get that profit?: ")
            if Ans2 == hamountr:
                c = 1
            else:
            #print hamountr
            #print Ans2
                print
                print("No way! I don't think you counted right.")

    print
    print("Well it's all settled then! I'll get started on that as soon as I can!")
    time.sleep(3)
    print

# Random Event (75% chance to occur, 3 possibilities)*******************************

    global p
    global pie
    global cake
    cake = 0
    p = random.randint(0,3)

    if p != 0:
        print("I'm off, but stick around for a second, my wife has something for you for all your hard work.")
        if p == 1:
            pie = "cherry"
        if p == 2:
            pie = "banana cream"
        if p == 3:
            pie = "pecan"


#***************************************************************************************



    time.sleep(2)
    print
    time.sleep(2)
    print("*Farmer Todd jogs off to start sowing his field, he shouts his thanks over his shoulder*")
    time.sleep(1)

#_____________________________________________________________________________________

#_____________________________________________________________________________________
def job2():

# Path 2: Missing child

# Intro

#name = "Filler"
#if needtabs = yes:
    print
    time.sleep(1)
    print
    time.sleep(1)
    print("*You reach Lord Donovan's manor after a small journey, it is tucked away in the forest behind a winding path*")
    print
    time.sleep(1)
    print
    time.sleep(6)
    print("Ah yes, Sir "+ str(name) + ", I've been expecting you. As you were informed,")
    print("my son Philip went missing when he was outside playing yesterday.")
    print
    time.sleep(6)
    print("I do not take the safety of my family lightly,")
    print("I want your word that you will bring him home safely.")
    time.sleep(6)
    
    ld = 0
    while ld == 0:
        print
        time.sleep(4)
        ldready = raw_input("Can you promise me that? ")
        if ldready == "Yes" or ldready == "yes" or ldready == "y" or ldready == "Y":
            time.sleep(1)
            print
            print("I appreciate that.")
            time.sleep(1)
            print("This is what I know so far")
            print
            ld = 1

# Information

    time.sleep(2)
    infoList = random.randint(1,4)

    info1 = "Nanette the maid says she saw him playing at the edge of the woods before dark."
    info2 = "Clarence the cook told me he overhead Philip say he was bored and wanted an adventure."
    info3 = "Michael the butler said he was playing hide and seek with Philip, but wasn't able to find him."
    info4 = "My wife told me he was whining about going swimming and wouldn't talk to her after she said no."

    if infoList == 1:
        print (info1)
        time.sleep(3)
        print (info2)
        time.sleep(3)
        print (info3)
    if infoList == 2:
        print (info1)
        time.sleep(3)
        print (info2)
        time.sleep(3)
        print (info4)
    if infoList == 3:
        print (info1)
        time.sleep(3)
        print (info3)
        time.sleep(3)
        print (info4)
    if infoList == 4:
        print (info2)
        time.sleep(3)
        print (info3)
        time.sleep(3)
        print (info4)

    time.sleep(8)
    print
    print("That is all I have heard, please be on your way and work swiftly.")
    time.sleep(3)
    print
    time.sleep(1)
    print("*You set out to look for Philip as Lord Donovan continues to pace anxiously*")
    time.sleep(4)
    print
    time.sleep(1)
    print
    time.sleep(1)

# Branching paths

    print("*You come to a branch in the path, it extends in 3 directions*")
    time.sleep(3)

# Randomize paths*******************

    q = "Leads back to the village, maybe he went to find a friend to play with."
    r = "Leads down to the river, that seems like a place kids would play."
    s = "Leads further into the forest, maybe he got lost while playing."

    wayList = [q, r, s]
#print wayList
    random.shuffle(wayList)
#print wayList
    way1 = wayList[-1]
    way2 = wayList[-2]
    way3 = wayList[0]

#***********************************

    global p
    global pie
    p = 0
    pie = 0
    m = 0
    d = 0
    while m == 0:
        print
        time.sleep(1)
        print("1. "+ way1)
        if d == 0:
            time.sleep(3)
        print("2. "+ way2)
        if d == 0:
            time.sleep(3)
        print("3. "+ way3)
        if d == 0:
            time.sleep(2)
        time.sleep(2)
        print
        chooseWay = raw_input("Which path seems right? (Village, River, or Forest): ")
        d = 1
        time.sleep(1)
        if chooseWay == "Village" or chooseWay == "village":
            print
            print("*You head back to the village*")
            time.sleep(3)
            print
            time.sleep(1)
            print("*Along your way you see plenty of children playing, but no sign of Philip*")
            time.sleep(4)
            print
            time.sleep(1)
            print
            time.sleep(1)
            print("*You're getting nowhere, so you decide to head back*")
            time.sleep(3)
            print
            time.sleep(1)
            print("It's getting late, I can't afford to wander around aimlessly.")
            time.sleep(4)
            print
            time.sleep(1)
            print
            time.sleep(1)
            print("*You find yourself back at the break in the path*")
            time.sleep(3)
            p = 1
            pie = "coconut cream"

        if chooseWay == "Forest" or chooseWay == "forest":
            print
            print("*You head further into the forest*")
            time.sleep(3)
            print
            time.sleep(1)
            print("*As you weave through the trees, you see no evidence that Philip was here*")
            time.sleep(4)
            print
            time.sleep(1)
            print
            time.sleep(1)
            print("*You're getting nowhere, so you decide to head back*")
            time.sleep(3)
            print
            time.sleep(1)
            print("It's getting late, I can't afford to wander around aimlessly.")
            time.sleep(4)
            print
            time.sleep(1)
            print
            time.sleep(1)
            print("*You find yourself back at the break in the path*")
            time.sleep(3)
            p = 1
            pie = "blackberry"
        
        if chooseWay == "River" or chooseWay == "river":
            print
            print("*You head in the direction of the river*")
            time.sleep(3)
            print
            time.sleep(1)
            print("*As you're walking, you notice small footprints, you decide to follow them*")
            time.sleep(4)
            print
            time.sleep(1)
            print
            time.sleep(1)
            print("*You hear a scream in the distance*")
            time.sleep(3)
            print
            print("Help!")
            time.sleep(1)
            print("HELP!")
            time.sleep(1)
            print("HEEEEELLLLLLP!!!")
            time.sleep(4)
            print
            print("*You notice a small figure waving their arms on a small island in the middle of the river*")
            time.sleep(4)
            print("That must be Philip.")
            time.sleep(1)
            print
            time.sleep(1)
            print("*You head down the bank towards the water*")
            time.sleep(3)
            print
            time.sleep(1)
            m = 1

# Finding Child

    print
    time.sleep(1)
    print("*You can clearly see Philip is stranded with no way to get back to shore*")
    time.sleep(3)
    print
    time.sleep(1)
    print("*He shouts to you from a distance*")
    time.sleep(2)
    print("'Sir Knight! I swam over here, but got stuck when the waters sped up, please help me'")
    time.sleep(4)
    print
    time.sleep(1)
    print("Well this is certainly a different job than I signed up for, but I guess I'm up to the task")
    time.sleep(4)
    print
    time.sleep(1)

# Problem

# Calculations***********************

    decimal.getcontext().rounding = decimal.ROUND_DOWN

    initialSpeed = int(random.randrange(14,20))
    corrAns = int(random.randrange(30,60))
    corrAnsrad = float((corrAns*math.pi)/180)
    vertSpeed = float(initialSpeed*(math.sin(corrAnsrad)))
    vertTime = float((2*vertSpeed)/(9.81))
    horSpeed = float(initialSpeed*math.cos(corrAnsrad))
    riverWidthur = str(float(horSpeed*vertTime))
    k = decimal.Decimal(riverWidthur)
    riverWidth = round(k,2)
    
    r = decimal.Decimal(str(float(random.randrange(1500,3000))/100))
    rockWeight = float(round(r,2)) #Red Herring

#************************************


    print("*You look over the tools you have at your disposal*")
    time.sleep(3)
    print
    time.sleep(1)
    print("*There is a sign nearby claiming that the island is "+ str(riverWidth) + " meters away*")
    time.sleep(4)
    print
    time.sleep(1)
    print("*There is a large coil of excess rope next to a rope swing*")
    time.sleep(3)
    print
    time.sleep(1)
    print("*You figure you could probably pull him back across the river if you could get the rope to him*")
    time.sleep(5)
    print
    time.sleep(1)
    print("*You grab the coil of rope and a large rock sitting nearby it*")
    time.sleep(5)
    print("*The rock feels heavy, about "+str(rockWeight)+" Kilograms if you were to estimate*")
    time.sleep(6)
    print
    time.sleep(1)
    print("From your days in the King's forces, you gained a knack for estimating your own strength")
    time.sleep(5)
    print("You estimate that you could throw this rock at approximately " +str(initialSpeed)+ " meters per second.")
    time.sleep(6)
    print
    time.sleep(1)
    print("*You tie the end of the rope securely around your rock*")
    time.sleep(5)
    print

# Question

    #print(int(corrAns))
    g = 0
    while g == 0:
        time.sleep(1)
        Ans = input("What angle should you throw it at? (Round Down): ")
        if int(Ans) == int(corrAns):
               print("Well, here goes nothing")
               time.sleep(1)
               print
               time.sleep(3)
               print("*You throw the rock with all your might at a "+str(Ans) +" degree angle*")
               time.sleep(2)
               print
               print("*                          ")
               time.sleep(0.05)
               print("    *                      ")
               time.sleep(0.09)
               print("        *                  ")
               time.sleep(0.15)
               print("            *              ")
               time.sleep(0.23)
               print("               *           ")
               time.sleep(0.33)
               print("                  *        ")
               time.sleep(0.45)
               print("                    *      ")
               time.sleep(0.59)
               print("                      *    ")
               time.sleep(0.6)
               print("                       *   ")
               time.sleep(0.6)
               print("                        *  ")
               time.sleep(0.6)
               print("                        *  ")
               time.sleep(0.6)
               print("                       *   ")
               time.sleep(0.6)
               print("                      *    ")
               time.sleep(0.59)
               print("                    *      ")
               time.sleep(0.45)
               print("                  *        ")
               time.sleep(0.33)
               print("               *           ")
               time.sleep(0.23)
               print("            *              ")
               time.sleep(0.15)
               print("        *                  ")
               time.sleep(0.09)
               print("    *                      ")
               time.sleep(0.05)
               print("*Thud*")
               time.sleep(1)
               print
               g = 1
        else:
               print("Well, here goes nothing")
               time.sleep(1)
               print
               time.sleep(3)
               print("*You throw the rock with all your might at a "+str(Ans) +" degree angle*")
               time.sleep(2)
               print
               print("*                          ")
               time.sleep(0.05)
               print("    *                      ")
               time.sleep(0.09)
               print("        *                  ")
               time.sleep(0.15)
               print("            *              ")
               time.sleep(0.23)
               print("               *           ")
               time.sleep(0.33)
               print("                  *        ")
               time.sleep(0.45)
               print("                    *      ")
               time.sleep(0.59)
               print("                      *    ")
               time.sleep(0.6)
               print("                       *   ")
               time.sleep(0.6)
               print("                        *  ")
               time.sleep(0.6)
               print("                        *  ")
               time.sleep(0.6)
               print("                       *   ")
               time.sleep(0.6)
               print("                      *    ")
               time.sleep(0.59)
               print("                    *      ")
               time.sleep(0.45)
               print("                  *        ")
               time.sleep(0.33)
               print("               *           ")
               time.sleep(0.23)
               print("            *              ")
               time.sleep(0.15)
               print("        *                  ")
               time.sleep(0.09)
               print("    *                      ")
               time.sleep(0.05)
               print("*Splash*")
               time.sleep(1)
               print(".")
               time.sleep(1)
               print(".")
               time.sleep(1)
               print(".")
               time.sleep(2)
               print("You missed...")
               time.sleep(3)
               print
               time.sleep(1)
               print("*You pull back in your rope and prepare for another toss*")
               time.sleep(1)
               print

    print("*You land your shot perfectly on target, narrowly missing Philip in the process*")
    time.sleep(6)
    print
    time.sleep(1)
    print("*Philip grabs hold of the rope and you reel him in to shore*")
    time.sleep(2)
    print
    time.sleep(0.2)
    print
    time.sleep(0.7)
    print
    time.sleep(0.2)
    print
    time.sleep(0.7)
    print
    time.sleep(0.2)
    print
    time.sleep(2)

# Conclusion

    print("*You bring Philip ashore and reunite him with his parents*")
    time.sleep(4)
    print
    time.sleep(1)
    print("Thank you Sir "+ str(name)+ ", I never once doubted your ability.")
    time.sleep(2)
    print("Our family thanks you and I will give my regards to the King.")
    time.sleep(1)



#_____________________________________________________________________________________


#_____________________________________________________________________________________
def job3():
    
    #  Path 3: Blacksmith
    #  Intro

#name = "filler"

    time.sleep(1)
    print
    time.sleep(1)
    print("*You arrive at the blacksmith's house after a short journey down the road*")
    time.sleep(3)
    print
    time.sleep(1)
    print
    time.sleep(3)
    print("Sir "+ str(name) + "! Thank you so much for coming, my orders are extremely")
    print("backed up and your help will be invaluable.")
    time.sleep(6)
    print
    print("Blacksmithing is hard work, and you'll have to be in")
    print("top shape if we want to finish before sundown.")
    time.sleep(6)

    bs = 0
    while bs == 0:
        print
        time.sleep(4)
        bsready = raw_input("Are you ready to get started? ")
        if bsready == "Yes" or bsready == "yes" or bsready == "y" or bsready == "Y":
            time.sleep(1)
            print
            print("Great!")
            time.sleep(1)
            print("So here's the situation")
            print
            bs = 1


#  Heat of furnace (2000-3000F)

    time.sleep(2)
    furnaceTemp = random.randint(2000, 3000)

    print("I'm still rebuilding since my shop was burned down in the battle,")
    print("so my equipment isn't perfect. From what I can tell, my furnace")
    print("can only get up to about " + str(furnaceTemp) + " degrees today.")

    time.sleep(8)
    print
#  Gold (1945F), Iron (2700F), Steel (2800F)

    materialAvailable = random.randint(1,3)

    if materialAvailable == 1:
        print("I currently have access to Gold and Iron")
        y = 0
        while y == 0:
            chosenMetal = raw_input("Which metal should I use? (Gold or Iron): ")
            if chosenMetal == "Iron" and furnaceTemp <= 2700:
                print
                print("I'm not sure my furnace is hot enough to use that type of metal.")
            elif chosenMetal == "iron" and furnaceTemp <= 2700:
                print
                print("I'm not sure my furnace is hot enough to use that type of metal.")
            else:
                y = 1

    elif materialAvailable == 2:
        print("I currently have access to Iron and Steel")
        z = 0
    
        while z == 0:
            questionTemp = raw_input("Do you think my furnace is hot enough to melt these? (Y or N): ")
            print
            if furnaceTemp >= 2700 and questionTemp == "Y":
                print("You know what? You're right, I think we'll be fine.")
                time.sleep(1)
                z = 1
            elif furnaceTemp >= 2700 and questionTemp == "N" or furnaceTemp <= 2700 and questionTemp == "Y":
                print("Are you sure? I think you should check your numbers again, don't want to waste our time.")
            elif furnaceTemp <= 2700 and questionTemp == "N":
                furnaceTemp = random.randint(2700, 3000)
                print("You're right, I should be able to turn it up to around " + str(furnaceTemp) +"F, that should be good.")
                z = 1
                
        y = 0
        while y == 0:
            chosenMetal = raw_input("Which metal should I use? (Iron or Steel): ")
            if chosenMetal == "Steel" and furnaceTemp <= 2800:
                print
                print("I'm not sure my furnace is hot enough to use that type of metal.")
            elif chosenMetal == "steel" and furnaceTemp <= 2800:
                print
                print("I'm not sure my furnace is hot enough to use that type of metal.")
            else:
                y = 1



    elif materialAvailable == 3:
        print("I currently have access to Gold and Steel")
        y = 0
        while y == 0:
            chosenMetal = raw_input("Which metal should I use? (Gold or Steel): ")
            if chosenMetal == "Steel" and furnaceTemp <= 2800:
                print
                print("I'm not sure my furnace is hot enough to use that type of metal.")
            elif chosenMetal == "steel" and furnaceTemp <= 2800:
                print
                print("I'm not sure my furnace is hot enough to use that type of metal.")
 
            else:
                y = 1

    time.sleep(1)
    print("Alright, we'll go with " + str(chosenMetal) + " then.")
    time.sleep(3)




#  Helmet (2-4lbs), Sword (4-7lbs), Dagger (1-3lbs)

    print
    time.sleep(1)
    gearNeeded = random.randint(1,3)
    if gearNeeded == 1:
        itemWeight = random.randint(2,5)
        chosenItem = "helmet"
    if gearNeeded == 2:
        itemWeight = random.randint(4,7)
        chosenItem = "sword"
    if gearNeeded == 3:
        itemWeight = random.randint(2,4)
        chosenItem = "dagger"



    if gearNeeded == 1:
        print("I have an order for helmets today")
        time.sleep(2)
        print("I'll need " + str(itemWeight) + " pounds of " + str(chosenMetal) + " to make 1 helmet.")

    if gearNeeded == 2:
        print("I have an order for swords today")
        time.sleep(2)
        print("I'll need " + str(itemWeight) + " pounds of " + str(chosenMetal) + " to make 1 sword.")

    if gearNeeded == 3:
        print("I have an order for daggers today")
        time.sleep(2)
        print("I'll need " + str(itemWeight) + " pounds of " + str(chosenMetal) + " to make 1 dagger.")


#  Amount of Material


    time.sleep(4)
    print
    if chosenMetal == "iron" or chosenMetal == "Iron":
        materialAmount = random.randint(45, 120)
    if chosenMetal == "gold" or chosenMetal == "Gold":
        materialAmount = random.randint(25, 55)
    if chosenMetal == "steel" or chosenMetal == "Steel":
        materialAmount = random.randint(40, 85)

    print("Resources are scarce, so I only have " +str(materialAmount) +" lbs of " + str(chosenMetal) +" ore to work with.")

#  % of material lost (10-40%)


    time.sleep(4)
    if chosenMetal == "iron" or chosenMetal == "Iron":
        materialLost = random.randint(20, 50)
    if chosenMetal == "gold" or chosenMetal == "Gold":
        materialLost = random.randint(30, 50)
    if chosenMetal == "steel" or chosenMetal == "Steel":
        materialLost = random.randint(10, 30)

    print("Even worse, my ore isnt perfect, so we'll be losing about " + str(materialLost) + " percent of the mass once we melt it down.")
    time.sleep(8)
    print

# Calculations


#print(materialLost)
    metalPercent = (100 - materialLost)
#print(str(metalPercent))
    finalAmount = (metalPercent*materialAmount)
#print(str(finalAmount))
    correctPieces = (finalAmount/itemWeight)
#print(str(correctPieces))
    corrAns = (correctPieces/100)
#print(str(corrAns))

    print("I'm really not too good with my numbers, but the King says you're an expert.")

    time.sleep(1)
    x = 0
    while x == 0:
        Ans = input("How many pieces can I make? (No decimals): ")
        if int(Ans) == int(corrAns):
            print("Really? I would've have no idea how to start, thanks for the help!")
            x = 1
        else:
            print
            print("I don't know why, but that doesn't seem right, maybe run your numbers again?")

    time.sleep(4)
    print
    time.sleep(1)
    print
    time.sleep(1)
    print
    print("*You and Henry get to work on the "+ str(chosenItem) + "s*")
    print
    time.sleep(2)
    print
    time.sleep(2)
    print
    time.sleep(2)
    print

# Random Event (75% chance to occur, 3 possibilities)*******************
    global p
    global pie
    global cake
    p = random.randint(0,3)
    if p == 1:
        pie = ""
        while pie == "":
            pie = raw_input("Sir " + str(name) + ", random question, but what's your favorite fruit? ")
            print("Ooh that's a good one, mine are strawberries")
            time.sleep(2)
            print
            time.sleep(1)
            print
            print
            print("*You both get back to work*")
    
    elif p == 2:
        pie = ""
        while pie == "":
            pie = raw_input("Sir " + str(name) + ", random question, but do you happen to like strawberries? ")
            if pie == "yes" or pie == "Yes" or pie == "y" or pie == "Y":
                print("Splendid! They're my favorite, I believe they're in season now too.")
                pie = "strawberry"
            else:
                print("Ah, that's a shame, I believe they're in season at the moment.")
                pie = "apple"
        time.sleep(2)
        print
        time.sleep(1)
        print
        print
        print("*You both get back to work*")
    elif p == 3:
        pie = ""
        while pie == "":
            pie = raw_input("Sir " + str(name) + ", random question, but do you like pie? ")
            if pie == "yes" or pie == "Yes" or pie == "y" or pie == "Y":
                print("Splendid! My wife makes the best pies, you'll have to take one home.")
                pie = "strawberry"
            else:
                print("That's a shame, my wife makes the best pies in town,")
                print("maybe I can convince you to try one some time.")
                pie = 0
                cake = 1
        time.sleep(2)
        print
        time.sleep(1)
        print
        print
        time.sleep(1)
        print("*You both get back to work*")
#**************************************************


    time.sleep(2)
    print
    time.sleep(2)
    print
    time.sleep(2)
    print
    time.sleep(2)
    print("*After a long day of hard work, you successfully helped make "+ str(corrAns)+ " " + str(chosenItem) +"s!*")
    time.sleep(8)

#____________________________________________________________________________________________________


def runPath(choosePath):
    print
    print
    time.sleep(1)
    if choosePath == "1":
        print("Farming? That doesn't seem too bad, let's go with that one.")
    if choosePath == "2":
        print("I've been a bit bored lately, finding a missing kid seems kind of fun.")
    if choosePath == "3":
        print("I always wanted to see how my gear was made, let's try out blacksmithing.")
 
    time.sleep(3)
    print
    time.sleep(1)
    print("*You head off down the road, glad to have an easy job for once.*")
    time.sleep(2)
    print

    #Job 1 Path run
    if choosePath == "1":        
        NPCs = "Lord Donovan and Blacksmith Henry"
        NPC = "Farmer Todd"
        #print("Start 1")
        job1()
        

    #Job 2 Path run
    if choosePath == "2":
        NPCs = "Farmer Todd and Blacksmith Henry"
        NPC = "Lord Donovan"
        #print("Start 2")
        job2()


    #Job 3 Path run
    if choosePath == "3":
        NPCs = "Farmer Todd and Lord Donovan"
        NPC = "Blacksmith Henry"
        #print("Start 3")
        job3()

    print
    time.sleep(1)
    print
    time.sleep(2)
    if p != 0:
        print("Before you head out the door, " +str(NPC) + "'s wife hands you a freshly made " +str(pie) +" pie.")
        time.sleep(4)
        print("That's awfully sweet of her, and I certainly feel like I've been repaid for my work now.")
        time.sleep(8)
        print
        time.sleep(1)
        print("You return home and chat with your fellow Knight about your days as you both snack on your pie,")
        
    elif cake == 1:
        print("Before you head out the door, " +str(NPC) + "'s wife hands you a freshly made angel food cake.")
        time.sleep(2)
        print("She sure works quick, I certainly feel like I've been repaid for my work now.")
        time.sleep(8)
        print
        time.sleep(1)
        print("You return home and chat with your fellow Knight about your days as you both snack on your cake,")

    elif p == 0 and cake == 0:
        print("You return home and chat with your fellow Knight about your days,")

    time.sleep(5)
    print("it seems he had a good time helping "+ str(NPCs) + ", you're a tad jealous")
    print
    time.sleep(6)
    print("Maybe those other 2 jobs could've been even more fun.")
    print
    time.sleep(5)
    

    
# Run Code Start

playAgain = "yes"
while playAgain == "yes" or playAgain == "Yes" or playAgain == "y" or playAgain == "Y":
    Intro()
    choice = choosePath()
    runPath(choice) # 1, 2, or 3
    playAgain = raw_input("Do you want to play again?: ")
