# Python implementation of Minesweeper

def main():
    setup()
    

def setup():
    # Choose width of minefield
    sizeX = None
    while (sizeX is None):
        sizeX = int(input('How wide would you like your minefield? (2-50) '))
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
        if sizeY < 2:
            print('Minefield must be taller than 1 cell!')
            sizeY = None
        elif sizeY > 50:
            print('Minefield cannot be more than 30 cells tall!')
            sizeY = None
    
    # Choose number of mines in the minefield
    numMines = None
    while (numMines is None):
        numMines = int(input('How many mines would you like? '))
        if numMines < 1:
            print('Minefield must have at least one mine!')
            numMines = None
        elif numMines > ((sizeX * sizeY) - 1):
            print('Not enough space on the minefield! Choose less mines!')
            numMines = None

if __name__ == '__main__':
    main()