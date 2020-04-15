from gameToken import Token
from terminal_text_color import TextColor
import numpy as np
import os

# Initialize Textcolour

tc = TextColor()

# Constraints

Rows = 7
Columns = 6

# Functions


def buildTable():
    os.system('cls')
    token = Token()
    table = np.empty((Rows, Columns,), dtype=Token)
    for i in range(Rows):
        for j in range(Columns):
            table[i][j] = token
    return table


def pToken():
    while True:
        try:
            position1 = int(input('Enter horizontal position: '))
            if position1 >= 0 and position1 < 7:
                break
            else:
                print('Must be between 0 and 6')
        except ValueError:
            print('ERROR. Must be an integer between 0 and 6')
    while True:
        try:
            position2 = int(input('Enter vertical position: '))
            if position2 >= 0 and position2 < 6:
                break
            else:
                print('Must be between 0 and 5')
        except ValueError:
            print('ERROR. Must be an integer between 0 and 5')
    return position1, position2


def chooseOption(table):
    while True:
        option = input('\nEnter colour(R/G): ')
        if option.upper() == 'R' or option.upper() == 'G':
            break
        else:
            printTable(table)
            print('ERROR. Must be RED (R) or green (G)')
    return option


def writeRedToken(data):
    data.occupied = True
    data.colour = tc.default_red('R')
    return data


def writegreenToGen(data):
    data.occupied = True
    data.colour = tc.default_green('G')
    return data


def printTable(table):
    os.system('cls')
    for i in range(Rows):
        print('\n')
        for j in range(Columns):
            print(table[i][j].colour, end='   ')
            if i == 6 and j == 5:
                print('\n')


def placeToken(table):
    token = Token()
    option = chooseOption(table)
    while True:
        pos1, pos2 = pToken()
        if option.upper() == 'R' and table[pos1][pos2].occupied == False:
            token = writeRedToken(token)
            table[pos1][pos2] = token
            break
        elif option.upper() == 'G' and table[pos1][pos2].occupied == False:
            token = writegreenToGen(token)
            table[pos1][pos2] = token
            break
        else:
            printTable(table)
            print('Space occupied by another token')
            print('Chosen colour:', option.upper())

    return table

# WIN parameter is a boolean value


def areTokensHorizontal(table, win):
    for i in range(Rows):
        for j in range(Columns):
            if j < 3:
                if table[i][j].colour == table[i][j+1].colour == table[i][j+2].colour == table[i][j+3].colour == tc.default_red('R'):
                    printTable(table)
                    print('RED TEAM WINS\n')
                    win = True
                else:
                    if table[i][j].colour == table[i][j+1].colour == table[i][j+2].colour == table[i][j+3].colour == tc.default_green('G'):
                        printTable(table)
                        print('GREEN TEAM WINS\n')
                        win = True
                    else:
                        if table[i][j].colour == table[i][j-1].colour == table[i][j-2].colour == table[i][j-3].colour == tc.default_red('R'):
                            printTable(table)
                            print('RED TEAM WINS\n')
                            win = True
            else:
                if table[i][j].colour == table[i][j-1].colour == table[i][j-2].colour == table[i][j-3].colour == tc.default_green('G'):
                    printTable(table)
                    print('GREEN TEAM WINS\n')
                    win = True
    return win


def areTokensVertical(table, win):
    for i in range(Rows):
        for j in range(Columns):
            if i < 4:
                if table[i][j].colour == table[i+1][j].colour == table[i+2][j].colour == table[i+3][j].colour == tc.default_red('R'):
                    printTable(table)
                    print('RED TEAM WINS\n')
                    win = True
                else:
                    if table[i][j].colour == table[i+1][j].colour == table[i+2][j].colour == table[i+3][j].colour == tc.default_green('G'):
                        printTable(table)
                        print('GREEN TEAM WINS\n')
                        win = True
                    else:
                        if table[i][j].colour == table[i-1][j].colour == table[i-2][j].colour == table[i-3][j].colour == tc.default_red('R'):
                            printTable(table)
                            print('RED TEAM WINS\n')
                            win = True
            else:
                if table[i][j].colour == table[i-1][j].colour == table[i-2][j].colour == table[i-3][j].colour == tc.default_green('G'):
                    printTable(table)
                    print('GREEN TEAM WINS\n')
                    win = True
    return win


def areTokensDiagonalLeftRight(t, win):
    for i in range(Rows):
        for j in range(Columns):
            if i < 4 and j < 3:
                if t[i][j].colour == t[i+1][j+1].colour == t[i+2][j+2].colour == t[i+3][j+3].colour == tc.default_red('R'):
                    printTable(t)
                    print('RED TEAM WINS\n')
                    win = True
                else:
                    if t[i][j].colour == t[i+1][j+1].colour == t[i+2][j+2].colour == t[i+3][j+3].colour == tc.default_green('G'):
                        printTable(t)
                        print('GREEN TEAM WINS\n')
                        win = True
            else:
                if t[i][j].colour == t[i-1][j-1].colour == t[i-2][j-2].colour == t[i-3][j-3].colour == tc.default_red('R'):
                    printTable(t)
                    print('RED TEAM WINS\n')
                    win = True
                else:
                    if t[i][j].colour == t[i-1][j-1].colour == t[i-2][j-2].colour == t[i-3][j-3].colour == tc.default_green('G'):
                        printTable(t)
                        print('GREEN TEAM WINS\n')
                        win = True
    return win


def areTokensDiagonalRightLeft(table, win):
    for i in range(Rows):
        for j in range(Columns):
            if i < 4 and j > 2:
                if table[i][j].colour == table[i+1][j-1].colour == table[i+2][j-2].colour == table[i+3][j-3].colour == tc.default_red('R'):
                    printTable(table)
                    print('RED TEAM WINS\n')
                    win = True
                else:
                    if table[i][j].colour == table[i+1][j-1].colour == table[i+2][j-2].colour == table[i+3][j-3].colour == tc.default_green('G'):
                        printTable(table)
                        print('GREEN TEAM WINS\n')
                        win = True
            elif i > 3 and j < 3:
                if table[i][j].colour == table[i-1][j+1].colour == table[i-2][j+2].colour == table[i-3][j+3].colour == tc.default_red('R'):
                    printTable(table)
                    print('RED TEAM WINS\n')
                    win = True
                else:
                    if table[i][j].colour == table[i-1][j+1].colour == table[i-2][j+2].colour == table[i-3][j+3].colour == tc.default_green('G'):
                        printTable(table)
                        print('GREEN TEAM WINS\n')
                        win = True
    return win


def runGame():
    t = buildTable()
    win = False
    while not(win):
        printTable(t)
        placeToken(t)
        win = areTokensHorizontal(t, win)
        if win == False:
            win = areTokensVertical(t, win)
            if win == False:
                win = areTokensDiagonalLeftRight(t, win)
                if win == False:
                    win = areTokensDiagonalRightLeft(t, win)
