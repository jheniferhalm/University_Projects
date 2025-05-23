"""

Author: Jhenifer de Carvalho Halm
Purpose: W04 Project: Word Puzzle

In this Milestone Project I have added an introduction, prompting the user for their name so the game feels more personal.
Also added "{len(secret)}" in my hint section, in case I wanted to change my secret variable after creating my code.
"""

print()
print("Welcome to the Word Puzzle Game!")
your_name = input("Let me explain how the game works, first, can I get your name? ").strip().capitalize()
print()
print(f"Awesome, {your_name}, nice to meet you! \n\nThis is a word-guessing game where I initially picked a secret word for you to guess. \nThe word is hidden with blanks, and each time you guess, the game gives you a hint. \nIt shows which letters are correct and in the right spot, which are in the word but in the wrong spot, and which aren’t in the word at all. \nYou keep guessing until you get it right, and at the end, it tells you how many tries it took. ")
print()
print("Let's start!")
print()

secret = "helmet"
guess_count = 0
hint = ""
for letter in secret:
    hint += "_ "


print(f"Our secret word has {len(secret)} letters! {hint}")

while True:
    print()
    secret_guess = input("Can you guess the word? ").lower()
    guess_count += 1 # moved up, was a few lines down before
    if len(secret_guess) != len(secret):
        print(f"Your word needs to be {len(secret)} letters long. Let's try again!")
        continue


    if secret_guess == secret:
        if guess_count == 1:
            print()
            print("On your first try! Impressive! You have guessed it correctly and won the game!")
        else:
            print(f"\nYou have guessed the word! It took you {guess_count} tries!")
        break
    else:
        hint = ""
        for i in range(len(secret)):
            if secret_guess[i] == secret[i]:
                hint += secret_guess[i].upper() + " "
            elif secret_guess[i] in secret:
                hint += secret_guess[i].lower() + " "
            else:
                hint += "_" + " "                      
        print()
        print(f"Hint: {hint}")
        print()
        print("Your guess was not correct. Let's keep trying.")