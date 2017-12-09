""""
File : mazeSolve-Introduction-example.py
Based on  : https://medium.com/@lavanya.ac/introduction-to-backtracking-8ada04f0255
Date: 27-10-2017

Backtracking algorithms solve a complicated problem by breaking down into sub-problems.
They recursively build partial solutions to the problem. While solving the sub-problem,
if we did not reach the desired solution, then undo whatever we did for solving that sub-problem,
and move-on to solving the next sub-problem.

"""


def mazeSolve(maze, xdim, ydim):
  ## Prepopulate solution matrix with all 0s.
  for i in range(xdim):
    solution.append([])
    # print(i, solution[i])
  # print(solution)
    for j in range(ydim):
      solution[i].append(0)
    print(i,j, solution[i])
    
  for i in range(len(maze)):
    return mazeHelper(maze, 0, 0)


def mazeHelper(maze, row, col) :

    ##  If we already reached the end , return true
    ##  START is at [0][0] and TARGET is at the end of maze e.g [xdim-1][ydim-1]
    ##
    if (row == xdim-1 and  col == ydim-1 and  maze[row][col] == 1) :
      solution[row][col] = 1
      return True
    
    ## Check if the current position is valid - check if the current position has a 1 
    ##    and that we havent stepped outside the matrix boundary. 
    if (isValid(maze, row, col)) :
      ##  Add the current position to the solution
      solution[row][col] = 1
      ## Check if we can go down
      if (mazeHelper(maze, row + 1, col)) :
        return True
      
      ## Check if we can go right
      if (mazeHelper(maze, row, col + 1)) :
        return True
      
      ##  Since we couldnt go down or right , we are in the wrong spot, so lets backtrack.
      solution[row][col] = 0
      return False
    
    ## Couldnt find a solution , return false
    return False;


##  Checks if the given position is valid - check if the given position has a 1 
##  and that we havent stepped outside the matrix boundary. 
def isValid(maze, row, col) :
    if ( row < xdim and col < ydim and  maze[row][col] == 1) :
      return True
    else :
      return False
    
  

##############################################################################

solution = []
maze = [
  [1, 1, 1, 0, 0],
  [1, 0, 1, 1, 0],
  [1, 1, 0, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 1, 0, 1, 1]
]

xdim = len(maze)
ydim = len(maze[0]) 

print("Size of maze:",xdim,"*", ydim )


resutl = False
result = mazeSolve(maze, xdim, ydim)
print("mazeSolve() Returned:",result)


## Print SOLUTION matrix
print("SOLUTION matrix")
for x in range(xdim):
  print(solution[x])

## Print SOLUTION path
if(result):
  print("Maze SOLVED !!!\nPath is: ", end="")
  for i in range(xdim) :
    for j in range(ydim) :
      if ( (solution[i][j] == 1) and (i == xdim-1)  and (j == ydim-1) ):
        print((i,j))
      elif ( solution[i][j] == 1) :
          print((i,j),"-->", end ="")
else:
  print("Maze has NO SOLUTION !!!")