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
        field = Field(sizeX, sizeY, numMines)
    else:
        field = userSetup()
    
    placeMines(field)
    displayField(field)
    

def userSetup():
    # Choose width of minefield
    sizeX = None
    while (sizeX is None):
        sizeX = int(input('How wide would you like your minefield? (2-26) '))
        #TODO - Handle non-numbers entered
        if sizeX < 2:
            print('Minefield must be wider than 1 cell!')
            sizeX = None
        elif sizeX > 26:
            print('Minefield cannot be more than 26 cells wide!')
            sizeX = None
    
    # Choose height of minefield
    sizeY = None
    while (sizeY is None):
        sizeY = int(input('How tall would you like your minefield? (2-23) '))
        #TODO - Handle non-numbers entered
        if sizeY < 2:
            print('Minefield must be taller than 1 cell!')
            sizeY = None
        elif sizeY > 23:
            print('Minefield cannot be more than 23 cells tall!')
            sizeY = None
    
    # Choose number of mines in the minefield
    numMines = None
    while (numMines is None):
        numMines = int(input('How many mines would you like? '))
        #TODO - Handle non-numbers entered
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

def displayField(field):
    for y in range(len(field.minefield)):
        for x in range(len(field.minefield[y])):
            if x == field.sizeX - 1:
                ending = '\n'
            else:
                ending = ''

            if field.minefield[y][x].mine:
                print('[*]', end=ending)
            else:
                print('[ ]', end=ending)

class Field:    
    def __init__(self, sizeX, sizeY, numMines):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.numMines = numMines
        self.minefield = [[None for x in range(sizeX)] for y in range(sizeY)]

        for j in range(sizeY):
            for i in range(sizeX):
                self.minefield[j][i] = Tile(i,j)


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mine = False
        self.flag = False
    
    def placeMine(self):
        self.mine = True
    
    def toggleFlag(self):
        if self.flag:
            self.flag = False
        else:
            self.flag = True

if __name__ == '__main__':
    main()