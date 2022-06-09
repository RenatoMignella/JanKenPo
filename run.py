#random imported to generate the random value 
import random

def game():
    """
    Input for the user chose and machine will ramdom chose as well 
    """
    player = input("Please chose betwin rock , paper and scissors ")
    machine = random.choice(['rock', 'paper', 'scissors'])
    