import random
user_action=input("Enter a choice(rock, paper, scissor): ")
possible_action= ["rock", "paper","scissor"]

# use random.choice() to have the computer randomly select between the actions:

computer_action= random.choice(possible_action)

# Determine a Winner

if user_action==computer_action:
    print(f"both player selected {user_action}. Its a tie")
elif user_action== 'rock':
    if computer_action=="scissor":
        print("you win the game!! rock smashes scissor")
    else:
        print ("you lose!! rock cover paper!!")
elif user_action=='paper':
    if computer_action=='rock':
        print("you win!! paper cover rock!!")
    else:
        print("you lose!! scissor cuts paper")
elif user_action=='scissor':
    if computer_action=='paper':
        print("you win!! scissor cuts paper ")
    else:
        print("you lose!! rock smashes scissor")
    
