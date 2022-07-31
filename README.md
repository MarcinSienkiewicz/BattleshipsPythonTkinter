# Battleships #

##### *Wrote in Python and Tkinter* #####

### Requrements: ###
- no external libraries are needed
### Running the game ###
execute **battleships.pyw**
``` bash
python battleships.pyw
```
### About ###
The computer generates and randomly places ten 'ships' on the game board which is 10 by 10 squares. The ship's configuration (type) is also randomly selected. All you have to do is to find and 'sink' them by left-clicking the blue squares.
You have **22** attempts to do so. Ship 'hit' as well as sinking one does not decrement the number of attempts.

Said ships come in four different sizes:
- one ship taking up four squares
- two 'three-square' ships 
- three 'two-square' ships
- four 'one-square' ships

The squares that make up a ship have to be adjacent and share one side - they can't be placed diagonally.

If the ship is 'sunk' the game marks (in grey) adjacent squares that cannot hold another ship.

If the game is lost, the positions of the 'uncovered' ships are revealed.

For additional info, click in-game 'Help' button.
The help window is displayed by default on game startup. Tick the checkbox to disable it (the status of the help splash screen is saved in JSON file).
