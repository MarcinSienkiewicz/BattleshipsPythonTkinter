import random

# position as offsets (x, y) to randomally generated ship's start point
models = {1: [[[0, 0]]],
          2: [[[1, 0]], [[0, 1]]],
          3: [[[1, 0], [2, 0]], [[0, 1], [0, 2]], [[1, 0], [1, 1]], [[1, 0], [0, 1]],
                     [[-1, 1], [0, 1]], [[0, 1], [1, 1]]],
          4: [[[1, 0], [2, 0], [3, 0]], [[0, 1], [0, 2], [0, 3]], [[1, 0], [2, 0], [0, 1]],
                     [[1, 0], [0, 1], [1, 1]], [[1, 0], [2, 0], [2, 1]], [[1, 0], [-1, 1], [0, 1]],
                     [[1, 0], [1, 1], [2, 1]], [[-1, 1], [0, 1], [-1, 2]], [[0, 1], [1, 1], [1, 2]],
                     [[1, 0], [2, 0], [1, 1]], [[-1, 1], [0, 1], [0, 2]], [[0, 1], [1, 1], [0, 2]],
                     [[-1, 1], [0, 1], [1, 1]], [[-2, 1], [-1, 1], [0, 1]], [[0, 1], [1, 1], [2, 1]]]}

pointVicinity = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]

class Ship:
    def __init__(self, size):
        self.size = size  # how many fields occupy
        self.status = 'ok'  # ok, hit, sunk
        self.chosen = random.randint(0,len(models[self.size])-1)  # model from 'size' selected
        self.coords = []
        self.vicinity = []

    def getStartPoint(self):
        return [random.randint(0,9) for _ in range(2)]

    def calculateVicinity(self):
        tmpV = []
        for p in self.coords:
            for x in pointVicinity:
                xtmp = p[0]+x[0]
                ytmp = p[1] + x[1]
                if xtmp < 0 or xtmp > 9 or ytmp<0 or ytmp > 9:
                    continue
                else:
                    tmpPoint = [xtmp, ytmp]
                    if tmpPoint in self.coords or tmpPoint in tmpV:
                        continue
                    else:
                        tmpV.append([xtmp, ytmp])
        for x in tmpV:
            self.vicinity=[[p[0], p[1]] for p in tmpV]

    def calculateCoords(self):
        while True:
            createdFlag = True
            startPoint = self.getStartPoint()
            tmpCoords = []  # will be moved to coords if within the game board
            for x in models[self.size][self.chosen]:
                tmpCoords.append([startPoint[0] + x[0], startPoint[1] + x[1]])
            tmpCoords.insert(0, startPoint)

            # does the ship fit on board - check
            for x in tmpCoords:
                if x[0] < 0 or x[0] > 9 or x[1] < 0 or x[1] > 9:
                    # print("NOPE - recalculate req.", tmpCoords)
                    createdFlag = False
                    break
            if createdFlag:  # created ok
                self.hitPoints = []
                break

        self.coords = [[x[0], x[1]] for x in tmpCoords]

        # calculate ship's vicinity
        self.calculateVicinity()
