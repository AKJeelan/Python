guess_count = 0;
guess_limit = 3
secret = 9
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if(guess == secret):
        print("You win!")
        break
else:
    print("Sorry you are failed!")