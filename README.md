# JanKenPo

- JanKenPo is a Python terminal game
- Users can try beat the computer chosing betweenn Rock Paper and Scissors
###
- The live link can be found here - [JanKenPo](https://junkenoo.herokuapp.com/) 


![Responsice Mockup](/assets/images/AmIResponsiveScrenshot.JPG)

## How to play 

JanKenPo is a classic Rock Paper and Scissors game. 
######
The user can play against the computer by inputting the values on the terminal. 
######
The game will tell the player immediatley when win , lose or draw.

## Features
####
#### Existing Features
<img alt="Welcome" src="/assets/images/WelcomeScreenshot.JPG" width="80%">

- Randon computer selection 
  - Once the player choose computer will make a ramdom selection 
   - The player will not be able to see that
####
- Example when the player win  

<img alt="Win" src="/assets/images/WinScreenshot.JPG" width="80%">

###

- Example when the player lose  

<img alt="Lose" src="/assets/images/LoseScreenshot.JPG" width="80%">

###

- Example when the player Draw 
  

<img alt="Draw" src="/assets/images/DrawScreenshot.JPG" width="80%">

###
- Play again 
  - When the game is finished the user will be prompeted to press 'r' to play again or 'q' to exit the game.
###
  <img alt="Draw" src="/assets/images/PlayAgainSceenshot.JPG" width="90%">

  ####
  - Exit game 
    - once the player press 'q' to exit it will be showed a banner and the game will finish.
    ####
      <img alt="Draw" src="/assets/images/quitScreenshot.JPG" width="90%">

      ####
- Input validation and error checking 
  - 1
<img alt="validation" src="/assets/images/.JPG" width="90%">

####

### Testing

I have tested the project doing the following

- passed on [PEP8](http://pep8online.com/).
- Tried invalid inputs 
- Tested on Heroku and the Terminal.

  #### Bugs

  Solved Bugs
 - Validation problem
 

  #### Remain Bugs

- No remain Bugs 

 #### Validator Testing 
 - [PEP8](http://pep8online.com/)
   - Initially found few errors that where fixed only 2 Warnings left
 #### Deployment 
- When you create the app, you will need to add two buildpacks from the Settings tab. The ordering is as follows:

   - heroku/python
    - heroku/nodejs
    - You must then create a Config Var called - PORT. Set this to 8000

    
  -  Connect your GitHub repository and deploy as normal.

  #### Credits

   - [W3Schools](https://www.w3schools.com/python/python_datetime.asp)
   - [Code Institute](https://www.CodeInstitute.net)
   - [Youtube](https://www.youtube.com/)
