import random
chosen_pokemon = input('¿Against which pokemon do you wanna fight?: (Squirtle / Charmander / Bulbasaur)').upper()

pikachu_life = 100
enemy_life = 0

if chosen_pokemon == "SQUIRTLE":
    enemy_life = 90
elif chosen_pokemon == "CHARMANDER":
    enemy_life = 80
elif chosen_pokemon == "BULBASAUR":
    enemy_life= 100

while pikachu_life > 0 and enemy_life > 0:
    print('Choose a Move:')
    print('1)-Thunder Shock') #12 damage
    print('2)-Tail Whip')   #10 damage
    move_input = int(input())

    if move_input == 1:
        enemy_life -= 12
        print('Pikachu uses Thunder Shock and inflicts 12 points of damage')
        print('{}\'s Life = {}'.format(chosen_pokemon,(enemy_life)).lower().capitalize())
        print('Pikachu\'s Life = {}'.format(pikachu_life))

    elif move_input == 2:
        enemy_life -= 10
        print('Pikachu uses Tail Whip and inflicts 10 points of damage')
        print('{}\'s Life = {}'.format(chosen_pokemon, (enemy_life)).lower().capitalize())
        print('Pikachu\'s Life = {}'.format(pikachu_life))

    if chosen_pokemon == 'SQUIRTLE':
        print('Squirtle hits you and inflicts 8 damage points')
        pikachu_life -= 8
        print('{}\'s Life = {}'.format(chosen_pokemon, (enemy_life)).lower().capitalize())
        print('Pikachu\'s Life = {}'.format(pikachu_life))

    if chosen_pokemon == 'CHARMANDER':
        print('Charmander attacks you and inflicts 10 damage points')
        pikachu_life -= 10
        print('{}\'s Life = {}'.format(chosen_pokemon, (enemy_life)).lower().capitalize())
        print('Pikachu\'s Life = {}'.format(pikachu_life))
    if chosen_pokemon == 'BULBASAUR':
        random_damage_number = random.randint(8,12)
        print('Bulbasaur strikes you and inflicts {} points of damage'.format(random_damage_number))
        pikachu_life -= random_damage_number
        print('{}\'s Life = {}'.format(chosen_pokemon, (enemy_life)).lower().capitalize())
        print('Pikachu\'s Life = {}'.format(pikachu_life))

print('Combat Finished.')
if pikachu_life <= 0:
    print('Pikachu is the Winner')
elif enemy_life <= 0:
    print('{} is the Winner'.format(chosen_pokemon).lower().capitalize())