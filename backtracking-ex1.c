/*
	Name: backtracking-ex1.c
	Copyright: https://www.youtube.com/watch?v=0C8BUf_0DB4
	Date: 23/10/17
	Description: Backtracking algorithm and mazes
*/
#include <stdio.h>
#include <stdlib.h>

int findPath( int i, int j, int n, int A[4][4], int path[4][4]) ;
void printPath(int path[4][4]) ;


int main() {

	int maze[4][4] = {
		1,1,0,1,
		1,0,1,0,
		1,1,1,0,
		0,0,1,1
	} ;

	int mzpath[4][4] = {
		0,0,0,0,
		0,0,0,0,
		0,0,0,0,
		0,0,0,0
	} ;
	
	findPath(0,0,4,maze,mzpath) ;
	printPath(mzpath) ;

}


/***************************************************************/
int findPath( int i, int j, int n, int A[4][4], int path[4][4]) {
	
	// Check if the END of array ( destination ) is reached 
	if( i == n-1 && j == n-1) {
		path[i][j] = 1 ;
		return 1;
	}

	// Check if EVERY Cell is EMPTY (1) OR BLOCKED (0)
	if ( A[i][j] == 1 ) {  // Cell is EMPTY
		path[i][j] = 1 ; // Keep track of Cell & add Cell to Path

		// Check if you can move to the RIGHT side of the Cell Next COL: j+1
		if ( findPath(i, j+1, n, A, path) )
			return 1;

		// Check if you can move to the DOWN side of the Cell Next ROW : i+1 
		if ( findPath(i+1, j, n, A, path) )
			return 1;

		// If there are NO EMPTY Cells RIGHT or DOWN, GO BACK ( and remove Cell from the path )
		path[i][j] = 0 ;
	}

	// Other way NO PATH found to go . Return False (0)
	return 0;
}

/***************************************************************/
void printPath(int path[4][4]) {

	int i,j ;

	for(i=0; i<4; i++) {
		for(j=0; j<4; j++)
			if( path[i][j] == 1) {
				printf("(%d,%d)---> ",i,j );
				printf("\n") ;
			}
	}
}
