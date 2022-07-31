import tkinter
import files.gui

def tryAgain(gameOver, root):
    root.destroy()
    gameOver.destroy()
    files.gui.restartGame("destroy", False)

def finishIt(gameOver, root):
    root.destroy()
    gameOver.destroy()

def endScreen(isWinner, root):
    def disableRootXButton():
        pass
    root.protocol("WM_DELETE_WINDOW", disableRootXButton)

    # disable restart and help buttons from the root window
    root.nametowidget('.!button102')['state'] = "disabled"
    root.nametowidget('.!button101')['state'] = "disabled"

    gameOver = tkinter.Tk()
    gameOver.iconbitmap("files/icons/gameOver.ico")
    gameOver.configure(bg="black")

    overWidth = 300
    overHeight = 200
    displayWidth = gameOver.winfo_screenwidth()
    displayHeight = gameOver.winfo_screenheight()
    centeredPosition = f"{overWidth}x{overHeight}+{int((displayWidth / 2 - overWidth / 2) - 7)}+" \
                       f"{int((displayHeight / 2 - overHeight / 2) - 36)}"
    gameOver.geometry(centeredPosition)
    gameOver.rowconfigure(index=0, weight=1)
    gameOver.rowconfigure(index=1, weight=1)
    gameOver.columnconfigure(index=0, weight=1)
    gameOver.columnconfigure(index=1, weight=1)


    gameOverText = f"You {isWinner.upper()}"
    gameOver.title("Game Over")
    if isWinner == "Won":
        gameFg = "green"
    elif isWinner == "Lost":
        gameFg = "red"
    loserLabel = tkinter.Label(gameOver, text=gameOverText, bg='black', fg=gameFg, font=("Code", 35, "bold"))
    loserLabel.grid(row=0,column=0, sticky=tkinter.NSEW, columnspan=2)
    bQuit = tkinter.Button(gameOver, text="Quit", command=lambda: finishIt(gameOver, root),
                           bg="white", font=("Code", 11), width=80, height=2)
    bAgain = tkinter.Button(gameOver, text="Try again", command=lambda: tryAgain(gameOver, root),
                            bg="white", font=("Code", 11), width=80, height=2)

    bQuit.grid(row=1, column=0, sticky=tkinter.S)
    bAgain.grid(row=1, column=1, sticky=tkinter.S)
    gameOver.mainloop()