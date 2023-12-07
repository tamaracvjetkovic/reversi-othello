from copy import copy, deepcopy
import time

def copyTable(table):
    copyTable = deepcopy(table)
    return copyTable  
   
def showResult(player, black, white):
    if (player == 1):
        if (black > 9 and white > 9):
            print("\n        ⚫: ", black, "   ⚪: ", white, "\n\n")
            return
        if (black > 9): 
            print("\n          ⚫: ", black, "   ⚪: ", white, "\n\n")
            return
        print("\n           ⚫: ", black, "   ⚪: ", white, "\n\n")
        return
    else:
        if (black > 9 and white > 9):
            print("\n        ⚪: ", white, "   ⚫: ", black, "\n\n")
            return
        if (black > 9): 
            print("\n         ⚪: ", white, "   ⚫: ", black, "\n\n")
            return
        print("\n          ⚪: ", white, "   ⚫: ", black, "\n\n")
        return
   
def showTable(player, table, black, white):
    showResult(player, black, white)
    s = "    1   2   3   4   5   6   7   8\n  ┌───┬───┬───┬───┬───┬───┬───┬───┐\n"
    for i in range(0, 8):
        s += str(i + 1) + " │"
        for j in range(0, 8):
            if (table[i][j] == 1):
                s += "⚫ │"
                continue
            if (table[i][j] == 2):
                s += "⚪ │"
                continue
            s += "   │"  
        if (i == 7):
            s += "\n  └───┴───┴───┴───┴───┴───┴───┴───┘\n"  
        else:  
            s += "\n  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"    
    print(s)
    return   

def showTableAndValidsPlayer(player, table, valids, black, white):
    colors = []
    for c in range(1, 65):
        colors.append(str(c))
    showResult(player, black, white)
    num = 5
    for (y, x) in valids:
        table[y][x] = num
        num += 1
    s = "    1   2   3   4   5   6   7   8\n  ┌───┬───┬───┬───┬───┬───┬───┬───┐\n"
    for i in range(0, 8):
        s += str(i + 1) + " │"
        for j in range(0, 8):
            if (table[i][j] == 1):
                s += "⚫ │"
                continue
            if (table[i][j] == 2):
                s += "⚪ │"
                continue
            if (table[i][j] > 13):
                s += " "
                s += colors[table[i][j] - 5]
                s += "│"
                continue
            if (table[i][j] > 4):
                s += " "
                s += colors[table[i][j] - 5]
                s += " │"
                continue
            s += "   │"  
        if (i == 7):
            s += "\n  └───┴───┴───┴───┴───┴───┴───┴───┘\n"  
        else:  
            s += "\n  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"    
    print(s)
    for i in range(0, 8):
        for j in range(0, 8):
            if (table[i][j] > 2):
                table[i][j] = 0
    return


