import random

def show_title():
   title = '''
   _________         _________          ______   _______ 
   \__    _/|\     /|\__    _/|\     /|(  ___ \ (  ___  )
      )  (  | )   ( |   )  (  | )   ( || (   ) )| (   ) |
      |  |  | |   | |   |  |  | |   | || (__/ / | (___) |
      |  |  | |   | |   |  |  | |   | ||  __ (  |  ___  |
      |  |  | |   | |   |  |  | |   | || (  \ \ | (   ) |
   |\_)  )  | (___) ||\_)  )  | (___) || )___) )| )   ( |
   (____/   (_______)(____/   (_______)|/ \___/ |/     \|
                                                         
   _______           _______  _______ _________         
   (  ___  )|\     /|(  ____ \(  ____ \\__   __/         
   | (   ) || )   ( || (    \/| (    \/   ) (            
   | |   | || |   | || (__    | (_____    | |            
   | |   | || |   | ||  __)   (_____  )   | |            
   | | /\| || |   | || (            ) |   | |            
   | (_\ \ || (___) || (____/\/\____) |   | |            
   (____\/_)(_______)(_______/\_______)   )_(            
   '''
   print(title)
   print('You wake up feeling an unlimited amount of cuteness... OMG, you have been turned into Jujuba!')
   print('''
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢶⡶⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⣱⠋⠀⠘⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢶⡶⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⢁⡼⠁⠀⠀⠀⢻⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠈⠓⢄⠉⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠀⢠⠎⠀⠀⠀⠀⠀⠸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠙⢦⠀⠈⠛⢷⣤⡀⠀⣀⣠⣤⣴⡶⠶⠶⠶⠶⣶⣟⣁⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠑⢤⡀⢀⡨⠟⠛⠉⠉⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠉⠙⠲⢄⡀⠀⠀⠀⠀⠀⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⢀⡤⠟⠁⠀⠀⠀⠀⠀⠀⠀⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠹⡀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠈⢣⡀⣾⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⢀⡜⠁⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⡼⠀⠀⠳⡄⠀⢀⡴⠚⠉⠉⠉⠉⠓⢤⠀⠀⢹⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣀⡼⠀⠀⢠⠔⠋⠉⠀⢉⣙⠶⣄⣰⠃⠀⠀⠀⠙⣴⣿⠟⢿⣿⣷⣦⠀⠀⠀⢳⠀⠀⢿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠃⠀⢰⠋⠀⠀⣠⣾⣿⡏⠉⢻⡻⡄⠀⠀⠀⢠⠋⣷⣄⣤⣿⣿⣿⣧⠀⠀⢸⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣟⠀⠀⠀⣿⣿⣿⣷⣶⣾⡇⠹⡄⠀⠀⢼⠀⢻⡟⠛⠛⠋⣀⠇⠀⢀⡼⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠸⡄⠀⠀⠻⣈⠉⠉⢁⡽⠃⢰⠇⠀⠀⠈⠣⣄⠉⠓⠒⠊⢁⣠⣴⣊⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠙⠦⣄⣀⠈⠉⢋⣉⡠⠔⠋⠀⠙⠟⠁⠀⠀⠉⠉⢉⠉⠉⠁⠀⠊⠉⠑⠒⣾⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⢀⣠⠴⠊⠉⠉⠉⠉⢠⡀⠀⠀⠀⣠⠟⢤⣀⡀⢀⡰⠋⠀⠀⠀⠀⣌⠉⠉⣹⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣉⣠⠤⠖⠀⠀⠀⠀⠀⠙⠲⠶⠊⠁⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⢀⠈⠉⣷⠿⢴⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣄⣀⠴⠃⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⠾⣅⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠙⢦⣴⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠚⠁⣿⠀⠀⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⢀⡴⠋⠀⡽⠓⠲⠤⠤⠤⠤⠤⠤⠤⠤⠤⠔⠚⠋⠁⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⣀⠔⠁⠀⠰⡆⠀⠀⠀⠀⠀⠀⠈⠙⠒⡖⠚⠉⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⡟⠀⠀⠀⠀⢀⡠⠞⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀
⠀⠀⢀⣠⡶⠛⠉⢰⡧⠤⠴⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀
⠀⣰⠟⠉⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀
⣼⠏⠀⠀⠀⢠⡴⠶⣇⠀⠀⠀⠀⠀⠀⠀⣀⡤⠤⠤⠤⣀⢳⡀⣀⡤⠤⠤⠤⣄⡀⡇⣀⡤⠤⠤⠤⣄⣀⡿⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⢺⣀⢀⠘⣆⡀⣀⣀⣀⣠⡋⠁⢠⠀⢀⡀⠀⢹⡟⠁⠀⡄⠀⡀⠀⠙⡏⠁⢠⡀⠀⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀
⢻⡆⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠑⣼⣀⣸⣀⣀⣸⣇⣀⣀⣇⣀⣇⣀⣀⣇⣀⣘⣇⣀⣇⣀⣀⣼⠃⠀⠀⠀⠀⠀⠀
⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠻⢶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ''')
def start_mini_game():
   list_of_attributes = {'hp': 100, 'lv': 1, 'strength': 3, 'xp': 0, 'inventory':[], 'status':True}
   
   return list_of_attributes

def drawn_opponents(jujuba_lv):
   #opponents' list: [name, hp, strength, xp]
   mosquito = ['mosquito', 5,1,1]
   cockroach = ['cockroach',8,2,2]
   rat = ['rat', 10, 5, 10]
   fish = ['fish', 15, 3, 15]
   bird = ['bird', 20, 4, 20]
   chicken = ['chicken', 30, 7, 6, 30]
   snake = ['snake',50, 10, 50]
   
   
   
   if jujuba_lv < 5:
      opponent_drawn = random.choice([mosquito, cockroach])
   elif jujuba_lv < 10:
      opponent_drawn = random.choice([rat, fish, bird, chicken])
   else:
      opponent_drawn = snake
      
   
   return opponent_drawn

def game_over():
   print('You were a great Jujuba!')
   exit(0)
   
def attack(attacker_name, attacker_strengh, defender_name,defender_hp, defender_strengh):
   attacker_luck = random.randint(0,6)
   defender_luck = random.randint(0,6)
   
   if attacker_luck == 6:
      print(f'O {attacker_name} hit critical attack.')
   elif attacker_luck > 0:
      print(f'O {attacker_name} hit critical attack')
   else:
      print(f'O {attacker_name} missed the blow')
   
   damage = attacker_strengh*attacker_luck - defender_strengh*defender_luck
   
   if damage > 0:
      print(f'The {defender_name} suffered damage of {damage}')
      defender_hp -= damage
   else:
      print(f'The {defender_name} did not suffer any damage!')
   
   if defender_hp <= 0:
      print(f'The {defender_name} died!')
      return 0
   else:
      return defender_hp
   
   


show_title()
list_of_attributes = start_mini_game()
 
print(list_of_attributes)

opponent_drawn = drawn_opponents(1)
print(opponent_drawn)
game_over()