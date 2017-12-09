from turtle import *


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




#### Check Position ####
def checkPos():
	global startPosition, endPosition

	print(pos()[0], startPosition[0], pos()[1] ,startPosition[1] , pos()[0] ,endPosition[0],pos()[1] ,endPosition[1] )
	# if(  (pos()[0] > startPosition[0]) and (pos()[1] > startPosition[1]) and ( pos()[0] < endPosition[0]) and (pos()[1] < endPosition[1])  ) :
	if( pos()[0] > startPosition[0] and pos()[0] < endPosition[0]) :
		print("Iside Area")
	else:
		print("Out of Area")


################# Main() #########################

def main():

	global boxSize
	global startPosition, endPosition
	stack = []
	visited = []
	count = 1
	size_X = 5
	size_Y = 5
	boxSize = 40
	startX = -size_X * 20
	startY = -size_Y * 20
	screen = Screen()
	screen.setup(boxSize*size_X*3, boxSize*size_Y*3)
	screen.bgcolor('white')

	screen.onkey(moveForward, "Up")
	screen.onkey(moveRight, "Right")
	screen.onkey(moveLeft, "Left")
	screen.onkey(moveBack, "Down")
	screen.listen()

	pu()
	speed(0)
	ht()
	pensize(2)
	times = 0
	goto(0,0)

	### DRAW the Area ###
	### For each ROW of rectangles ###
	for i in range(size_Y):
		times = 0 
		## Print ROW NUMBERS on the left side ##
		startPosition=(startX - boxSize, startY)
		print("startPosition:", startPosition)
		goto(startPosition)
		# goto(startX - 40, startY)
		pd()
		write(i+1,  font=("Arial", 18, "normal"), align="left")
		### draw all COLUMNS of rectangles ###
		while times < size_X :

			rect(startX,startY, boxSize)
		## Print COLUMN NUMBERS on the bottom side- ONLY for 1st ROW ##
			if i==0:
				pu()
				goto(startX+boxSize*3/5, startY - 40)
				pd()
				write(times+1, font=("Arial", 18, "normal"), align="right")
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

		
		print(pos())
		# print(xcor(), yxor())	
	endPosition = pos()
	print("EndPosition:", endPosition)

	### FILL the Rectangle with color  ###	
	# goto(-(size_X*20)+5 , -(size_Y*20)+boxSize-5 )
	# penup()
	# begin_fill()
	# pendown()
	# color("yellow")
	# for x in range(4):
	# 	fd(boxSize-10)
	# 	rt(90)
	# end_fill()

	goto(-size_X * 20 + boxSize/2 , -size_Y * 20 + boxSize/2 )
	st()	
	dot("red")
	pu()		
	print(pos()[0], pos()[1])

	speed("slowest")
	# while ( pos()[0] > startPosition[0] and pos()[1] > startPosition[1] \
	# 	and pos()[0] < endPosition[0] and pos()[1] < endPosition[1]  ) :

	screen.mainloop()



	exitonclick()
  

if __name__ == '__main__':
    main()

