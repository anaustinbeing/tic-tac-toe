# tic-tac-toe
This paper-and-pencil game can be played more interactively on your computer in two modes:
* Single player (Beat the computer).
* Two player.

**Rules for tic-tac-toe:**
* Players take turns putting their marks in empty squares.
* The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
* When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

**Introducing the interface:**
* A board (3x3) will be initially displayed showing the position of each squares.
* Selection of mode: 1. Single player 2. Two player.
* Type in the position where you need to place your X or O when your turn is up.

1. In single player mode, you will beat against computer. Suppose, you are X and computer is O. Part of your strategy is trying to figure out how to get continuous three Xs in a row or a column or a diagonal. The other part is trying to figure out how to stop the computer from getting there. After you put an X in a square, you start looking ahead. Where's the best place for your next X? You look at the empty squares and decide which ones are good choices—which ones might let you make three Xs in a row. You also have to watch where the computer puts its O. That could change what you do next. If the computer gets two Os in a row, you have to put your next X in the last empty square in that row, or the computer will win. 

2. In two player mode, you play against another player. The rules and strategies remain the same.
