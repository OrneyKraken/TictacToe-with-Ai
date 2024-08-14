"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0 
    count_o = 0  

    for rows in range(len(board)): 
        for cols in range(len(board[0])): 
            if board[rows][cols] == X : 
                count_x += 1 
            elif board[rows][cols] == O : 
                count_o += 1 
    
    if count_x > count_o : 
        return O 
    else : 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allPossibleSet = set() 

    for rows in range(len(board)) : 
        for cols in range(len(board[0])) : 
            if board[rows][cols] == EMPTY : 
                allPossibleSet.add((rows,cols))

    return allPossibleSet                 

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not valid action") 
    
    row,col = action 
    board_copy = copy.deepcopy(board) 

    board_copy[row][col] = player(board)

    return board_copy 


def checkRow(board,player): 

    for i in range(len(board)): 
        if board[i][0] == player and board[i][1] == player and board[i][2] == player : 
            return True 
    return False     

def checkCol(board,player): 
    for i in range(len(board)):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player : 
            return True 
            
    return False 

def checkFirstCross(board,player): 
    count = 0 
    for i in range(len(board)): 
        for j in range(len(board[0])):
            if i == j and board[i][j] == player : 
                count += 1 
    if count == 3: 
        return True 
    else : 
        return False              

def checkSecondCross(board,player):
    if board[0][2] == player and board[1][1] == player and board[2][0] == player : 
        return True 
    return False   

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board,X) or checkCol(board,X) or checkFirstCross(board,X) or checkSecondCross(board,X): 
        return X 
    elif checkRow(board,O) or checkCol(board,O) or checkFirstCross(board,O) or checkSecondCross(board,O):
        return O 
    else : 
        return None 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X : 
        return True 
    if winner(board) == O : 
        return True 
    for i in range(len(board)) : 
        for j in range(len(board[0])) : 
            if board[i][j] == EMPTY : 
                return False 
    return True 

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X : 
        return 1 
    elif winner(board) == O :
        return -1 
    else : 
        return 0  


def  max_value(board) : 
    v = -math.inf
    if terminal(board) : 
        return utility(board) 
    
    for action in actions(board): 
        v = max(v,min_value(result(board,action)))
    return v

def  min_value(board) : 
    v = math.inf
    if terminal(board) : 
        return utility(board) 
    
    for action in actions(board): 
        v = min(v,max_value(result(board,action)))
    return v    



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) : 
        return None 
    
    elif player(board) == X : 
        plays = [] 
        for action in actions(board): 
            plays.append([min_value(result(board,action)),action])

        return sorted(plays, key = lambda x: x[0], reverse = True)[0][1]

    elif player(board) == O : 
        plays = [] 
        for action in actions(board): 
            plays.append([min_value(result(board,action)),action])

    return sorted(plays, key = lambda x: x[0])[0][1]

