import random
number_to_guess = random.randint(1,10)
try_counter = 0


while (try_counter < 5):
    user_number = int(input('Adivina el numero: '))
    if user_number == number_to_guess:
        print('You Win!')
        exit()
    elif try_counter < 4:
        print('Try Again!')
        try_counter += 1
    elif try_counter == 4:
        print('You Lose :c')
        print('The number was: {}'.format(number_to_guess))
        try_counter += 1


