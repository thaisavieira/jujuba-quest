import random

# Title and welcome
# Character creation
   ## HP: 100
   ## Level: 1
   ## Str: 3
   ## Exp: 0
   ## Inventory: 0
   ## Status: Alive
   
# Combat system
# Character progression
# Items and inventory

def title_screen_selections():
   option = input('>')
   if option.lower() == 'play':
      start_game()
   elif option.lower() == 'help':
      help_menu()
   elif option.lower() == 'quit':
      quit_game()
   else: 
      print('Type a valid command!')
      

def title_screen():
   print('######################################')
   print ('##### Welcome to Jujubas Quest! #####')
   print('######################################')
   print('              - Play -                ')
   print('              - Help -                ')
   print('              - Quit -                ')

title_screen()
#title_screen_selections()
