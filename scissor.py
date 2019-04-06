import sys
u1 = input("what's your name?")
u2 = input("and your name")
u1_answer = input("%s,do you want to choose rock,paper or scissors?"%u1)
u2_answer = input("%s,do you want to choose rock,paper or scissors?"%u2)

def compare(u1,u2):
    if u1 == u2:
        return("it's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("paper wins")
    elif u1 == 'scissors':
        if u2 =='paper':
            return("scissors win")
        else:
            return("Rock wins")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("paper wins!")
        else:
            return("scissors win!")
    else:
        return("Invalid input!You have not entered rock ,paper ,scissors,try again.")
    sys.exit()


print(compare(u1_answer,u2_answer))