import random
import pwinput


def gamevscomp():
    personchoice = input("Please enter your choice from Rock/Paper/Scissors\n")
    if personchoice != "Rock" and personchoice != "Paper" and personchoice != "Scissors":
        print("\nPlease enter a valid choice")
        result = -1
    else:
        compchoice = random.choice(["Rock", "Paper", "Scissors"])
        print("\nComputer has chosen " + str(compchoice))
        if personchoice == "Rock":
            if compchoice == "Paper":
                result = 1
            elif compchoice == "Scissors":
                result = 2
            else:
                result = 0
                print("\nIt is a tie. Kindly provide your choices again.\n")
        elif personchoice == "Paper":
            if compchoice == "Scissors":
                result = 1
            elif compchoice == "Rock":
                result = 2
            else:
                result = 0
                print("\nIt is a tie. Kindly provide your choices again.\n")
        else:
            if compchoice == "Rock":
                result = 1
            elif compchoice == "Paper":
                result = 2
            else:
                result = 0
                print("\nIt is a tie. Kindly provide your choices again.\n")

    while int(result) <= 0:
        result = gamevscomp()
    return result


def gamevsplayer(p1, p2):
    print(str(p1)+",plase enter your choice from Rock/Paper/Scissors\n")
    p1choice = pwinput.pwinput(prompt="Choice: ", mask=" ")
    print(str(p2) + ",please enter your choice from Rock/Paper/Scissors\n")
    p2choice = pwinput.pwinput(prompt="Choice: ", mask=" ")
    if (p1choice != "Rock" and p1choice != "Paper" and p1choice != "Scissors") or (p2choice != "Rock" and p2choice != "Paper" and p2choice != "Scissors"):
        print("\nPlease enter a valid choice")
        result = -1
    else:
        print("\n" + str(p1) + " has chosen " + str(p1choice) + "\n" + str(p2) + " has chosen " + str(p2choice))
        if p2choice == "Rock":
            if p1choice == "Paper":
                result = 1
            elif p1choice == "Scissors":
                result = 2
            else:
                result = 0
                print("\nIt is a tie. Kindly provide your choices again.\n")
        elif p2choice == "Paper":
            if p1choice == "Scissors":
                result = 1
            elif p1choice == "Rock":
                result = 2
            else:
                result = 0
                print("\nIt is a tie. Kindly provide your choices again.\n")
        else:
            if p1choice == "Rock":
                result = 1
            elif p1choice == "Paper":
                result = 2
            else:
                result = 0
                print("\nIt is a tie. Kindly provide your choices again.\n")

    while int(result) <= 0:
        result = gamevsplayer(p1, p2)
    return result


print("Welcome to Rock-Paper_Scissors game")
vswho = input("Press 1 for a game against computer\nPress 2 for a game against another player\nPress 0 to exit the game\nKindly provide your choice\n")
while int(vswho) != 0:
    gametype = input("Press 1 for quick game\nPress any other digit 'n' for a n-round game\nKindly provide yor choice\n")
    if int(vswho) == 1:
        if int(gametype) == 0:
            winner = gamevscomp()
            if int(winner) == 1:
                print("\nYou Lost! Computer has won the game")
            else:
                print("\nCongratulations, You Win!")
        else:
            comp = 0
            player = 0
            for i in range(int(gametype)):
                winner = gamevscomp()
                if int(winner) == 1:
                    comp += 1
                    print("\nYou Lost! Computer has won the game")
                else:
                    player += 1
                    print("\nCongratulations, You Win!")
            print("\nComputer : "+str(comp)+"\nPlayer : "+str(player))
            if comp>player:
                print("\nYou Lost! Computer has won the set game")
            elif player>comp:
                print("\nCongratulations, you win the set game!")
            else:
                print("\nOops, it is a tie.")
    else:
        player1 = input("First Player, kindly enter your name\n")
        player2 = input("Second Player, kindly enter your name\n")
        if int(gametype) == 0:
            winner = gamevsplayer(player1, player2)
            if int(winner) == 1:
                print("\n"+str(player1)+" has won the game")
            else:
                print("\n"+str(player2)+" has won the game")
        else:
            p1 = 0
            p2 = 0
            for i in range(int(gametype)):
                winner = gamevsplayer(player1, player2)
                if int(winner) == 1:
                    p1 += 1
                    print("\n"+str(player1)+" has won the game")
                else:
                    p2 += 1
                    print("\n"+str(player2)+" has won the game")
            print(str(player1)+" : "+str(p1)+"\n"+str(player2)+" : "+str(p2))
            if p1 > p2:
                print("\n" + str(player1) + " has won the set game")
            elif p2 > p1:
                print("\n" + str(player2) + " has won the set game")
            else:
                print("\nOops, it is a tie.")
    vswho = input("\nPress 1 for a game against computer\nPress 2 for a game against another player\nPress 0 to exit the game\nKindly provide your choice\n")
print("\nThanks for playing the game. Have a nice day")


