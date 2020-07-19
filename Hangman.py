#Intro: this code is designed to play hangman with the computer
##Date: 21/11/17
###Author: Manasi Mehta
import random
#####GLOBALS#############
LettersGuessed = ""
HangmanHead = " "
HangmanBody = "    "
HangmanLeg = "    "
Clue = ""
clues = ""
theWord = ""
maskWord = ""
livesleft = " "
#####FUNCTIONS############
def LoadDict():
    File = open("dictionary.txt","r")
    words = File.read().splitlines()
    return words

def BuildMan():
    Head = "  "
    Body = "    "
    Legs = "    "
    if (livesleft == 5):
        Head = " 0"
    elif (livesleft == 4):
        Head = " 0"
        Body = " |  "
    elif (livesleft == 3):
        Head = " 0"
        Body = "/|  "
    elif (livesleft == 2):
        Head = " 0"
        Body = "/|\\ "
    elif (livesleft == 1):
        Head = " 0"
        Body = "/|\\ "
        Legs = "/   "
    elif (livesleft == 0):
        Head = " 0"
        Body = "/|\\ "
        Legs = "/ \\ "
        print ("Sorry you have ran out of lives")
    return Head, Body, Legs

def DrawScreen():
    File = open("dictionary.txt","r")
    Words = File.read()
    words = len(Words.split(" "))
    print("__________________________________________________________________")
    print("|                                       |                        |")
    print("|                                       |                        |")
    print("|             H A N G M A N             |       178691 words     |")
    print("|                                       |                        |")
    print("|---------------------------------------|------------------------|")
    print("|                                       |   ____________________ |")
    print("| "+ MaskWord.ljust(26) +"            |   |/        |          |")
    print("|                                       |   |        " + HangmanHead + "          |")
    print("| Lives left: "+ str (livesleft) + "                         |   |        " + HangmanBody + "        |")
    print("| Clues left: "+ str (clues) +"                         |   |        " + HangmanLeg + "        |")
    print("|                                       |   |                    |")
    print("| Letters guessed: " + str(LettersGuessed.ljust(18)) + "   |   |\__________________ |") 
    print("|                                       |                        |")
    print("|_______________________________________|________________________|")
#####MAIN PROGRAM####################################################################################################
AllWords = LoadDict()
NoOfWords = len(AllWords)
TheWord = random.choice(AllWords)
MaskWord = "*" * len(TheWord)
LettersGuessed = " "
print ("Do you want to play hangman?")
playAgain = input("?")
while playAgain == "yes":
    playAgain1 = True
    Continues = True
    while Continues:
        print ("How many lives do you want?")
        print ("A: 4")
        print ("B: 5")
        print ("C: 6")
        livesLeft = input ("?")
        if livesLeft.lower() == "a":
            livesleft = 4
            Continues = False
        elif livesLeft.lower() == "b":
            livesleft = 5
            Continues = False
        elif livesLeft.lower() == "c":
            livesleft = 6
            Continues = False
        else:
            print ("I don't understand")
            Continues = True
            
        Continue = True
        while Continue:
            print ("How many clues do you want?")
            print ("A: 2")
            print ("B: 3")
            print ("C: 4 ")
            livesLeft = input ("?")
            if livesLeft.lower() == "a":
                clues = 2
                Continue = False
            elif livesLeft.lower() == "b":
                clues = 3
                Continue = False
            elif livesLeft.lower() == "c":
                clues = 4
                Continue = False
            else:
                print ("I don't understand")
                Continue = True
                
    gameOn = True
    while gameOn:
        HangmanHead, HangmanBody, HangmanLeg = BuildMan()
        DrawScreen()
        print ("""Please guess a letter.
You can type clue for a hint!
You can also type new for a new word!
If you know the word you can type it completly!""")
        userGuess = input ("?")
        userGuess = userGuess.upper()
        if (userGuess == "CLUE"):
            if clues == 0:
                print ("You have ran out of clues")
            else:
                clue = random.choice(TheWord)
                if (clue != LettersGuessed):
                    print ("Your clue is, in the word there is a " + clue)
                    pos =  -1
                    pos = TheWord.find(clue, pos + 1 )
                    MaskWord = MaskWord [0:pos] + clue + MaskWord [pos + 1 : len(MaskWord)]
                    LettersGuessed += clue
                    clues -= 1
                elif (clue == LettersGuessed):
                    clue = random.choice(TheWord)
                    print ("Your clue is, in the word there is a " + clue)
                    pos =  -1
                    pos = TheWord.find(clue, pos + 1 )
                    MaskWord = MaskWord [0:pos] + clue + MaskWord [pos + 1 : len(MaskWord)]
                    LettersGuessed += clue
                    clues -= 1
                
        elif (userGuess == TheWord):
            print ("You have guessed correctly!")
            pos =  -1
            MaskWord = MaskWord [0:pos] + TheWord
            play = True
        elif (userGuess == "NEW"):
            AllWord2 = LoadDict()
            NoOfWord2 = len(AllWord2)
            TheWord2 = random.choice(AllWord2)
            TheWord = TheWord2
            MaskWord2 = "*" * len(TheWord2)
            MaskWord = MaskWord2
            LettersGuessed2 = ""
            LettersGuessed = LettersGuessed2 
        elif(len(userGuess)> 1):
            print ("Pick only one letter")
        else: 
            if(LettersGuessed.find(userGuess) >= 0):
                print("Letter already guessed")
            else:
                LettersGuessed += userGuess
                pos =  -1
                if (TheWord.find(userGuess) >= 0):
                    while (TheWord.find(userGuess, pos + 1) >= 0 ):  
                        pos = TheWord.find(userGuess, pos + 1 )
                        MaskWord = MaskWord [0:pos] + userGuess + MaskWord [pos + 1 : len(MaskWord)]  
                        if (TheWord == MaskWord):
                            gameOn = False
                    print ("Well Done!")
                else:
                    livesleft -= 1
                    if livesleft == 0:
                        gameOn = False
                    print ("The letter you have entered is not the word!")
    HangmanHead, HangmanBody, HangmanLeg = BuildMan()
    DrawScreen()               
    if (livesleft == 0):
        print ("You lost, the word was " + TheWord)
    else:
        print ("You won! Well done!")
    print ("Do you want to continue?")
    PlayAgain = input ("?")
    play = True
    while play:
        if PlayAgain == "yes":
            AllWord = LoadDict()
            NoOfWord = len(AllWord)
            TheWord1 = random.choice(AllWord)
            TheWord = TheWord1
            MaskWords = "*" * len(TheWord1)
            MaskWord = MaskWords
            LettersGuesseds = ""
            LettersGuessed = LettersGuesseds
            play = False
            playAgain1 = True
            gameon = True
            
        elif PlayAgain == "no":
            print ("Ok bye!")
            play = False
            playAgain1 = False
            playAgain = False
            
        else:
            print ("I don't understand!")           
            play = False
if playAgain == "no":
    print ("Ok bye!")
    playAgain = False
