"""
def first_program():
    Current_year = 2026
    name = input("type username: ")
    age = int(input("type user's age: "))
    target_year = Current_year - age + 100
    print(f"{name} will turn 100 years in {target_year}")
first_program()

def second_program():
    num = int(input("type a number: "))
    check = int(input("type a number: "))
    if check % 2 == 0:
        print(f"{check} is an even number.")
    else:
        print(f"{check} is an odd number.")
    if check % 4 == 0:
        print(f"{check} is a multiple of 4")
    if check % num == 0:
        print(True)
    else:
        print(False)
second_program()

def third_program():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for r in a:
        if r < 5:
            b.append(r)
    print(b)
third_program()

def fourth_program():
    num = int(input("type number: "))
    x = range(1, num + 1)
    l = []
    for u in x:
        if u % num == 0:
            l.append(u)
    print(l)
fourth_program()

def fifth_program():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    d = []
    for r in a:
        if r in b:
            d.append(r)
    print(d)
fifth_program()

def sixth_program():
    user = input()
    if user == user[::-1]:
        print(user)
    else:
        print("not a palindrome!")
sixth_program()
 c  
def s_program():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = []
    for r in a:
        if r % 2 == 0:
            b.append(r)
    print(b)
s_program()

def e_program():
    while True:
        user1 = input("Rock, Paper, Scissors? ")
        user2 = input("Rock, Paper, Scissors? ")

        if user1 == "paper" and user2 == "rock":
            print("Player1 wins")
        elif user2 == "player" and user1 == "rock":
            print("Player2 wins")
        if user1 == "rock" and user2 == "scissors":
            print("Player1 wins")
        elif user2 == "rock" and user1 == "scissors":
            print("PLayer2 wins")
        if user1 == "scissors" and user2 == "paper":
            print("Player1 wins")
        elif user2 == "scissors" and user1 == "paper":
            print("PLayer2 wins")
        elif user1 == user2:
            print("Tied, Try again")

        next_round = input("Do you want to continue? Y/N   ")
        if next_round == "Y":
            continue
        else:
            break
e_program()

import random
def n_program():
    guess = random.randint(1, 9)

    while True:
        user = int(input("type number: "))
        if user == guess:
            print("Champion!")
        elif user < guess:
            print("Guess too low..")
        elif user > guess:
            print("Guess too high..")

        next_round = input("Do you want to continue? ")
        if next_round == "Yes":
            continue
        elif next_round == "exit":
            break
n_program()

def t_program():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    new = set(a)
    new1 = set(b)
    new.symmetric_difference(new1)
    print(list(new))
t_program()

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new = set(a)
new1 = set(b)
li = list(new)
li1 = list(new1)
new_list = []
for r in li:
    if r in li1:
        new_list.append(r)
print(new_list)

def ev_program():
    user = int(input("type a number: "))
    if user <= 1:
        print("not a prime number")

    is_prime = True
    for x in range(2, user):
        if user % x != 0:
            is_prime = False
            break
    if is_prime:
        print(f"{user} is a prime number.")
    else:
        print(f"{user} is not a prime number.")
ev_program()

def tw_program(number):
    new_list = []
    new_list.append(number[0])
    new_list.append(number[-1])
    print(new_list)
tw_program([5, 10, 15, 20, 25])

def fibonacci(n):
    a = 0
    b = 1
    for r in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

count = int(input("Enter the number of the sequence: "))
print("Your Fibonacci sequence:")
fibonacci(count)

def fw_program(lis):
    new_lis = []
    for r in lis:
        if r not in new_lis:
            new_lis.append(r)
    print(new_lis)
fw_program([11,22,3,3,4])

lis = [11,22,3,3,4]
n = set(lis)
new_list = list(n)
print(new_list)

try:
    num = int(input("type number: "))
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("zero")
except ValueError:
    print("not a number!")

def fw_program():
    words = input("type: ")
    word = words.split()
    print(word[::-1])
fw_program()

import random
def ff_games():
    numbers = random.randint(1000, 9999)
    guess = int(input("Guess the numbers? "))
    cows = 0
    bulls = 0
    print(numbers)
    for r in str(guess):
        if r not in str(numbers):
            cows += 1
    for s in str(numbers):
        if s != r:
            bulls += 1

    print(cows,bulls)
ff_games()




import random

def generate_secret_number():
    #Generates a random 4-digit number as a string.
    digits = random.choices("0123456789", k=4)
    return "".join(digits)

def check_guess(secret, guess):
    #Compares the secret number and the guess to count cows and bulls.
    cows = 0
    bulls = 0
    
    # We convert the strings to lists to easily cross off digits we've already counted
    secret_list = list(secret)
    guess_list = list(guess)
    
    # Step 1: Count Cows (Correct digit in the correct place)
    # We loop backwards so we can safely remove elements from the lists
    for i in range(3, -1, -1):
        if guess_list[i] == secret_list[i]:
            cows += 1
            # Remove them from lists so they aren't double-counted as bulls
            secret_list.pop(i)
            guess_list.pop(i)
            
    # Step 2: Count Bulls (Correct digit in the wrong place)
    for digit in guess_list:
        if digit in secret_list:
            bulls += 1
            # Remove from secret list so we don't match the same secret digit twice
            secret_list.remove(digit)
            
    return cows, bulls

def play_game():
    print("--- Welcome to Cows and Bulls! ---")
    print("I have generated a random 4-digit number.")
    print("Cow = Right digit in the right place.")
    print("Bull = Right digit in the wrong place.\n")
    
    secret_number = generate_secret_number()
    guess_count = 0
    print(secret_number)
    # Loop continuously until the user guesses the number
    while True:
        guess = input("Guess a 4-digit number: ")
        
        # Simple input validation
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter exactly 4 numbers.")
            continue
            
        guess_count += 1
        
        # Check cows and bulls
        cows, bulls = check_guess(secret_number, guess)
        
        # Win condition
        if cows == 4:
            print(f"\n🎉 Congratulations! You guessed the correct number: {secret_number}")
            print(f"It took you {guess_count} guesses.")
            break
        else:
            print(f"Result: {cows} Cows, {bulls} Bulls\n")

# Start the game
if __name__ == "__main__":
    play_game()

def tw_program(lis, number):
    if number not in lis:
        return False
    else:
        return False
result = tw_program([0,1,2,3,4,5], 3)
print(result)


filename = input("Enter the name of your file: ")
print("-------Writing to the file-------")
with open(filename, "w") as file:
    file.write("This is the very first line of my file.\n")
print(f"Created {filename} and wrote the first line")


print("------Appending to the file------")
user_line = input("Type second sentence to add to a file: ")
with open(filename, "a") as file:
    file.write(user_line + "\n")
print("Added successfully")


print("-------Reading the file------")
print(f"OPening the {filename} to read your changes")
with open(filename, "r") as file:
    content = file.read()
    print("---File contents---")
    print(content)
    print("--------------------")

def draw_board(size):
    for _ in range(size):
        print(" ---" *size)
        print("|   "* (size) + "|")

    print(" ---" * size)
board_size = int(input("What size game board would you like to draw? "))
draw_board(board_size)

def guessing_game2():
    user_secret_number = int(input("What is your secret number? "))
    
    low = 0
    high = 100
    guesses = 0

    while True:
        # Instead of random, guess the exact middle between low and high
        computer_guess = (low + high) // 2
        guesses += 1
        print(f"Computer guesses: {computer_guess}")

        if computer_guess == user_secret_number:
            print(f"Computer won in {guesses} tries!")
            break
        elif computer_guess < user_secret_number:
            print("Guess too low..\n")
            low = computer_guess + 1  # Raise the lowest possible boundary
        elif computer_guess > user_secret_number:
            print("Guess too high..\n")
            high = computer_guess - 1  # Lower the highest possible boundary

guessing_game2()

def te_program():
    num1 = int(input("type number: "))
    num2 = int(input("type number: "))
    num3 = int(input("type number: "))

    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)
te_program()    

import random

def get_random_sowpods_word(filename="sowpods.txt"):
    #Reads the SOWPODS word file and returns a single uppercase word at random.
    with open(filename, "r") as file:
        # Read lines, strip whitespace/newlines, and keep non-empty words
        words = [line.strip
        words = random.choice(new)() for line in file if line.strip()]
    
    # Pick and return a random word from the list
    return random.choice(words)

if __name__ == "__main__":
    secret_word = get_random_sowpods_word()
    print(f"Random SOWPODS word selected: {secret_word}")


def play_hangman(secret_word):
    secret_word = secret_word.upper()
    guessed_letters = set()
    
    print("Welcome to Hangman!")
    
    while True:
        # Build the visual clue (e.g., "E V _ P O R _ T E")
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("\nWord: " + " ".join(display_word))
        
        # Check if all letters have been revealed
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly!")
            break
            
        guess = input("Guess a letter: ").strip().upper()
        
        # Validate input length and type
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        # Bonus: Check if the letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter!")
        else:
            guessed_letters.add(guess)
            if guess in secret_word:
                print(f"Good job! '{guess}' is in the word.")
            else:
                print(f"Sorry, '{guess}' is not in the word.")

if __name__ == "__main__":
    # Test with "EVAPORATE" as specified in the exercise
    play_hangman("EVAPORATE")
"""

# Binary Search Trees
class Node:
    def __init__(self, price):
        self.price = price
        self.left = None
        self.right = None

    
def insert(node, price):
        if node is None:
            return Node(price)
        if price < node.price:
            node.left = insert(node.left, price)
        elif price > node.price:
             node.right = insert(node.right, price)

        return node

def search(node, target):
  # Base case: if node is None or we found the target
  if node is None or node.price == target:
    return node

  # If target is smaller, search left
  if target < node.price:
    return search(node.left, target)

  # Otherwise, search right
  return search(node.right, target)

miracle = Node(4.50)
insert(miracle, 3.00)
insert(miracle, 5.00)
insert(miracle, 6.00)
insert(miracle, 1.50)

# Search for 6.00 (Exists)
find = search(miracle, 6.00)
if find:
    print(f"Found price: {find.price}")  # Accessing the .price attribute!
else:
    print("Price not found.")

# Search for 9.99 (Does not exist)
find2 = search(miracle, 9.99)
if find2:
    print(f"Found price: {find2.price}")
else:
    print("Price 9.99 not found in the tree.")
    s= 2