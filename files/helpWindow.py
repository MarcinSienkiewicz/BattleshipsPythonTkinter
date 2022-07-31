import tkinter
import json
from pathlib import Path

def settingsSplash(splashBox):
    with open("files/settings.json") as file:
        settingsRead = json.load(file)

    settingsRead['splash'] = not settingsRead['splash']
    with open("files/settings.json", 'w') as file:
        json.dump(obj=settingsRead, fp=file, indent=1)

def gameHelp():

    helpWindow = tkinter.Tk()
    helpWindow.iconbitmap("files/icons/question.ico")
    helpWindow.title("About")
    helpWindow.configure(bg='white')

    helpWidth = 620
    helpHeight = 470
    displayWidth = helpWindow.winfo_screenwidth()
    displayHeight = helpWindow.winfo_screenheight()
    centeredPosition = f"{helpWidth}x{helpHeight}+{int((displayWidth / 2 - helpWidth / 2) - 7)}+" \
                       f"{int((displayHeight / 2 - helpHeight / 2) - 36)}"

    helpWindow.geometry(centeredPosition)
    title = tkinter.Label(helpWindow, text="Game info", bg='white', font=("Code", 13, "bold"))
    title.grid(row=0, column=0)

    outerFrame = tkinter.Frame(helpWindow, bg='white')
    outerFrame.columnconfigure(index=0, weight=1)
    outerFrame.columnconfigure(index=1, weight=1)
    outerFrame.columnconfigure(index=2, weight=1)

    outerFrame.rowconfigure(index=0, weight=1)
    outerFrame.rowconfigure(index=1, weight=1)
    outerFrame.rowconfigure(index=2, weight=1)
    outerFrame.rowconfigure(index=3, weight=1)
    outerFrame.rowconfigure(index=4, weight=1)
    outerFrame.rowconfigure(index=5, weight=1)

    l1 = tkinter.Label(helpWindow)
    gameInfo = """The aim of the game is to 'sink' all TEN ships placed on the game board.\n
    Those are:
    ONE four-mast
    TWO three-mast
    THREE two-mast
    FOUR one-mast ships.\n    
    \nThe ship type, as well as the ship's position on the board are randomly generated. 

    One blue square represents one field on the game board. The board is 10x10 squares.
    In order to win the game, you need to 'hit' and then 'sink' all the ships.    

    You have TWENTY TWO attempts - hitting a ship or sinking one does not decrement the number of player's tries.
    \n
    Clicking a square on the game board results in one of three possible outcomes:   
    """


    contents = tkinter.Label(outerFrame, text=gameInfo, bg='white')

    outerFrame.grid(row=1, column=0)
    contents.grid(row=0, column=0, columnspan=3)
    miss = tkinter.Label(outerFrame, text=u"•", bg="#808b96")
    missText = tkinter.Label(outerFrame, text="Miss", bg="white", font=("TkDefaultFont",9,"bold"))
    miss.grid(row=1, column=0)
    missText.grid(row=2, column=0)

    hitText = tkinter.Label(outerFrame, text="Ship hit", bg="white", font=("TkDefaultFont",9,"bold"))
    hit = tkinter.Label(outerFrame, text=u"⛞", bg="#e67e22")
    hit.grid(row=1, column=1)
    hitText.grid(row=2, column=1)

    sunkText = tkinter.Label(outerFrame, text="Ship sunk", bg="white", font=("TkDefaultFont",9,"bold"))
    sunk = tkinter.Label(outerFrame, text=u"⛝", bg="#2ecc71")
    sunk.grid(row=1, column=2)
    sunkText.grid(row=2, column=2)


    vicinityText = tkinter.Label(outerFrame, text="""If the ship is sunk, the game will mark the ship's adjacent
fields - those are squares where other ships cannot be located.""", bg="white")
    vicinityText.grid(row=3, column=0, columnspan=3)

    uncoveredText = tkinter.Label(outerFrame,
                                  text="If the game is lost, position of the uncovered ships will be marked with:",
                                  bg="white", pady=5)
    uncoveredSymbol = tkinter.Label(outerFrame, text=u"⛴", bg='#FF0000', fg='black')

    uncoveredText.grid(row=4, column=0, columnspan=2, sticky="E")
    uncoveredSymbol.grid(row=4, column=2, sticky="W")

    # set checkbox according to json file
    splashValue = tkinter.IntVar()
    splash = tkinter.Checkbutton(outerFrame, text="Don't display this window again", bg="#F5F5F5", font=("Code",11),
                                 borderwidth=1, relief="ridge", command=lambda: settingsSplash(splash))
    splash.grid(row=5, column=0, sticky="E", padx=10, columnspan=2)
    with open("files/settings.json") as file:
        fromFile = json.load(file)

    if not fromFile['splash']:
        splash.select()
    else:
        splash.deselect()

    splashButton = tkinter.Button(outerFrame, text="Close", font=("Code", 11, "bold"),
                                  command=helpWindow.destroy, width=10)
    splashButton.grid(row=5, column=2, sticky="E", pady=10)
    # end test
    helpWindow.mainloop()