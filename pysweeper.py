# Python implementation of Minesweeper

def main():
    field = setup()
    

def setup():
    # Choose width of minefield
    sizeX = None
    while (sizeX is None):
        sizeX = int(input('How wide would you like your minefield? (2-50) '))
        #TODO - Handle non-numbers entered
        if sizeX < 2:
            print('Minefield must be wider than 1 cell!')
            sizeX = None
        elif sizeX > 50:
            print('Minefield cannot be more than 50 cells wide!')
            sizeX = None
    
    # Choose height of minefield
    sizeY = None
    while (sizeY is None):
        sizeY = int(input('How tall would you like your minefield? (2-30) '))
        #TODO - Handle non-numbers entered
        if sizeY < 2:
            print('Minefield must be taller than 1 cell!')
            sizeY = None
        elif sizeY > 30:
            print('Minefield cannot be more than 30 cells tall!')
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

class Field:
    sizeX = None
    sizeY = None
    numMines = None
    
    def __init__(self, sizeX, sizeY, numMines):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.numMines = numMines

class Tile:
    x = None
    y = None
    mine = False
    flag = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def placeMine():
        self.mine = True
    
    def toggleFlag():
        if flag:
            flag = False
        else:
            flag = True

if __name__ == '__main__':
    main()