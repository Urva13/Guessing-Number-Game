import random
import pyfiglet
font = pyfiglet.figlet_format('Guess The Number')

EASY_LEVEL_ATTEMPT = 10
HARD_LEVEL_ATTMPT = 5

def set_difficulty(level_chosen):
    
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPT
    
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTMPT
    
    else:
        return
    
def check_answer(guessed_number,answer,attempts):
    
    if guessed_number<answer:
        print("Youe guess too low")
        return attempts-1
    
    elif guessed_number>answer:
        print("Youe guess too high")
        return attempts-1
    
    else:
        print(f"You guess is right... the answer was {answer}")
        
def game():
    print(font)
    print("let me think of a number 1 to 100.")
    
    answer = random.randint(1, 100)

    level = input("Choose level of difficulty ... Type 'easy' or 'hard':")

    attempts = set_difficulty(level)

    if attempts != EASY_LEVEL_ATTEMPT and attempts != HARD_LEVEL_ATTMPT:
    
        print("You have enetered wrong difficulty level...Play again!!")
    
    guessed_number = 0
    
    while guessed_number!=answer:
        
        print(f"Yoy have {attempts} attempts remaining to guess the number.")
        
        guessed_number = int(input("Guess a number:"))
        
        attempts = check_answer(guessed_number,answer,attempts)
        
        if attempts==0:
            print("You are out of guesses...You loose!")
            return
        
        elif guessed_number!=answer:
            print("Guess again")
game()