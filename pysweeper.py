# Eric Kimsey
# 2019
# Python implementation of Minesweeper

import random, argparse

def main():
    parser = argparse.ArgumentParser(description='A Python implementation of Minesweeper.')
    parser.add_argument('-r', '--random', action='store_true', help='Generate a random minefield.')
    args = parser.parse_args()
    
    if args.random:
        sizeX = random.randrange(2, 26)
        sizeY = random.randrange(2, 23)
        numMines = random.randrange(1, round((sizeX * sizeY) / 2))
        print(str(sizeX) + ' x ' + str(sizeY) + ' with ' + str(numMines) + ' mines')
        field = Field(sizeX, sizeY, numMines)
    else:
        field = userSetup()
    
    placeMines(field)
    determineValues(field)

    while True:
        displayField(field)
        if not field.end:
            getUserInput(field)
        else:
            print('GAME OVER')
            break

def userSetup():
    # Choose width of minefield
    sizeX = None
    while (sizeX is None):
        try:
            sizeX = int(input('How wide would you like your minefield? (2-26) '))
        except ValueError:
            print('Value entered is not an integer!')
            continue
        if sizeX < 2:
            print('Minefield must be wider than 1 cell!')
            sizeX = None
        elif sizeX > 26:
            print('Minefield cannot be more than 26 cells wide!')
            sizeX = None
    
    # Choose height of minefield
    sizeY = None
    while (sizeY is None):
        try:
            sizeY = int(input('How tall would you like your minefield? (2-23) '))
        except ValueError:
            print('Value entered is not an integer!')
            continue
        if sizeY < 2:
            print('Minefield must be taller than 1 cell!')
            sizeY = None
        elif sizeY > 23:
            print('Minefield cannot be more than 23 cells tall!')
            sizeY = None
    
    # Choose number of mines in the minefield
    numMines = None
    while (numMines is None):
        try:
            numMines = int(input('How many mines would you like? '))
        except ValueError:
            print('Value entered is not an integer!')
            continue
        if numMines < 1:
            print('Minefield must have at least one mine!')
            numMines = None
        elif numMines > ((sizeX * sizeY) - 1):
            print('Not enough space on the minefield! Choose less mines!')
            numMines = None

    return Field(sizeX, sizeY, numMines)

def placeMines(field):
    numMinesTmp = field.numMines

    while (numMinesTmp > 0):
        x = random.randrange(0, field.sizeX)
        y = random.randrange(0, field.sizeY)
        if (not field.minefield[y][x].mine):
            field.minefield[y][x].placeMine()
            numMinesTmp = numMinesTmp - 1

def determineValues(field):
    for y in range(len(field.minefield)):
        for x in range(len(field.minefield[y])):
            if field.minefield[y][x].mine:
                continue
            
            value = 0
            # Check top-left
            if x > 0 and y > 0:
                if field.minefield[y-1][x-1].mine:
                    value = value + 1
            
            # Check above
            if y > 0:
                if field.minefield[y-1][x].mine:
                    value = value + 1
            
            # Check top-right
            if x < len(field.minefield[y]) - 1 and y > 0:
                if field.minefield[y-1][x+1].mine:
                    value = value + 1
            
            # Check left
            if x > 0:
                if field.minefield[y][x-1].mine:
                    value = value + 1
            
            # Check right
            if x < len(field.minefield[y]) - 1:
                if field.minefield[y][x+1].mine:
                    value = value + 1
            
            # Check bottom-left
            if x > 0 and y < len(field.minefield) - 1:
                if field.minefield[y+1][x-1].mine:
                    value = value + 1
            
            # Check below
            if y < len(field.minefield) - 1:
                if field.minefield[y+1][x].mine:
                    value = value + 1
            
            # Check bottom-right
            if x < len(field.minefield[y]) - 1 and y < len(field.minefield) - 1:
                if field.minefield[y+1][x+1].mine:
                    value = value + 1
            
            field.minefield[y][x].value = value

def displayField(field):
    for y in range(len(field.minefield)):
        for x in range(len(field.minefield[y])):
            if x == field.sizeX - 1:
                ending = '\n'
            else:
                ending = ''

            if field.minefield[y][x].revealed:
                if field.minefield[y][x].mine:
                    print('[*]', end=ending)
                else:
                    print('[' + str(field.minefield[y][x].value) + ']', end=ending)
            else:
                print('[ ]', end=ending)

def depthFirstSearch(field, x, y):
    # Check above
    if y > 0:
        if field.minefield[y-1][x].value == 0 and not field.minefield[y-1][x].revealed:
            field.minefield[y-1][x].revealed = True
            depthFirstSearch(field, x, y-1)
    
    # Check left
    if x > 0:
        if field.minefield[y][x-1].value == 0 and not field.minefield[y][x-1].revealed:
            field.minefield[y][x-1].revealed = True
            depthFirstSearch(field, x-1, y)
    
    # Check right
    if x < len(field.minefield[y]) - 1:
        if field.minefield[y][x+1].value == 0 and not field.minefield[y][x+1].revealed:
            field.minefield[y][x+1].revealed = True
            depthFirstSearch(field, x+1, y)
    
    # Check below
    if y < len(field.minefield) - 1:
        if field.minefield[y+1][x].value == 0 and not field.minefield[y+1][x].revealed:
            field.minefield[y+1][x].revealed = True
            depthFirstSearch(field, x, y+1)

def getUserInput(field):
    while True:
        try:
            userX = int(input('Choose X coordinate: '))
            userY = int(input('Choose Y coordinate: '))
        except ValueError:
            print('Value entered is not an integer!')
            continue
        
        if userX < 0 or userX > len(field.minefield[0]) - 1 or userY < 0 or userY > len(field.minefield) - 1:
            print('Value entered is out of range!')
            continue
        
        if not field.minefield[userY][userX].revealed:
            field.minefield[userY][userX].revealed = True
            if field.minefield[userY][userX].mine:
                field.end = True
            if field.minefield[userY][userX].value == 0:
                depthFirstSearch(field, userX, userY)
        else:
            print('This tile has already been revealed!')
            continue
        
        break

class Field:    
    def __init__(self, sizeX, sizeY, numMines):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.numMines = numMines
        self.revealedMines = 0
        self.minefield = [[None for x in range(sizeX)] for y in range(sizeY)]
        self.end = False

        for j in range(sizeY):
            for i in range(sizeX):
                self.minefield[j][i] = Tile(i,j)


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mine = False
        self.flag = False
        self.revealed = False
        self.value = None
    
    def placeMine(self):
        self.mine = True
    
    def toggleFlag(self):
        if self.flag:
            self.flag = False
        else:
            self.flag = True

if __name__ == '__main__':
    main()