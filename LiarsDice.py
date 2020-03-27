"""     Liar's Dice
    A Game By BJ Mestnik
        On Python3
        weeeeeeeee
                        """

import random, sys, time
dieNumber=1
dieQuant=1
bet=[1,1]
remainingDice=[]
diceList={}
numDice=1
diceCount={}
deleteList={}
totalDiceLeft=0
originalNumPlayers=0

def compileDiceList():                    # Function for compliling a complete list of dice for each round
    global numPlayers, numDice, diceList
    diceList={}
    for player in range(1,numPlayers+1):
        miniDiceList=[]
        for die in range(numDice):
            miniDiceList.append(random.randint(1,6))
        diceList.setdefault(player,miniDiceList)
        if player in deleteList:
            for a in range(deleteList[player]):
                del diceList[player][random.randint(0,(len(diceList[player])-1))]

def countDice():                          # Function for counting total quantity of each number
    global diceList, diceCount, totalDiceLeft
    totalDiceLeft=0
    for v in  diceList.values():
        for die in v:
            diceCount.setdefault(die,0)
            diceCount[die]+=1
    for number in diceCount:
        totalDiceLeft+=diceCount[number]
    return diceCount

def deleteDice(player):                        # Function for deleting dice of a player
    deleteList.setdefault(player,0)
    deleteList[player]+=1
    return deleteList

def checkLoss():                                # Function for checking if a player has lost
    global playerPosition, diceList, numPlayers, stillPlayerDice
    copyDiceList=diceList.copy()
    for player in copyDiceList:
        if copyDiceList[player]==[] and player!=playerPosition:
            print("Player "+str(player)+" is out of dice and has been eliminated")
            numPlayers-=1
            del diceList[player]
    if playerPosition not in diceList or diceList[playerPosition]==[]:
        stillPlayerDice=False
    elif len(diceList)==1:
        print("You are the only player left! Congratualtions, you are a huge liar!")
        sys.exit()

def playerBet():                                # Function for Player to place bet
    global dieNumber,dieQuant,bet
    sure=False
    while sure!=True:
        x=True
        print("Please place a bet")
        print("What die number would you like to bet on?")
        dieNumber=input()
        if dieNumber.isdecimal()==False or int(dieNumber)>6 or int(dieNumber)<1:
            print('Please enter a number between 1 and 6\n')
        else:
            print("How many "+dieNumber+"s do you think there are on the table?")
            dieQuant=input()
            if dieQuant.isdecimal()==False:
                print('Please enter a number')
            elif int(dieQuant)<bet[0]:
                print('Either bet quantity or die number must be greater than the current bet of '+str(bet[0])+" "+str(bet[1])+"s")
            else:
                while x==True:
                    print("You think there are a total of " + dieQuant + " dice with the number "+ dieNumber)
                    print("Is this true?")
                    sureQuest=input('y/n: ')
                    if sureQuest=='n' or sureQuest=='no':
                        x=False
                    elif sureQuest=='y' or sureQuest=='yes':
                        bet=[int(dieQuant),int(dieNumber)]
                        sure=True
                        x=False
                    else:
                        print("Please enter 'y' or 'n' ")
    return bet #bet=[int(dieQuant),int(dieNumber)]

def playerDoubt():                              # Function for Player to doubt previous bet
    global noDoubt,diceList,currentPlayer
    x=True
    while x== True:
        print("Do you doubt the previous bet?")
        print("(careful, if you are wrong you will lose a die)")
        doubt=input('y/n: ')
        if doubt=='n' or doubt=='no':
            break
        elif doubt=='y' or doubt=='yes':
            if bet[1] in diceCount and diceCount[bet[1]]<bet[0]:
                print("You were right! There were only " + str(diceCount[bet[1]])+" "+str(bet[1])+'s\n')
                if currentPlayer==1:
                    deleteDice(numPlayers)
                else:
                    deleteDice((currentPlayer-1))
            else:
                if bet[1] in diceCount:
                    print('Wrong! There were ' + str(diceCount[bet[1]])+" "+str(bet[1])+'s')
                    print('You lose a die\n')
                    deleteDice(currentPlayer)
                else:
                    print("Right! There weren't any "+str(bet[1])+'s\n')
                    if currentPlayer==1:
                        deleteDice(numPlayers)
                    else:
                        deleteDice((currentPlayer-1))
            noDoubt=False
            x=False
        else:
            print("Please enter 'y' or 'n' ")

def randAIBet():                            # Function for Random AI Betting
    global bet
    u=bet
    while bet==u:
        compbetNum=random.randint(1,6)
        if compbetNum<=bet[1]:
            compbetQuant=bet[0]+1
        else:
            compbetQuant=bet[0]
        bet=[compbetQuant,compbetNum]
    return bet

def randAIDoubt():                              # Function for Player to doubt previous bet
    global noDoubt,diceList,currentPlayer
    doubt=random.randint(0,numPlayers)
    if doubt>0:
        return 0
    else:
        print("Computer player " + str(currentPlayer) + " doubts the previous bet")
        if bet[1] in diceCount and diceCount[bet[1]]<bet[0]:
            time.sleep(1.5)
            print("Computer player " + str(currentPlayer) + " was right. There were only " + str(diceCount[bet[1]])+" "+str(bet[1])+'s\n')
            print("Previous player loses a die")
            if currentPlayer==1:
                deleteDice(numPlayers)
            else:
                deleteDice((currentPlayer-1))
        elif bet[1] in diceCount:
            print('Wrong! There were ' + str(diceCount[bet[1]])+" "+str(bet[1])+'s')
            print("Computer player " + str(currentPlayer) +" loses a die\n")
            deleteDice(currentPlayer)
        else:
            print("Computer player " + str(currentPlayer) + " was right. There weren't any "+str(bet[1])+'s\n')
            print("Previous player loses a die")
            if currentPlayer==1:
                deleteDice(numPlayers)
            else:
                deleteDice((currentPlayer-1))
        noDoubt=False


                                                    # START OF MAIN PROGRAM LOOP

print("Welcome to Liar's Dice")                     # Intro
print("Are you prepared to lie?")

print("Please enter number of players")
while True:                                         #Defines starting number of players
    rawnumPlayers=input()
    if rawnumPlayers.isdecimal()==True:
        break
    else:
        print("Please enter a number")
numPlayers=int(rawnumPlayers)

print()
print("How many dice should each player start with?")
while True:                                           #Defines starting number of dice
    rawnumDice=input()
    if rawnumDice.isdecimal()==True:
        break
    else:
        print("Please enter a number")
numDice=int(rawnumDice)

print("\nGet ready for Liar's Dice with")               #Defines playerPosition, currentPlayer, and starting player
print((str(numPlayers)+' Players and').center(30))
print((str(numDice)+' Dice').center(30))
print()
playerPosition=random.randint(1,numPlayers)
currentPlayer=random.randint(1,numPlayers)
if currentPlayer==playerPosition:  #playerPosition=random.randint(1,numPlayers)
    print("You have been randomly selected to go first!")
else:
    print("Computer player "+str(currentPlayer)+" has been randomly selected to go first.\n")

stillPlayerDice=True                                    # Loop for each round including loss conditions
totalRounds=numDice*numPlayers
while stillPlayerDice==True:
    for round in range(1,((totalRounds)+1)):
        bet=[1,1]
        diceCount={}
        compileDiceList()
        countDice()
        checkLoss()
        if stillPlayerDice==False:
            print("Oh no! You are out of dice. You have lost the game")
            break
        else:
            print("Round "+str(round))
            print("There are " + str(totalDiceLeft) + " dice left")
            print("The starting bet is 1 1s\n")
            print("You have rolled: "+str(diceList[playerPosition])+'\n')


            noDoubt=True                                #loop for betting and checking doubt
            while noDoubt==True:
                if currentPlayer==playerPosition: #playerPosition=random.randint(1,numPlayers)
                    playerDoubt()
                    if noDoubt==False:
                        currentPlayer+=1
                        if currentPlayer>numPlayers:
                            currentPlayer=currentPlayer-numPlayers
                        break
                    else:
                        playerBet()
                    currentPlayer+=1
                elif currentPlayer<=numPlayers:
                    randAIDoubt()
                    if noDoubt==False:
                        currentPlayer+=1
                        if currentPlayer>numPlayers:
                            currentPlayer=currentPlayer-numPlayers
                        break
                    else:
                        randAIBet()
                    print('Computer player '+str(currentPlayer)+' has bet '+str(bet[0])+' '+str(bet[1]) + 's')
                    time.sleep(0.5)
                    currentPlayer+=1
                else:
                    currentPlayer=currentPlayer-numPlayers
