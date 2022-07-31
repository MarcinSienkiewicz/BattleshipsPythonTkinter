import files.gui
import files.ship
import files.board
import files.helpWindow
import random
from pathlib import Path
import json

def startGame():
    # 'about game' splash screen on startup checkbutton
    settingsFile = "files/settings.json"
    with open(settingsFile) as file:
        splashStatus = json.load(file)['splash']
    if splashStatus:
        files.helpWindow.gameHelp()

    files.gameField = files.board.Board(10)
    counter = 1
    for sSize in range(len(files.ship.models),0,-1):
        for _ in range(counter):
            while True:
                s = files.ship.Ship(sSize)
                s.calculateCoords()
                placedOk = files.gameField.tryPlace(s)
                if placedOk:
                    if s.size == 1:
                        del s.coords[0]
                    files.gameField.drawShip(s)
                    break
        counter += 1
    # display grid with placed ships
    # gameField.showGrid()
    return files.gameField

if __name__ == "__main__":
    gameField = startGame()
    files.gui.makeGui(files.gameField)

