#random imported to generate the random value 
import random

def game():
    """
    Input for the user chose and machine will ramdom chose as well 
    """
    player = input("Please chose betwin rock , paper and scissors ")
    machine = random.choice(['rock', 'paper', 'scissors'])
    
    """
    Rules 
    two equals Draw 
    rock beats scissors , scissors beats paper , 
    and paper beats rock 
    """
    if player == machine:
        return "draw"
    