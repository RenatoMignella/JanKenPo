#random imported to generate the random value 
import random

#pyfiglet imported to generate nice interface 
import pyfiglet

def welcome():
    # Print Welcome message
    banner = pyfiglet.figlet_format("JunKenPo")
    print(banner)

    print("Welcome to JunKenPo\n")
    print("Please chose betwin rock paper and scissors and challenge the Computer !!\n")
    print("Please type only lower case letters Exemple: paper , rock , scissors")

def game():
    """
    Input for the user chose and machine will ramdom chose as well 
    """
    player = input("The computer has chosen, It's your turn:\n")
    machine = random.choice(['rock', 'paper', 'scissors'])
    
    """
    Rules two equals draw 
    rock beats scissors , scissors beats paper , 
    and paper beats rock 
    """
             
    if player == machine:
        return 'Result is: Draw !'
              
    if win_game(player, machine):
        return 'Result is: You win congatulations !!'
    
    return 'Result is: You lost sorry..'
  

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
          print("Thank you for playng !")
          break
            
   
def main():
    """
    main function that will call all other ones 
    Ref love sandwichs project 
    """                 
welcome()           
game()
play_again()
      


print(main())
   