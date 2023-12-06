

global oki00
global oki77
global oki07
global oki70

   
def validMoves2(cur, opp, table, m2):
    global oki00, oki77, oki07, oki70
    oki00 = 0
    oki77 = 0
    oki07 = 0
    oki70 = 0     
    corners = []
    valids = validMoves(cur, opp, table)
    if (oki00 == 1):
        corners.append((0, 0))
    if (oki77 == 1):
        corners.append((7, 7))
    if (oki07 == 1):
        corners.append((0, 7))
    if (oki70 == 1):
        corners.append((7, 0))
    if (len(corners) != 0):
        return corners
    else:
        return valids
    
    
def validMoves(cur, opp, table):
    global oki00, oki77, oki07, oki70
    oki00 = 0
    oki77 = 0
    oki07 = 0
    oki70 = 0 
    valids = []
    used = {}
    for starty in range(0, 8):
        for startx in range(0, 8):
            if (table[starty][startx] == cur):
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        ok = 0
                        if (dy == 0 and dx == 0):
                            continue
                        for ctr in range(1, 8):        
                            y = starty + ctr * dy
                            x = startx + ctr * dx
                            if (x >= 0 and y >= 0 and x < 8 and y < 8):
                                if (used.get((y, x)) is not None):
                                    break
                                if (table[y][x] == cur):
                                    break
                                if (table[y][x] == opp):
                                    ok = 1
                                    continue
                                if (table[y][x] == 0 and ok == 1):
                                    move = (y, x)
                                    used[move] = 1
                                    if (move == (0, 0)):
                                        oki00 = 1
                                    elif (move == (7, 7)):
                                        oki77 = 1
                                    elif (move == (7, 0)):
                                        oki70 = 1
                                    elif (move == (0, 7)):
                                        oki07 = 1
                                    valids.append(move) 
                                    ok = 0   
                                    break
                                else:
                                    break
                            else:
                                break                                       
    return valids


def makeMove(color, table, starty, startx, count, black, white):
    table[starty][startx] = color
    if (count is True):
        if (color == 1):
            black += 1
        else:
            white += 1
        
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (dy == 0 and dx == 0):
                continue
            zavrsi = 0
            for ctr in range(1, 8):
                x = startx + ctr * dx
                y = starty + ctr * dy
                if (x >= 0 and y >= 0 and x < 8 and y < 8):
                    pass
                else:
                    break
                if (table[y][x] == 0):
                    break
                if (table[y][x] == color):
                    if (zavrsi == 1):
                        break
                    #print("EVO GA COLOR: ", y, ",",  x)
                    for ctr in range(1, 8):
                        x2 = x - ctr * dx
                        y2 = y - ctr * dy
                        if (x2 >= 0 and y2 >= 0 and x2 < 8 and y2 < 8):
                            pass
                        else:
                            break
                        if (table[y2][x2]) == color:
                            break
                        table[y2][x2] = color 
                        if (count is True):
                            if (color == 1):
                                black += 1
                                white -= 1
                            else:
                                white += 1
                                black -= 1
                    zavrsi = 1            
            continue
        continue
    if (count is True):
        return black, white
      
      
def numValidMoves(cur, opp, table):
    return (len(validMoves(cur, opp, table)))