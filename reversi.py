'''
SV48-2022, Tamara Cvjetkovic
cvjetkovic.sv48.2022@uns.ac.rs
'''

from tree import TreeNode, Tree
from datetime import datetime
from copy import copy, deepcopy

import copy
import time

from reversiMakingMoves import validMoves, validMoves2, makeMove, numValidMoves
from reversiUtils import copyTable, showResult, showTable, showTableAndValidsPlayer
from reversiHeuristic import heuristicEvaluation
from reversiMinimax import minimax, computersMove

global black, white
black = 2
white = 2
              

def playReversi(player, table):
    global black, white
    opp = 2
    if (player == 1):
        print("\nIgrate kao crna tackica - ⚫\n")
    else:
        print("\nIgrate kao bela tackica - ⚪\n") 
        opp = 1
    kraj = 0  
    while (kraj == 0):  
        validsPlayer = validMoves(player, opp, table)
        if (len(validsPlayer) != 0):
            print("\n\n\nVI STE NA POTEZU.\n")
            showTableAndValidsPlayer(player, table, validsPlayer, black, white)
            while (True):
                num = str(input("\nIzaberite broj poteza: "))
                try: 
                    c = int(num)
                    if (c < 1 or c > len(validsPlayer)):
                        print("\nGRESKA! Pogresan unos.\n")   
                        continue 
                    (row, col) = validsPlayer[c - 1]
                    print("Izabrana celija: [", end = "")
                    print(row + 1, ", ", end = "")
                    print(col + 1, end = "")
                    print("]")
                    break
                except:
                    print("\nGRESKA! Pogresan unos.\n")   
                    continue    
            b, w = makeMove(player, table, row, col, True, black, white)
            black = b
            white = w
            print("\n\n\nStanje table nakon Vaseg poteza:\n")
            showTable(player, table, black, white)
        validsComputer = validMoves2(opp, player, table, 1)      
        if (len(validsComputer) == 0 and len(validsPlayer) == 0):
            kraj = 1
            continue
        if (len(validsPlayer) == 0):
            print("\n\nNEMATE TRENUTNO SLOBODNIH POTEZA!\n\n")
            pass
        #print(validsComputer)
        if (len(validsComputer) != 0):
            print("\n\n\nKompjuter igra....")
            # kompjuter igra potez
            #print(validsComputer)
            compMove = computersMove(player, table, validsComputer, black, white)
            (y, x) = compMove
            b, w = makeMove(opp, table, y, x, True, black, white) 
            black = b
            white = w 
            print("\nIzabrana celija kompjutera: [", end = "")
            print(y + 1, ", ", end = "")
            print(x + 1, end = "")
            print("]\n")
            print("\n\nStanje table nakon kompjuterovog poteza:\n")
            showTable(player, table, black, white)
            print("\n\n")
            continue
        
    if (player == 1):
        if (black > white):
            print("\n\n\nCESTITAMO, pobedili ste!\n")
            print("Krajni rezultat: \n")
            showResult(player, black, white)
        if (black == white):
            print("\n\n\nNERESENO!\n")  
            print("Krajni rezultat: \n")
            showResult(player, black, white)
        if (black < white):
            print("\n\n\nIZGUBILI STE, vise srece drugi put!\n") 
            print("Krajni rezultat: \n")
            showResult(player, black, white)   
    else:
        if (white > black):
            print("\n\nCESTITAMO, pobedili ste!\n")
            print("Krajni rezultat: \n")
            showResult(player, black, white)
        if (white == black):
            print("\n\nNERESENO!\n") 
            print("Krajni rezultat: \n")
            showResult(player, black, white) 
        if (white < black):
            print("\n\nIZGUBILI STE, vise srece drugi put!\n")
            print("Krajni rezultat: \n") 
            showResult(player, black, white)
    print("─────────────────────────────────────────────────\n\n\n") 
    return   
  
  

if __name__ == '__main__':
    dateNow = datetime.now()
    d1 = dateNow.strftime("%d/%m/%Y, %H:%M:%S")
    d2 = str(d1)
    print("\n\n")
    print(d2)
    print("\n\nDobrodosli u igru 'Reversi'!\n\n\n")
    
    table = [[0,  0,  0,  0,  0,  0,  0,  0],
             [0,  0,  0,  0,  0,  0,  0,  0],
             [0,  0,  0,  0,  0,  0,  0,  0],
             [0,  0,  0,  2,  1,  0,  0,  0],
             [0,  0,  0,  1,  2,  0,  0,  0],
             [0,  0,  0,  0,  0,  0,  0,  0],
             [0,  0,  0,  0,  0,  0,  0,  0],
             [0,  0,  0,  0,  0,  0,  0,  0]]
                  
    while (True):
        print("Izaberite boju: ")
        print("1. crni - ⚫")
        print("2. beli - ⚪")
        boja = str(input("\nUnesi broj: "))
        if (boja == "1"):
            print("\n\n\n─────────────────────\n")
            print("'REVERSI'\n")
            playReversi(1, table)
            break
        elif (boja == "2"):
            print("\n\n\n─────────────────────\n")
            print("'REVERSI'\n")
            playReversi(2, table)
            break
        else:  
            print("\nGRESKA! Unesite ponovo.\n\n")
            continue
        
        
                    
'''
for i in range(1, 9):
    for j in range(1, 9):
        print(table[i][j], end = "  ")
        if (table[i][j] == -1):
            if (table[i][j] == 0):
                print("", end = " ")
        if (table[i][j] == 0 or table[i][j] == 2 or table[i][j] == 1):
            print("", end = " ") 
    print("\n")
print("\n\n")  


for i in range(1, 9):
    for j in range(1, 9):
        print(table[i][j], end = " ") 
    print("")
print("\n\n")    
    
    
for i in range(1, 9):
    for j in range(1, 9):
        if (table[i][j] != 0):
            print(table[i][j], end = " ")
        else:
            print(valids[i * 10 + j], end = " ") 
    print("")
print()                 
'''