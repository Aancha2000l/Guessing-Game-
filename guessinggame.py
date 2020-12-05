from random import randint

answer = randint(1, 10)

guess_count = 0
guess_limit = int(input("Number of chances you want: "))
out_of_guesses = False
while True:
    try:
       if guess_count<guess_limit:
           guess = int(input('guess a number from 1-10: '))
           guess_count += 1
           if 0 < int(guess) < 11:
               if guess == answer:
                   print("BRAVO!!!, You did it")
                   break
               else:
                   print("oops, try again")
                   continue
               pass
           else:
               print("Please enter the number between 1-10")
       else:
           print("Opps!!! You Lose. You are out of guesses.")
           break
    except ValueError as err:
        print(f'please enter a number{err}')
        continue
