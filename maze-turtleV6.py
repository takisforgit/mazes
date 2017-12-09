from turtle import *

### Set Start position ####
def setStartPosition():
	global boxSize, startPosition, endPosition, size_X, size_Y
	startX = -size_X * 20
	startY = -size_Y * 20
	startPosition=(startX, startY)
	# print("AREA StartPosition:", startPosition)

################# Draw rectangle #########################
def rect(startX, startY, boxSize):
	pu()
	goto(startX, startY)
	pd()
	for i in range(4):
		fd(boxSize)
		lt(90)
	pu()

#### MOVE Right ####
def moveRight():
	global boxSize, startPosition, endPosition
	pu()
	checkPos()
	rt(90)
	fd(boxSize)
	dot("red")
	print(int(pos()[0]), int(pos()[1])	)
	pu()

#### MOVE Left ####
def moveLeft():
	global boxSize, startPosition, endPosition
	pu()
	checkPos()
	lt(90)
	fd(boxSize)
	dot("red")
	print(int(pos()[0]), int(pos()[1])	)
	pu()


def moveForward():
	global boxSize, startPosition, endPosition
	pu()
	checkPos()
	fd(boxSize)
	dot("red")
	print(int(pos()[0]), int(pos()[1])	)
	pu()


def moveBack():
	global boxSize, startPosition, endPosition
	pu()
	checkPos()
	rt(180)
	fd(boxSize)
	dot("red")
	print(int(pos()[0]), int(pos()[1])	)
	pu()


#### Check Position - if turtle is INSIDE AREA ####
def checkPos():
	global startPosition, endPosition

	# print("startPosition:", startPosition)
	# print("stopPosition:", stopPosition)

	print(pos(), startPosition,endPosition )
	if( ((pos()[0] > startPosition[0]) and (pos()[1] > startPosition[1])) and (( pos()[0] < endPosition[0]) and (pos()[1] < endPosition[1]))  ):
	 # if( pos()[0] > startPosition[0] and pos()[0] < endPosition[0]) :
		print("Iside Area")
	else:
		print("Out of Area")

#### Check Right move if possible ####
def checkRight(step):
	global startPosition, endPosition

	print(pos(), startPosition,  endPosition )
	if( ( (int(pos()[0]+step) > startPosition[0]) and (int(pos()[0]+step < endPosition[0])) ) and  ( (int(pos()[1]+step) > startPosition[1]) and (int(pos()[1]+step < endPosition[1])) ) ) :
		return True
	else:
		return False


#### Check Left move if possible ####
def checkLeft(step):
	global startPosition, endPosition

	print(pos()[0], startPosition[0], pos()[1] ,startPosition[1] , pos()[0] ,endPosition[0],pos()[1] ,endPosition[1] )
	if( (float(pos()[0]+step) > startPosition[0]) and ( float(pos()[0]+step) < endPosition[0]))  :
		return True
	else:
		return False


################# Remove RIGHT line of rectangle #########################
def removeRightSide(startX, startY, boxSize):
	pu()
	goto(startX, startY)
	pencolor("yellow")
	# dot()
	setheading(0)
	pencolor("white")
	for i in range(1):
		fd(boxSize)
		lt(90)
	fd(1)
	pd()
	fd(boxSize-1)
	pencolor("black")
	pu()


################# Remove DOWN line of rectangle #########################
def removeDownSide(startX, startY, boxSize):
	pu()
	goto(startX, startY)
	pencolor("blue")
	# dot()
	setheading(0)
	pencolor("white")
	pd()
	fd(1)
	fd(boxSize-1)
	pencolor("black")
	pu()	

################# Main() #########################

def main():

	global boxSize, size_X, size_Y
	global startPosition, endPosition
	stack = []
	visited = []
	directions =["R", "L", "U", "D"]
	direction = ""
	count = 1
	size_X = 5
	size_Y = 5
	boxSize = 40
	startX = -size_X * 20
	startY = -size_Y * 20
	screen = Screen()
	# screen.setup(boxSize*size_X*3, boxSize*size_Y*3)
	screen.bgcolor('white')

	screen.onkey(moveForward, "Up")
	screen.onkey(moveRight, "Right")
	screen.onkey(moveLeft, "Left")
	screen.onkey(moveBack, "Down")
	screen.listen()

	pu()
	speed(0)
	ht()
	pensize(1)
	times = 0
	goto(0,0)

	### DRAW the Area ###
	### For each ROW of rectangles ###
	for i in range(size_Y):
		startPosition=(startX , startY)
		# print("Row startPosition:", startPosition)
		times = 0 
		## Print ROW NUMBERS on the left side ##
		goto(startX-boxSize, startY )
		# goto(startX - 40, startY)
		pd()
		write(i,  font=("Arial", 18, "normal"), align="left")
		### draw all COLUMNS of rectangles ###
		while times < size_X :

			rect(startX,startY, boxSize)
		## Print COLUMN NUMBERS on the bottom side- ONLY for 1st ROW ##
			if i==0:
				pu()
				goto(startX+boxSize*3/5, startY - 40)
				pd()
				write(times, font=("Arial", 18, "normal"), align="right")
				pu()

			## next Rectangle in the same ROW		
			times += 1
			startX = startX + boxSize 
			## Print NUMBERS inside rectangles ##
			goto(startX-boxSize/2, startY+5)
			pencolor("light green")
			write(count,  font=("Arial", 14, "normal"), align="center")
			pencolor("black")
			count+=1
		## DRAW next ROW 			
		startX = -size_X * 20
		startY = -size_Y * 20 + (i+1)*boxSize

		
		# print(pos())
		# print(xcor(), yxor())	
	endPosition = pos()
	# print("EndPosition:", endPosition)
	setStartPosition()

	
	startX = -size_X * 20
	startY = -size_Y * 20
	
	# goto(startX + boxSize/2 , startY + boxSize/2 )
	goto(startX , startY )
	st()	
	# dot("red")
	pu()	
	direction="R"
	# print(pos()[0], pos()[1])


	lista =[(0,0),(0,3),(1,0),(1,1),(2,3),(3,2),(3,3),(2,2),(4,1),(0,2),(4,0)]
	for item in lista:
		startX = -size_X * 20
		startY = -size_Y * 20
		# print(item[0], item[1])
		goto(startX, startY) 
		### Remove Right Side Bar  ###	
		cellX = -(size_X*20)+ ( (item[1]) * boxSize) 
		cellY = -(size_Y*20) + ( (item[0]) * boxSize) 
		removeRightSide(cellX, cellY, boxSize)
		


	listb =[(1,0),(2,0),(1,2),(1,4),(3,1),(2,1),(2,3),(4,2),(4,3),(3,3),(4,1),(4,0)]
	for item in listb:
		startX = -size_X * 20
		startY = -size_Y * 20
		# print(item[0], item[1])
		goto(startX, startY) 
		### Remove Right Side Bar  ###	
		cellX = -(size_X*20)+ ( (item[1]) * boxSize) 
		cellY = -(size_Y*20) + ( (item[0]) * boxSize) 
		removeDownSide(cellX, cellY, boxSize)
		
	speed("slowest")
	st()
	screen.mainloop()

	exitonclick()
  

if __name__ == '__main__':
    main()

