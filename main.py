import random
import time

print("--- BR Rock Paper Scissors ---")
title = "\nRules:\n- Rock always beats Scissors\n- Scissors always beat Paper\n- Paper always beats Rock\n\n1 - Rock\n2 - Paper\n3 - Scissors\n"
letters = list(title)
for letter in letters:
    print(letter, end='', flush=True) 
    time.sleep(0.03) 

while True:
    bot = random.randint(1, 3)
    user = int(input("Enter a number from 1 to 3: "))

    if user == 1 and bot == 3:
        print("You WIN!👍")
    elif user == 3 and bot == 2:
        print("You WIN!👍")
    elif user == 2 and bot == 1:
        print("You WIN!👍")
    elif user == bot:
        print("Draw!🤝")
    elif user >= 4:
        print("The maximum number is 3!✋")
    else:
        print("You LOSE!👎")
input()

