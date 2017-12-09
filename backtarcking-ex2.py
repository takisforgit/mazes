"""
	Name: backtracking-ex2.py
	Copyright: https://brilliant.org/wiki/recursive-backtracking/
	Date: 23/10/17
	Description: Backtracking algorithm and mazes
"""


def solveMaze(Maze, position, N):
	''' Return a list of the paths taken '''
	if position == ( N-1, N-1): 
		return [(N-1, N-1)]

	x, y = position

	## Check DOWN cell
	if( (x+1 < N) and (Maze[x+1][y] == 1) ) :
		a = solveMaze(Maze, (x+1,y), N)
		# print("a=",a)

		if a != None:
			print("DOWN Return value=", [ (x,y)] + a )
			return [ (x,y)] + a 

	## Check RIGHT cell
	if( (y+1 < N) and (Maze[x][y+1] == 1) ) :
		b = solveMaze(Maze, (x,y+1), N)
		# print("b=",b)

		if b != None:
			print("RIGHT Return value=", [ (x,y)] + b )
			return [ (x,y)] + b



Maze = [
[1,0,1,0,0],
[1,1,0,1,0],
[0,1,0,1,0],
[0,1,0,0,0,],
[1,1,1,1,1]
]


Maze2 = [
[1,0,0,0],
[1,1,0,1],
[0,1,0,0],
[1,1,1,1]
]


Maze3 = [
[1,0,0,0],
[1,1,0,1],
[0,1,1,1],
[1,1,0,1]
]

# print(solveMaze(Maze,(0,0), 5) )
print(solveMaze(Maze2,(0,0), 4) )
# print(solveMaze(Maze3,(0,0), 4) )






