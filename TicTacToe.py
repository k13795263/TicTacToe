#!/usr/bin/pyton3
import itertools
import numpy as np

play1 = 1
play2 = 2
qTable = {}
episode = 0

for i in itertools.product([0,1,2], repeat = 9):
     qTable.update({i : 0})

def reward(state): #return reward in current state
     board = [(0,1,2), (3,4,5), (6,7,8),(0,3,6), (1,4,7), (2,5,8),(0,4,8), (2,4,6)]
     for (a, b, c) in board:
         if (state[a] != 0):
             if (state[a] == state[b] == state[c]):
                 return 1
     return 0
     
     
def chooseMove(board, pool, player): # return random position in space board
    temp = []
    for i in range(len(board)):
         if (board[i] == 0):
             temp.append(i)
    length = len(temp)
    return (temp[np.random.randint(0, length)])
    
def nextQvalue(board, pool, player): #return all q-value in nextState for current state
        if (0 in board):
            value = []
            for i in range(len(board)):
                if (board[i] != 0) :
                     temp = board[:]
                     temp[i] = player
                     k = tuple(temp)
                     value.append(pool[k])
            return value
        else:
            return [0, 0]

def feedBackQvalue(length, qTable, state):
    preState = state[:]
    while (length > 0):
        preState[p[length]] = 0
        qTable[tuple(preState)] = qTable[tuple(preState)] + 0.1 *(0.9 * qTable[tuple(state)] - qTable[tuple(preState)])
        state = preState[:]
        length -= 1
    return 0
    
while (episode < 10000):
    episode += 1
        
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    p = []
    turn = 1
    while ( 0 in state):
        position = chooseMove(state, qTable, turn) # return random position in space board
        p.append(position)           # recode path choose
        state[position] = turn
        if(reward(state) == 1 ):
            if (turn == 1):
                qTable[tuple(state)] = 1
            elif(turn == 2):
                qTable[tuple(state)] = -1
            break
        elif(turn == 1):
            turn = 2
            t = nextQvalue(state,qTable, turn) #q-value
            expected = (0.9 * min(t) - qTable[tuple(state)]) #q-value
            qTable[tuple(state)] += 0.1 * expected #q-value
        else:  #turn == 2
            turn = 1
            t = nextQvalue(state,qTable, turn) #q-value
            expected = (0.9 * max(t) - qTable[tuple(state)]) #q-value
            qTable[tuple(state)] += 0.1 * expected #q-value
    length = len(p) -1
    k=feedBackQvalue(length, qTable, state)

def choose(board, pool): #computer always to  choose maxQvalue position return
    k=-1000
    co = 0
    for i in range(len(board)):
        temp = board[:]
        if (board[i] == 0):
            temp[i] = 1
            if (pool[tuple(temp)] > k):
                k = pool[tuple(temp)]
                co = i
    return co


board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
while (0 in board):  #I never win in my experience 
    postion = choose(board, qTable)
    board[postion] = 1
    print (board)
    if (reward(board) == 1):
        print ('computer win')
        break
    k = int(input("input you want position for board "))
    board[k] = 2
    print (board)
    if (reward(board) == -1):
        print ('your win')
        break
print (board)
  
  
    
