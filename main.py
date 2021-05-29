from random import randint
game_running = True

def calculate_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)

print('Welcome to Monster Game!!')
while game_running == True:
  new_round = True
  player = {'name': 'Diana', 'attack': 10, 'heal': 16, 'health': 100}
  monster = {'name': 'Max', 'attack_min': 10, 'attack_max': 20, 'health': 100}

  while new_round == True:
  
    player_won = False
    monster_won = False

    print('Please select action')
    print('1) Attack')
    print('2) Heal')
    print('3) Exit Game')

    player_choice = input()

    if player_choice == '1':
      monster['health'] = monster['health'] - player['attack']
      if monster['health'] <= 0:
        player_won = True
        print('Player Won...')

      player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
      if player['health'] <= 0:
        monster_won = True
        print('Monster Won...')


    elif player_choice == '2':
      player['health'] = player['health'] + player['heal']
      
      player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])  
      if player['health'] <= 0:
        monster_won = True
        print('Monster Won...')


    elif player_choice == '3':
      new_round = False
      game_running = False

    else:
      print('Invalid Input')  

    print('Player heakth:' + str(player['health']))
    print('Monster heakth:' + str(monster['health'])) 

    # Adding exit condition should keep the game running untill either player or monste win the game (health of  either player  or monster equal to or smaller than zero). 
    if player_won == True or monster_won == True:
      new_round = False
