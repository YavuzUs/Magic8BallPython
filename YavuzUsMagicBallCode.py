#Yavuz Ata Us
#Magic 8 Ball Extra - Cred Assignment

from random import randint

def main():
    playagain = True
    notgiven = 0
    messageout = ("Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful", \
                 "As I see it, yes", "Most likely", "Outlook good", "Signs point to yes", "Yes", "It is certain", \
                 "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "Reply hazy, try again", \
                 "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again")
    messagecount = [0] * 20
    while playagain == True:
        print("Clear your mind and get ready for the Magic 8 Ball Experience!")
        print()
        input("Press ENTER key to shake the Magic Ball")
        magicChoice = randint(0, 19)
        print("The room starts shaking as the 8 Ball comes to a desicion!")
        print(f"Your desicion is {messageout[magicChoice]}")
        messagecount[magicChoice] = messagecount[magicChoice] + 1
        print(f"This desicion has been granted {messagecount[magicChoice]} times!")
        print()
        askuser = input("Would you like to ask the being another question? (Answer Y for yes, or N for no) : ")
        while askuser not in ("Y", "y", "N", "n"):
            print("This is not a valid entry, answer properly or get crushed!")
            askuser = input("Would you like to ask the being another question? (Answer Y for yes, or N for no) : ")
        if askuser == "Y":
            playagain = True
        elif askuser == "y":
            playagain = True
        elif askuser == "N":
            playagain = False
        elif askuser == "n":
            playagain = False


    print("Your questions have been answered! Quiver away before the ball crushes you!")
    print()
    print("The following judgements are yet to be given!")
    for notgiven in range (0,20):
        if messagecount[notgiven] == 0:
            print(f"{messageout[notgiven]}")
            notgiven = notgiven +1
        else:
            notgiven = notgiven +1
        


main()
