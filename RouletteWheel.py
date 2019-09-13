from random import randint

amount = 1000
print("\nYour Total amount is " + str(amount) + "\n")
bet = 0
Game = True

while(Game != False):
    number = randint(0, 49)

    check = input("You Want To play this game Y or N \n")

    if(check == "N" or check == "n"):
        Game = False
        print("Good Bye ! ")

    else:
        BetNumber = int(input("\nEnter a number which you want to bet \n"))

        if (BetNumber >= 0 and BetNumber < 50):
            BetAmount = int(input("\nEnter a amount which you want to bet \n"))

            if(BetAmount>0):

                if (amount >= BetAmount):

                    if (number == BetNumber):
                        print("\n***********ooooooohhhhhhhhhh Great You wonnnnnnn this match ******************")
                        amount *= 50
                        print("\nGreat your amount is " + str(amount))

                    else:
                        print("\nOppse the number is \n" + str(number))
                        print("\nYou lose the game \n")
                        amount -= BetAmount
                        print("Your Remaining amount is = " + str(amount) + "\n")

                else:
                    print("You have not sufficient amount to play this game \n Try again later \n")
                    Game = False
            else:
                print("\nPlease Enter a real amount\n")

        else:
            print("Please Choose a number between 0 to 49 \n")
