#random imported to generate the random value
import random
#pyfiglet imported to generate nice interface
import pyfiglet

def welcome():
    """Print Welcome message"""
    
    banner = pyfiglet.figlet_format("JanKenPo.")
    print(banner)

    print("Welcome to JanKenPo\n")
    print("Please choose betweenn rock paper and scissors and challenge the Computer !!\n")
    print("Please type only lower case letters Example: paper , rock , scissors\n")

def game():
    """
    Input for the user chose and machine will ramdom chose as well 
    and Rules: two equals draw rock beats scissors , scissors beats paper , 
    and paper beats rock
    """
    player = input("The computer has chosen, It's your turn:\n")
    machine = random.choice(['rock', 'paper', 'scissors'])
                 
    if player == machine:
        return 'Result is: Draw !'
              
    if win_game(player, machine):
        return 'Result is: You win congatulations !!'
    
    return 'Result is: You lost sorry..'
    
    # while True:
        
    #  if validade_input(player):
    #     print('deu certo')
    #     break

def win_game(player1, computer1):
    """
    It will return true if the player win 
    rock beats scissors , scissors beats paper , 
    and paper beats rock 
    """   
    if (player1 == 'rock' and computer1 == 'scissors') or \
        (player1 == 'scissors' and computer1 == 'paper')\
            or (player1 == 'paper' and computer1 == 'rock'):
                return True
               
def play_again():
    """
    function to define play again or exit 
    """
    
    while True:
      continu = input("To play again press'r', to finish press 'q'\n")
      if continu == 'r':
        print(game())
      else:
          banner2 = pyfiglet.figlet_format("Thank you for playng !")
          print(banner2)
          break
          
            
# def validade_input(player):
#     """
#     this function will validade all awnsers that the use input 
    
#     """
#     try:
        
#         if player != 'rock' and player != 'paper' and player !='scissors':
#            raise ValueError(
#                 f"you must to type paper , rock or scissors "
#             )
#     except ValueError as e:
#         print(f"invalid data: {e}, please try again .\n")
#         return False
        
#     return True  
    
    
   
def main():
    """
    main function that will call all other ones
    Ref love sandwichs project
    """                 
welcome()          
print(game())
play_again()
      


print(main())
   