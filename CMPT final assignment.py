#####################################
#######    Final Projet MPT 120      #######
#######    Dean Chiu  301309796    #######
#######    Angus Fan 301317306     #######
#######  Artur Eginyan 301311126  #######
#####################################

def read_string_list_from_file(the_file):
    fileRef = open(the_file,"r") 
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1] 
        localList.append(string)        
    fileRef.close()
    return localList

def catchNum(file):
    if file == "d":
        filename = "planetsData1.txt"
        localList = read_string_list_from_file(filename)
    else:
        filename = input("enter the file name: ")
        localList = read_string_list_from_file(filename)
    planCiv, planFuel, planRocks = [],[],[]
    for i in range (len(localList)):
        localList[i] = localList[i].split("-")
        planCiv.append(int(localList[i][0]))
        planFuel.append(int(localList[i][1]))
        planRocks.append(int(localList[i][2]))
    return (planCiv,planFuel,planRocks)

def welcome ():
    print ("\nWelcome to No Man's Scam CMPT 120 Game!!")
    print ("========================================\n")
    
def board(planetNum,Civ,Fuel,Rocks):
    print ("It is turn number: "+ str(moves[0]))
    planetList = []
    if drawboard == "y":
        for i in range(planetNum):
            planetList.append(i)
        print ("Planet #" + "  " + "Civ" + "    "+"Fuel" + "      " + "Rocks")
        for a,b,c,d in zip(planetList,Civ,Fuel,Rocks):
            if charPos[0] == a:
                print ("%4s %7s %7s %9s" % (a,b,c,d) + "    <~~~  " + charName)
            else:
                print ("%4s %7s %7s %9s" % (a,b,c,d))
                
def movePosition(charPos):
    move= input("\nDo you want to roll a die (d) or choose the number positions you want to move by (c)?: ")
    move = validateinput(str(),move,"d","c")
    out  = False
    while out == False:
        if (move == "d" or move == "c"):
            if move == "d":
                dist = r.randint(1,6)
                print ("You rolled a " + str(dist) )
                print ("")
                out = True
            elif move == "c":
                dist = input ("How many moves do you want to make?: ")
                dist = validateinput(int(),dist,0,100)
                out = True
        while (move != "d" and move != "c"):
            move = input("Please enter a valid input (d/c): ")
            move = validateinput(str(),move,"d","c")
    position = charPos[0] + int(dist)
    position = position % planNum[0]
    charPos.append(position)
    del(charPos[0])
    print(charName + " is on planet " + str(charPos[0]))
    return (charPos, moves)

def validateinput(propInput,Input,para1,para2):
    if type(propInput) == int:
        while not(Input.isdigit()) or not(para1 <= int(Input) <= para2):
            Input = input("Please enter a valid input ("+ str(para1) + ".."+ str(para2)+"): ")
    elif type (propInput) == str:
        while not (Input.isalpha()) or (Input not in (para1,para2)):
            Input = input("Please enter a valid input ("+ para1 + "/" + para2+"): ")
    return Input

def Input ():
    global catchNumlist,drawboard,charName,proportion,varExplosion, normalExplosion, planPyth, charCiv,turns
    proportion = 10
    ### txt input (d/i) ###
    file = input ("Default or input? (d/i): ")
    while file.isdigit() or not file in "di":
        file = input ("Please enter a valid input (d/i): ")
        file = validateinput(str(),file,"d","i")
    if file == "d":
        catchNumlist = catchNum("d")        
    else:
        catchNumlist = catchNum("i")
    ### About Character ###
    print("\nData for character: ")
    charName = input("Name: ")                                     
    charCiv = input("Civilisation level (0..3): ")
    charCiv = validateinput(int(),charCiv,0,3)
    charCiv = int(charCiv)
    charFuel.append( input("Initial fuel (10..50): "))
    charFuel[0] = validateinput(int(),charFuel[0],10,50)
    charFuel[0] = int(charFuel[0])
    recData()
    ### About Game ###
    turns = input("Maximum turns this game (0..10): ")
    turns = validateinput(int(),turns,0,10)
    truns = int(turns)
    planNum.append(len(planRocks)-1)
    planPyth = input("Where do you want Planet Python to be? (1.." + str(planNum[0]) +" or 0 for none): ")
    planPyth = validateinput(int(),planPyth,1,planNum[0])
    if planPyth == "0":
        planPyth = "100"
    planPyth = int(planPyth)
    varExplosion = input("Allow Wow Explosion to happen? (y/n): ")
    varExplosion = validateinput(str(),varExplosion,"y","n")
    if varExplosion == "n":
        normalExplosion = input ("Since you dont want Amazing Explosion to happen, do you want Mild Explosion to happen? (y/n): ")
        normalExplosion = validateinput(str(),normalEXplosion,"y","n")
    if varExplosion == "y" or normalExplosion == "y":
        proportion = input ("Proportion explosion? (1...5 or 0 for none) : ")
        proportion = validateinput(int(),proportion,0,5)
        proportion = int(proportion)
    drawboard = input("Do you want to draw the board? (y/n): ")
    drawboard = validateinput(str(),drawboard,"y","n")
    return turns

def askplay ():
    global gamenum
    play = input("Do you want to play? (y/n): ")
    play = validateinput(str(),play,"y","n")
    gamenum += 1
    return play

def askplayagain ():
    global gamenum
    play = input("Do you want to play again? (y/n): ")
    play = validateinput(str(),play,"y","n")
    if play == "y":
        gamenum += 1
    return play

def Initialize ():
    global charPos, charFuel , charRocks , planNum ,planCiv, planFuel, planRocks,gameover,out,moves,explosionVarify,dist,position,status,play
    gameover,out = False,False
    moves,charPos,charRocks = [1],[0],[0]
    charFuel,planCiv,planFuel,planRocks,planNum = [],[],[],[],[]
    explosionVarify = [0,0]
    dist,position,numcheck,fuel = 0,0,0,0
    status = "alive"
    play ="y"
    return

def recData():
    global planCiv, planFuel, planRocks,charlist
    planCiv = catchNumlist[0]
    planFuel = catchNumlist[1]
    planRocks = catchNumlist[2]
    charlist = [charPos ,charCiv, charFuel[0], charRocks]
    
def checkExplosion():
    planNum[0] = len(planRocks)-1
    if proportion == 0:
        explosionNum = r.randint(1,planNum[0])
    elif  1<=proportion <= 5:
        explosionNum = r.randint (1,proportion*planNum[0])
    if varExplosion == "y":
        wowExplosion(planNum,explosionNum)
    elif varExplosion == "n" and normalExplosion == "y":
        normExplosion(planNum,explosionNum)
    return status

def wowExplosion(planNum,numcheck):
    global planPyth,status
    if numcheck ==charPos[0]:
        status = "dead"
        return status
    if numcheck <= (planNum[0]):
        print ("\n###A wow explosion happened at planet " + str(numcheck)+"###")
        if numcheck < charPos[0]:
            charPos[0] -= 1
            add = int(planRocks[numcheck])
            del (planRocks[numcheck],planCiv[numcheck],planFuel[numcheck])
        else:
            add = int(planRocks[numcheck])
            del(planRocks[numcheck],planCiv[numcheck],planFuel[numcheck])        
        for i in range (numcheck-1,0,-1):
            planRocks[i] = int(planRocks[i]) + add
            add = planRocks[i]
        if numcheck == planPyth:
            planPyth = 100
        if planNum[0] == 1:
            print ("\n###There is no more planet other than planet 0###" )
            status = "stuck"
        planNum[0] -= 1
        planPyth -= 1
    else:
        print ("\n###No explosion happened this round###")
    return

def normExplosion(check,numcheck):
    global planPyth,status
    add = 0
    if numcheck ==charPos[0]:
        status = "dead"
        return status
    if numcheck-1 <= planNum[0]:
        print ("\n###A normal explosion happened at planet " + str(numcheck-1)+"###")
        for i in range (numcheck,0,-1):
            planRocks[i] = int(planRocks[i]) + add
            add = planRocks[i]
    elif numcheck == planPyth:
        planPyth = 100
    else:
        print ("\n###No explosion happened this round###")
    return 

def randomFuel(Fuel):
    global fuel
    fuel = 0
    if Fuel != 0:
        fuel = r.randint(1,Fuel)
    return fuel

def compareCiv(charCiv,planCiv,charFuel):
    print ("\n-Fuel-")
    print ("There are aliens in this planet with civilization level " +str(planCiv[charPos[0]]))
    if charCiv < planCiv[charPos[0]]:
        fuel = randomFuel(planFuel[charPos[0]])
        charFuel[0] = charFuel[0] - fuel
        if charFuel[0] <=0:
            charFuel[0] = 0
        (planFuel[charPos[0]] )+= fuel
        print("The aliens are more inteligent than you and were able to scam you")
        print ("You lost " + str(fuel) + " litres of fuel")
    elif charCiv == planCiv[charPos[0]]:
        fuel = randomFuel(charFuel[0])
        charFuel[0] = charFuel[0] - fuel
        if charFuel[0] <=0:
            charFuel[0] = 0
        planFuel[charPos[0]] += fuel
        print("The aliens outsmarted you.")
        print ("You lost " + str(fuel) + " litres of fuel")
    elif charCiv > planCiv[charPos[0]]:
        fuel = randomFuel(planFuel[charPos[0]])
        charFuel[0] = charFuel[0] + fuel
        planFuel[charPos[0]] -= fuel
        print("You are more intelligent than the aliens and made a great deal")
        print ("You gained " + str(fuel) + " litres of fuel")
    print ("You now have " + str(charFuel[0]) +" litres of fuel")
    charlist[2] = charFuel[0]
    return

def compareRocks(charRocks,planRocks):
    print ("\n-Rocks-")
    print("There are " +str(planRocks[charPos[0]]) + " rocks on this planet")
    charRocks.append(planRocks[charPos[0]]//3)
    planRocksLost = planRocks[charPos[0]]//3
    planRocks[charPos[0]] = planRocks[charPos[0]] - planRocksLost
    print (charName+ " collected " + str(planRocksLost )+ " rocks.")
    print (charName + " now has " + str(charRocks) + " rocks\n")
    return charRocks

def GameCondition(charFuel,charPos,moves,status,turns):
    global win
    gameover = bool()
    if charFuel[0] <= 0:
        print ("You ran out of Fuel and got stranded on the planet")
        gameover = True
    elif charPos[0] == planPyth:
        print ("Congratulations, " + charName + " has successfully reached Planet Python!!")
        gameover = "win"
        win += 1
    elif moves[0] > int(turns):
        print ("You ran out of turns and can no longer continue on your quest")
        gameover = True
    elif status == "dead":
        print (charName + " did not survive his journey")
        gameover = True
    elif status == "stuck":
        print ("you are stuck at planet 0")
        gameover = True
    return gameover

def Info(charlist):
    print ("Update Info")
    print (charName + "'s current position is : " + str(charPos[0]))
    print (charName + " has " + str(charlist[2]) + " litres of fuel")
    print (charName + " collected " + str(charlist[3])+" rocks so far")
    print (charName + " is " + status)
    if gameover == False:
        print (charName + " is ready to continue")
    elif gameover == "win":
        print ("")
    elif gameover == "win":
        print (charName + " has won the game ")
    else:
        print ("R.I.P. " + charName)
        
def binary(planRocks):
    bine =[]
    for i in range (len(planRocks)):
        if planRocks[i]%2 == 0:
            bine.append(0)
        else:
            bine.append(1)
    return bine

def base2(bine):
    s,ans =0,0
    for i in range (-1,-len(bine)-1,-1):
        ans = ans + bine[i]*(2**s)
        s += 1
    return ans

def result (planRocks):
    lastRocks = planRocks
    print ("############### Final Result ###############")
    print ("The rock specimens remain in the last game is " + str(lastRocks))
    print ("The corresponing binary is " + str(binary(lastRocks)))
    print ("The number is "+ str(base2(binary(lastRocks))) + " in base 2")
    print ("The user has played " + str(gamenum) + " game(s).")
    print ("Of those, the user  won " + str(win) + " game(s)")
    print ("############################################")
    
##### Top Level   #####
import random as r
win,gamenum = 0,0
welcome()
Initialize()
play = askplay()
while play == "y":
    Initialize()
    turns = Input ()
    board(planNum[0]+1,planCiv,planFuel,planRocks)
    while gameover == False:
        status = checkExplosion()
        print ("\n****After Explosion****")
        board(planNum[0]+1,planCiv,planFuel,planRocks)
        gameover = GameCondition(charFuel,charPos,[0],status,turns)
        if gameover == False:
            charPos = movePosition (charPos)[0]
            print ("\n****After Moving Position****")
            board(planNum[0]+1,planCiv,planFuel,planRocks)
            moves[0] += 1
            compareCiv(charCiv,planCiv,charFuel)
            compareRocks(charRocks,planRocks)
            gameover = GameCondition(charFuel,charPos,moves,status,turns)
            if gameover == False:
                Info(charlist)
    play = askplayagain()
if play == "n":
    print ("I'm sorry you feel that way \n")
    result(planRocks)



            
