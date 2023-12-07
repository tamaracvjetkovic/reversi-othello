from reversiMakingMoves import validMoves, makeMove, numValidMoves
from reversiUtils import copyTable, showResult, showTable, showTableAndValidsPlayer
   

def heuristicEvaluation(player, table):
    my_color = 2
    opp_color = 1
    if (player == 2):
        my_color, opp_color = opp_color, my_color
     
    my_tiles = 0
    opp_tiles = 0
    my_front_tiles = 0
    opp_front_tiles = 0
    x = 0
    y = 0
    i = 0
    j = 0
    k = 0
    p = 0
    c = 0
    l = 0
    m = 0
    f = 0
    d = 0

    X1 = [-1, -1, 0, 1, 1, 1, 0, -1]
    Y1 = [0, 1, 1, 1, 0, -1, -1, -1]
    
    V = [[20, -3, 11, 8, 8, 11, -3, 20],
    	 [-3, -7, -4, 1, 1, -4, -7, -3],
    	 [11, -4, 2, 2, 2, 2, -4, 11],
    	 [8, 1, 2, -3, -3, 2, 1, 8],
    	 [8, 1, 2, -3, -3, 2, 1, 8], 
         [11, -4, 2, 2, 2, 2, -4, 11],
    	 [-3, -7, -4, 1, 1, -4, -7, -3],
    	 [20, -3, 11, 8, 8, 11, -3, 20]]

    for i in range(0, 8):
        for j in range(0, 8):
            if (table[i][j] == my_color):
                d += V[i][j] 
                my_tiles += 1
            elif (table[i][j] == opp_color):
                d -= V[i][j]
                opp_tiles += 1
            if (table[i][j] != 0):
                for k in range(0, 8):
                    x = i + X1[k]
                    y = j + Y1[k]
                    if (x >= 0 and x < 8 and y >= 0 and y < 8 and table[x][y] == 0):
                        if (table[i][j] == my_color):
                            my_front_tiles += 1
                        else:
                            opp_front_tiles += 1
                        break
  
    
    if (my_tiles > opp_tiles):
        p = (100.0 * my_tiles) / (my_tiles + opp_tiles)
    elif (my_tiles < opp_tiles):
        p = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
    else:
        p = 0
        
    if (my_front_tiles > opp_front_tiles):
        f = -(100.0 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
    elif(my_front_tiles < opp_front_tiles):
        f = (100.0 * opp_front_tiles) / (my_front_tiles + opp_front_tiles)
    else:
        f = 0
        
    my_tiles = 0
    opp_tiles = 0
    if (table[0][0] == my_color):
        my_tiles += 1
    elif (table[0][0] == opp_color):
        opp_tiles += 1
    if (table[0][7] == my_color):
        my_tiles += 1
    elif (table[0][7] == opp_color):
        opp_tiles += 1
    if (table[7][0] == my_color):
        my_tiles += 1
    elif (table[7][0] == opp_color):
        opp_tiles += 1
    if (table[7][7] == my_color):
        my_tiles += 1
    elif (table[7][7] == opp_color):
        opp_tiles += 1
    c = 25 * (my_tiles - opp_tiles)


# Corner closeness
    my_tiles = 0
    opp_tiles = 0
    if (table[0][0] == 0):
        if (table[0][1] == my_color):
            my_tiles += 1
        elif (table[0][1] == opp_color):
            opp_tiles += 1
        if (table[1][1] == my_color):
            my_tiles += 1
        elif (table[1][1] == opp_color):
            opp_tiles += 1
        if (table[1][0] == my_color):
            my_tiles += 1
        elif (table[1][0] == opp_color):
            opp_tiles += 1
	
    if (table[0][7] == 0):
        if (table[0][6] == my_color):
            my_tiles += 1
        elif (table[0][6] == opp_color):
            opp_tiles += 1
        if (table[1][6] == my_color):
            my_tiles += 1
        elif (table[1][6] == opp_color): 
            opp_tiles += 1
        if (table[1][7] == my_color):
            my_tiles += 1
        elif (table[1][7] == opp_color):
            opp_tiles += 1
    
    if (table[7][0] == 0):
        if (table[7][1] == my_color):
            my_tiles += 1
        elif (table[7][1] == opp_color):
            opp_tiles += 1
        if (table[6][1] == my_color):
            my_tiles += 1
        elif (table[6][1] == opp_color):
            opp_tiles += 1
        if (table[6][0] == my_color): 
            my_tiles += 1
        elif (table[6][0] == opp_color):
            opp_tiles += 1
    
    if(table[7][7] == 0):
        if(table[6][7] == my_color):
            my_tiles += 1
        elif (table[6][7] == opp_color):
            opp_tiles += 1
        if (table[6][6] == my_color):
            my_tiles += 1
        elif (table[6][6] == opp_color):
            opp_tiles += 1
        if (table[7][6] == my_color):
            my_tiles += 1
        elif (table[7][6] == opp_color):
            opp_tiles += 1
    l = -12.5 * (my_tiles - opp_tiles);
    #print("l: ", l)
      
    my_moves = validMoves(my_color, opp_color, table)
    my_tiles = len(my_moves)
    opp_moves = validMoves(opp_color, my_color, table)
    opp_tiles = len(opp_moves)
    
# Mobility
    if (my_tiles > opp_tiles):
        m = (100.0 * my_tiles) / (my_tiles + opp_tiles);
    elif (my_tiles < opp_tiles):
        m = -(100.0 * opp_tiles) / (my_tiles + opp_tiles);
    else:
        m = 0;
        
    score = (10 * p) + (801.724 * c) + (382.026 * l) + (78.922 * m) + (74.396 * f) + (10 * d);
    return score;

    
    