import random
chosen_pokemon = input('¿Against which pokemon do you wanna fight?: (Squirtle / Charmander / Bulbasaur)').upper()

pikachu_life = 100
enemy_life = 0
pkm_attack_dmg = 0

if chosen_pokemon == "SQUIRTLE":
    enemy_life = 90
    pkm_name = 'Squirtle'
    pkm_attack_dmg = 8
elif chosen_pokemon == "CHARMANDER":
    enemy_life = 80
    pkm_name = 'Charmander'
    pkm_attack_dmg = 10
elif chosen_pokemon == "BULBASAUR":
    enemy_life= 100
    pkm_name = 'Bulbasaur'

while pikachu_life > 0 and enemy_life > 0:
    print('Choose a Move:')
    print('1)-Thunder Shock') #12 damage
    print('2)-Tail Whip')   #10 damage
    move_input = int(input())

    if move_input == 1:
        enemy_life -= 12
        print('Pikachu uses Thunder Shock and inflicts 12 points of damage')
        print('{}\'s Life = {}'.format(pkm_name,(enemy_life)).lower().capitalize())
        print('Pikachu\'s Life = {}'.format(pikachu_life))

    elif move_input == 2:
        enemy_life -= 10
        print('Pikachu uses Tail Whip and inflicts 10 points of damage')
        print('{}\'s Life = {}'.format(pkm_name, (enemy_life)).lower().capitalize())
        print('Pikachu\'s Life = {}'.format(pikachu_life))

    if pkm_name == 'Bulbasaur':
        bulbasaur_attack = random.randint(8,15)
        pikachu_life -= bulbasaur_attack
        print('{} attacks you and inflicts {} damage points'.format(pkm_name, bulbasaur_attack))
        print('{}\'s Life = {}'.format(pkm_name, (enemy_life)).lower().capitalize())
        print('Pikachu\'s Life = {}'.format(pikachu_life))
    else:
        print('{} attacks you and inflicts {} damage points'.format(pkm_name, pkm_attack_dmg))
        pikachu_life -= pkm_attack_dmg
        print('{}\'s Life = {}'.format(pkm_name, (enemy_life)).lower().capitalize())
        print('Pikachu\'s Life = {}'.format(pikachu_life))


print('Combat Finished.')
if pikachu_life <= 0:
    print('{} is the Winner'.format(pkm_name).lower().capitalize())
elif enemy_life <= 0:
    print('Pikachu is the Winner')

print('Combat has finished')