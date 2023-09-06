import random

computer_list = ["rook","sassers","papper"]

# print(comput_rand_choice) for test

user_input = None

welcome_massage ="""


░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

- in papper rock sassers game -
- type exit or q to Quit the game -\n
"""

print(welcome_massage)

user_input = input("- pls choice from papper rock sassers?:  ").strip().lower()

while user_input != "exit" or user_input == "q":
    # computer choice from list random
    comput_rand_choice = random.choice(computer_list)
    if user_input == comput_rand_choice :
        print("- user:",user_input)
        print("- computer:",comput_rand_choice)
        print("- tie || draw -")
        play_again = input("do you want to play again(yes,no)?: ").strip().lower()
        if play_again == "yes":
            user_input = input("- pls choice from papper rock sassers?:  ").strip().lower()
        else:
            break
                
            
    elif user_input == "rock":
        if comput_rand_choice == "papper":
            print("- user:",user_input)
            print("- computer:",comput_rand_choice)
            print("- you loss -")
            play_again = input("do you want to play again(yes,no)?: ").strip().lower()
            if play_again == "yes":
                user_input = input("- pls choice from papper rock sassers?:  ").strip().lower()
            else:
                break
                                
        if comput_rand_choice == "sassers":
            print("- user:",user_input)
            print("- computer:",comput_rand_choice)
            print("- you win -")
            play_again = input("do you want to play again(yes,no)?: ").strip().lower()
            if play_again == "yes":
                user_input = input("- pls choice from papper rock sassers?:  ").strip().lower()
            else:
                break
                         
            
    elif user_input == "papper":
        if comput_rand_choice == "sassers":
            print("- user:",user_input)
            print("- computer:",comput_rand_choice)
            print("- you loss -")
            play_again = input("do you want to play again(yes,no)?: ").strip().lower()
            if play_again == "yes":
                user_input = input("- pls choice from papper rock sassers?:  ").strip().lower()
            else:
                break
                
            
        if comput_rand_choice == "rock":
            print("- user:",user_input)
            print("- computer:",comput_rand_choice)
            print("- you win -")
            play_again = input("do you want to play again(yes,no)?: ").strip().lower()
            if play_again == "yes":
                user_input = input("- pls choice from papper rock sassers?:  ").strip().lower()
            else:
                break
                

    elif user_input == "sassers":
        if comput_rand_choice == "rock":
            print("- user:",user_input)
            print("- computer:",comput_rand_choice)
            print("- you loss -")
            play_again = input("do you want to play again(yes,no)?: ").strip().lower()
            if play_again == "yes":
                user_input = input("- pls choice from papper rock sassers?:  ").strip().lower()
            else:
                break
                
            
        if comput_rand_choice == "papper":
            print("- user:",user_input)
            print("- computer:",comput_rand_choice)
            print("- you win -")
            play_again = input("do you want to play again(yes,no)?: ").strip().lower()
            if play_again == "yes":
                user_input = input("- pls choice from papper rock sassers?:  ").strip().lower()
            else:
                break
                
                
    if user_input not in computer_list:
        user_input = input("- pls choice from papper rock sassers?:  ").strip().lower()        
              
                
            
            
# leave the game
print("game closed")            