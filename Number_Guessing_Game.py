import random 

number = random.randint(1, 100)
attempts = 0 

print("Welcome to the Number Guessing Game! @Saad Shaikh")
print("I have picked a numberbetween 1 to 100. Try to guess it..!!")

while True:
    guess = int(input("Enter you guess: "))
    attempts += 1 

    if guess < number:
        print("Too low...!! Try Again")
    elif guess > number:
        print("Too High...!! Try Again")
    else: 
        print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
        break