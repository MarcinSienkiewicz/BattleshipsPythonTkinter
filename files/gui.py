import tkinter
import files.gameEnd
import files.helpWindow
import battleships

buttonsCreated = [[x for x in range(10)] for x in range(10)]
shipStatusesFrame = {4: {'label': "", 'total': 1, 'sunk': 0}, 3: {'label': "", 'total': 2, 'sunk': 0},
                         2: {'label': "", 'total': 3, 'sunk': 0}, 1: {'label': "", 'total': 4, 'sunk': 0}}
attemptsLeft = {'label': "", 'number':22}

def buttonPress(b, gameField, root):
    global attemptsLeft
    row = b[0]
    column = b[1]
    status = gameField.shipHitCheck(row, column) # hit; miss; sunk
    if status[0] == "miss":
        buttonsCreated[row][column].configure(text=u"•",bg="#808b96", state="disabled", fg='white')
        attemptsLeft['number'] -= 1
        bgAttempts = "SystemButtonFace"
        colorAttempts = 'green'
        if attemptsLeft['number'] < 6:
            colorAttempts = 'white'
            bgAttempts = "red"
        elif attemptsLeft['number'] < 11:
            colorAttempts = 'orange'
        attemptsLeft['label'].configure(text=attemptsLeft['number'], fg = colorAttempts, bg=bgAttempts)
    elif status[0] == "hit":
        buttonsCreated[row][column].configure(text=u"⛞",bg="#e67e22", state="disabled")
    elif status[0] == "sunk":
        for point in status[1]:
            buttonsCreated[point[0]][point[1]].configure(text=u"⛝",bg="#2ecc71", state="disabled")

        # mark ships vicinity with 'miss' - other ships can't be here
        hitPoint = [row, column]
        for sunkShip in gameField.ships:
            if hitPoint in sunkShip.hitPoints:
                for vPoint in sunkShip.vicinity:
                    buttonsCreated[vPoint[0]][vPoint[1]].configure(text=u"•",
                                                                   bg="#808b96", state="disabled", fg='white')


    # no ships on field update
    sunk = gameField.getSunkShips()
    for x,y in sunk.items():
        shipStatusesFrame[x]['sunk'] = y
        shipStatusesFrame[x]['label'].configure(text=shipStatusesFrame[x]['total']-shipStatusesFrame[x]['sunk'])
        if shipStatusesFrame[x]['sunk']==shipStatusesFrame[x]['total']:
            shipStatusesFrame[x]['label'].configure(bg="#2ecc71")

    # win check and win screen
    noTypes = 4
    winCheck = 0
    for key, value in shipStatusesFrame.items():
        if value['total'] == value['sunk']:
            winCheck += 1
    if winCheck == 4:
        for row in range(10):
            for column in range(10):
                buttonsCreated[row][column].configure(state="disabled")
        files.gameEnd.endScreen("Won", root)

    # lost check and lost screen
    if attemptsLeft['number'] < 1:
        for row in range(10):
            for column in range(10):
                buttonsCreated[row][column].configure(state="disabled")

        # uncover ships that player didn't sink here
        for ship in gameField.ships:
            if len(ship.coords) > 0:
                for coord in ship.coords:
                    buttonsCreated[coord[0]][coord[1]].configure(bg="#FF0000", fg="black", text=u"⛴")
        #
        files.gameEnd.endScreen("Lost", root)

def makeGui(gameField):

    # root - main window
    root = tkinter.Tk()
    root.iconbitmap('files/icons/ship.ico')

    rootWidth = 350
    rootHeight = 400
    displayWidth = root.winfo_screenwidth()
    displayHeight = root.winfo_screenheight()
    centeredPosition = f"{rootWidth}x{rootHeight}+{int((displayWidth / 2 - rootWidth / 2) - 7)}+" \
                       f"{int((displayHeight / 2 - rootHeight / 2) - 36)}"
    root.geometry(centeredPosition)
    root.title("Battleships")

    # display ship hit statuses
    statusLabel = tkinter.Label(root,text="Ships remaining on field", font=("Code", 15))
    statusFrame = tkinter.Frame(root)

    for x in range(10):
        root.columnconfigure(index=x, weight=1)
        root.rowconfigure(index=x, weight=1)

    # one extra for destroyed ships
    root.rowconfigure(index=10, weight=1)

    # make buttons - gamefiled
    for row in range(10):
        for column in range(10):
            p = tkinter.Button(root, text="", bg="#85c1e9", fg="#85c1e9",
                               command=lambda press=[row,column]:buttonPress(press, gameField, root),width=10)
            p.grid(row=row, column=column, sticky="NWSE")
            buttonsCreated[row][column] = p

    #  ships status bit
    statusLabel.grid(row=10, column=0, columnspan=10)
    s4Label = tkinter.Label(root, text="Four-mast")
    s4Qty = tkinter.Label(root, text=shipStatusesFrame[4]['total']-shipStatusesFrame[4]['sunk'], background='orange', width=3, borderwidth=2, relief="groove")
    shipStatusesFrame[4]['label'] = s4Qty

    s3Label = tkinter.Label(root, text="Three-mast")
    s3Qty = tkinter.Label(root, text=shipStatusesFrame[3]['total']-shipStatusesFrame[3]['sunk'], background='orange', width=3, borderwidth=2, relief="groove")
    shipStatusesFrame[3]['label'] = s3Qty

    s2Label = tkinter.Label(root, text="Two-mast", pady=5)
    s2Qty = tkinter.Label(root, text=shipStatusesFrame[2]['total']-shipStatusesFrame[2]['sunk'], background='orange', width=3, borderwidth=2, relief="groove")
    shipStatusesFrame[2]['label'] = s2Qty

    s1Label = tkinter.Label(root, text="One-mast")
    s1Qty = tkinter.Label(root, text=shipStatusesFrame[1]['total']-shipStatusesFrame[1]['sunk'], background='orange', width=3, borderwidth=2, relief="groove")
    shipStatusesFrame[1]['label'] = s1Qty

    s4Label.grid(row=11, column=0, columnspan=3,sticky="E")
    shipStatusesFrame[4]['label'].grid(row=11, column=3)

    s3Label.grid(row=11, column=4, columnspan=3,sticky="E")
    shipStatusesFrame[3]['label'].grid(row=11, column=7)

    s2Label.grid(row=12, column=0, columnspan=3, sticky="E")
    shipStatusesFrame[2]['label'].grid(row=12, column=3)

    s1Label.grid(row=12, column=4, columnspan=3, sticky="E")
    shipStatusesFrame[1]['label'].grid(row=12, column=7)

    # moves left
    movesLeftLabel = tkinter.Label(root, text="Attempts left:", font=("Code", 12))
    movesLeftLabel.grid(row=13, column=0, columnspan=9)
    movesLeftNumber = tkinter.Label(root, text=attemptsLeft['number'], font=("Code", 12, "bold"), fg='green')
    attemptsLeft['label'] = movesLeftNumber
    movesLeftNumber.grid(row=13, column=6)

    # restart game and help buttons
    restartButton = tkinter.Button(root, text = "Restart game", borderwidth=2, height=2,
                                   bg="#D8D8D8", command=lambda: restartGame(root, True))
    helpButton = tkinter.Button(root, text = "Help", bg="#D8D8D8", height=2,command=files.helpWindow.gameHelp)
    restartButton.grid(row=14, column=0, columnspan=5,sticky="EW")
    helpButton.grid(row=14, column=5, columnspan=5, sticky="EW")

    root.mainloop()

def restartGame(rootWindow, flag):
    global shipStatusesFrame, attemptsLeft
    if flag == True:
        rootWindow.destroy()

    shipStatusesFrame = {4: {'label': "", 'total': 1, 'sunk': 0}, 3: {'label': "", 'total': 2, 'sunk': 0},
                         2: {'label': "", 'total': 3, 'sunk': 0}, 1: {'label': "", 'total': 4, 'sunk': 0}}
    attemptsLeft['number'] = 22
    gameField = battleships.startGame()

    makeGui(gameField)
