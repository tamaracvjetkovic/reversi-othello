

import time
import sys


from reversiMakingMoves import validMoves, validMoves2, makeMove, numValidMoves
from reversiUtils import copyTable, showResult, showTable, showTableAndValidsPlayer
from reversiHeuristic import heuristicEvaluation


global stateValues
stateValues = {}


def computersMove(player, table2, validsComputer, black, white):
    timeLimit = 3
    bestMove = None
    bestScore = float('-inf')
    computer = 2
    if player == 2:
        computer = 1
    #depth = 5       
    #print(validsComputer)
    if (len(validsComputer) == 0):
            maxTimePerMove = 0
    else:
        maxTimePerMove = float(timeLimit / len(validsComputer))
    for move in validsComputer:
        startTime = time.time()
        (y, x) = move
        bestMove = move
        table = copyTable(table2)
        makeMove(computer, table, y, x, False, black, white)
        alfa = float('-inf')
        beta = float('inf')
        score = minimax(player, table, alfa, beta, False, startTime, maxTimePerMove, 0, black, white)
        if score > bestScore:
            bestScore = score
            bestMove = move
    #print(bestScore)
    #print(maxdepth)
    return bestMove



def minimax(player, table, alfa, beta, maxPlayer, startTime, timeLimit, depth, black, white):
    #print(depth)
    computer = 2
    if player == 2:
        computer = 1 
    if (stateValues.get(str(table)) is not None):
        #print("sacuvao!\n")
        return stateValues[str(table)]
    if sys.gettrace() is None:
        if (black + white > 15 and black + white < 50):
            timeLimit2 = timeLimit - 0.0006
        else:
            timeLimit2 = timeLimit - 0.00006
    else:   
        timeLimit2 = timeLimit - 0.0004    
    if time.time() - startTime >= timeLimit2:
        heur = heuristicEvaluation(player, table)
        stateValues[str(table)] = heur
        return heur
    if maxPlayer: 
        maxEval = float('-inf')
        valids = validMoves2(computer, player, table, 1)
        if (len(valids) == 0):
            maxTimePerMove = 0
        else:
            maxTimePerMove = float(timeLimit / len(valids))
        for move in valids:
            moveStartTime = time.time()
            (y, x) = move
            newTable = copyTable(table)
            makeMove(computer, newTable, y, x, False, black, white)
            eval = minimax(player, newTable, alfa, beta, False, moveStartTime, maxTimePerMove, depth + 1, black, white)
            #print("False: ", eval)
            if (eval >= maxEval):
                maxEval = eval
            alfa = max(alfa, eval)
            if beta <= alfa:
                break
        return maxEval
    else:
        minEval = float('inf')
        valids = validMoves2(player, computer, table, 1)
        if (len(valids) == 0):
            maxTimePerMove = 0
        else:
            maxTimePerMove = float(timeLimit / len(valids))   
        for move in valids:
            moveStartTime = time.time()
            (y, x) = move
            newTable = copyTable(table)
            makeMove(player, newTable, y, x, False, black, white)
            eval = minimax(player, newTable, alfa, beta, True, moveStartTime, maxTimePerMove, depth + 1, black, white)
            #if (eval > 10000):
                #print(eval)
            if (eval <= minEval):
                minEval = eval
            beta = min(beta, eval)
            if beta <= alfa:
                break
        return minEval
    
    

    