class Board:
    def __init__(self, dim):
        self.dim = dim
        self.field = [[x for x in range(dim)] for y in range(dim)]
        self.initialize()
        self.ships=[]

    def initialize(self):
        for x in range(self.dim):
            for y in range(self.dim):
                self.field[x][y] = '-'

    def tryPlace(self, currentShip):
        # check if ship's coordinates don't overlap with other ship's ccords and vicinity
        for sPoint in currentShip.coords:
            for ship in self.ships:
                if sPoint in ship.coords or sPoint in ship.vicinity:
                    return False
        return True

    def drawShip(self, ship):
        # append ship to the list of ships on the board
        self.ships.append(ship)
        # draw the ship first
        for point in ship.coords:
            self.field[point[0]][point[1]] = str(ship.size)

        # draw ships vicinity now
        for point in ship.vicinity:
            if self.field[point[0]][point[1]] != "-":
                continue
            self.field[point[0]][point[1]] = "/"

    def shipHitCheck(self, x,y):
        for ship in self.ships:
            if [x,y] in ship.coords:
                hitIndex = ship.coords.index([x,y])
                ship.hitPoints.append([x,y])
                ship.status = "hit"
                del ship.coords[hitIndex]
                if len(ship.coords) == 0:
                    ship.status = "sunk"
                    return ["sunk",ship.hitPoints]
                return ["hit", [x,y]]
        return ["miss", []]

    # finish if necessary
    def getSunkShips(self):
        shipsSunk = {4:0, 3:0, 2:0, 1:0}
        for x in self.ships:
            if x.status == "sunk":
                shipsSunk[x.size] += 1
        return shipsSunk

    # helper method - printing stuff to stdout
    def showGrid(self):
        print("    " + "  ".join([str(x) for x in range(10)]))
        print()
        for x in range(self.dim):
            print(f'{x}   {"  ".join(self.field[x])}')
