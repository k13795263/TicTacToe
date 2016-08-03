# TicTacToe
in python3

use q-learning algorithm, i never make computer to lose

  if game over
     expected = reward
  else
     if player is '1'
        expected = reward + (discount * lowestQvalue(nextKey))
     else  #'2'
        expected = reward + (discount * highestQvalue(nextKey))
  change = learningRate * (expected - qtable[state][action])
  qtable[state][action] += change
  

