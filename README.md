# Blackjack-Python-Exam
<img width="705" alt="Screenshot 2019-07-31 at 11 28 43" src="https://user-images.githubusercontent.com/36447407/62200921-a9f66e80-b386-11e9-9e57-6e66097b03db.png">

## Assignment Solution
The assignment was to develop a console application of the card game Blackjack
* The game should be terminal based (text based), with no gui implementation
* The game should be single player game. One player against the computer
* The player should be able to choose if he or she wants to be a player or a dealer
* A bet functionality should be implemented

## To run the Blackjack game you must clone the repository or download it as zip
`git clone https://github.com/lass5643/Blackjack-Python-Exam.git`
1. After cloning/downloading the game, move to the folder `Blackjack-Python-Exam` in your terminal
2. To run the game, enter this command: `python3 blackjack.py`
3. Play the game by following the instructions on screen
4. Tests can be run by entering the command: `python3 unittests.py`

### Gameplay
* **When the game is launched, you will be prompted for your desired display name**
  * This will be used to differentiate you from the computer
* **Enter the amount you would like to deposit to your account**
  * This may only be a whole number.
* **Decide if you want to play as the Player or the Dealer**
  * Enter '1' for Player and '2' for Dealer
* **Gameplay as the Player**
  * Enter the amount you would like to bet
    * Only takes a whole number and may not be greater than your balance.
  * Choose 'Hit' or 'Stand' based on yours and the dealer's cards
  * The dealer will always stand on 17, 18, 19, 20, 21 (S17)
  * After the game, your balance will be updated accordingly
  * Choose if you would like to play again by entering 'y' or 'n'
* **Gameplay as the Dealer**
  * Enter the amount you would like to bet
    * Only takes a whole number and may not be greater than your balance.
  * The computer will automatically run their turn
    * The computer will hit on 4-15 and stand on 16-21
  * If the player busts you have won the game without doing anything! (House edge wohoo)
  * If the player **DOES NOT BUST** you will get to play your turn
  * You will automatically stand on 17, 18, 19, 20, 21
  * After the game, your balance will be updated accordingly
  * Choose if you would like to play again by entering 'y' or 'n'
