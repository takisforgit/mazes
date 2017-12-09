"""
	Name: backtracking-ex1.py
	Copyright: https://www.youtube.com/watch?v=0C8BUf_0DB4
	Date: 23/10/17
	Description: Backtracking algorithm and mazes
"""

#############################################################
def findPath(i, j, n, A, path) :
	""""
	Given the (i,j) the coordinates of Starting position, find the END of maze A
	Store it in path variable. 
	"""
	## Check if the END of array ( destination ) is reached 
	global visited
	if( (i == n-1) and ( j == n-1 ) ): 
		path[i][j] = 1 
		print("END reached,at (%d,%d)\n"%(i,j))
		return 1


	## Check if EVERY Cell is EMPTY (1) OR BLOCKED (0)
	if ( A[i][j] == 1 ) : ## Cell is EMPTY
		path[i][j] = 1     ## Keep track of Cell & ADD Cell to Path
		visited.append((i,j))
		# print("Visited (%d,%d)"%(i, j) )
		print("Visited ",visited)


		## ALWAYS check RIGHT first, then DOWN - ONLY
		## Check if you can move to the RIGHT side of the Cell Next COL: j+1
		if( findPath(i, j+1, n, A, path) ) :
			return 1;
		# else:
		# 	print("Cannot move RIGHT to (%d,%d)"%(i, j+1) )
			# print("Trying DOWN to (%d,%d)"%(i+1,j))
		
		## Check if you can move to the DOWN side of the Cell Next ROW : i+1 
		if ( findPath(i+1, j, n, A, path) ) :
			return 1
		# else:
		# 	print("Cannot move DOWN to (%d,%d)"%(i+1, j) )

		visited.pop()
		print("DEAD END or Already VISITED !!!")
		print("Go back to (%d,%d)..."%visited[-1])
		## If there are NO EMPTY Cells RIGHT or DOWN, GO BACK ( and remove Cell from the path )
		path[i][j] = 0 

	# print(path)

	## Other way NO PATH found to go . Return False (0)
	return 0 


#############################################################
def printPath(path) :

	rows = 4
	cols = 4
	print("\nPath from START --> END ( sequence of nodes ):")
	for i in range(rows) :
		for j in range(cols) :
			if ( path[i][j] == 1 ) :	## if Cell is in the path found
				print("(%d,%d)-->"%(i,j) , end="")
			# if ( i == rows-1 and j == cols-1): ## last cell
			# 	print("(%d,%d)"%(i,j))
	print("\n")
#############################################################
global visited
visited=[]

maze =  [ 
	[1,1,1,0],
	[1,0,1,0],
	[1,1,0,0],
	[0,1,1,1] 
	] 

mzpath= [ 
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0] 
	] 
	
findPath(0,0,4,maze,mzpath) 
printPath(mzpath)

