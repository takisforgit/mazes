from turtle import *


################# Draw rectangle #########################
def rect(startX, startY, boxSize):
	pu()
	goto(startX, startY)
	pd()
	fd(boxSize)
	lt(90)
	fd(boxSize)
	lt(90)
	fd(boxSize)
	lt(90)
	fd(boxSize)
	lt(90)
	fd(boxSize)
	# lt(180)
	pu()

#### MOVE Right ####
def moveR():
	global boxSize, startPosition, endPosition
	checkPos()
	rt(90)
	fd(boxSize)
	dot("red")
	print(int(pos()[0]), int(pos()[1])	)


#### MOVE Left ####
def moveL():
	global boxSize, startPosition, endPosition
	checkPos()
	lt(90)
	fd(boxSize)
	dot("red")
	print(int(pos()[0]), int(pos()[1])	)

def moveF():
	global boxSize, startPosition, endPosition
	checkPos()
	fd(boxSize)
	dot("red")
	print(int(pos()[0]), int(pos()[1])	)


def moveB():
	global boxSize, startPosition, endPosition
	checkPos()
	rt(180)
	fd(boxSize)
	dot("red")
	print(int(pos()[0]), int(pos()[1])	)




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

	screen = Screen()
	screen.setup(500, 500)
	screen.bgcolor('white')

	screen.onkey(moveF, "Up")
	screen.onkey(moveR, "Right")
	screen.onkey(moveL, "Left")
	screen.onkey(moveB, "Down")
	screen.listen()

	stack = []
	visited = []
	pu()
	count = 1
	size_X = 3
	size_Y = 3

	global boxSize
	global startPosition, endPosition
	boxSize = 40
	startX = -size_X * 20
	startY = -size_Y * 20

	speed(0)
	ht()
	pensize(2)
	# print(pos()[0], pos()[1]) 
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
			write(count, font=("Arial", 14, "normal"), align="center")
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
	pu()		
	print(pos()[0], pos()[1])

	speed("slowest")
	# while ( pos()[0] > startPosition[0] and pos()[1] > startPosition[1] \
	# 	and pos()[0] < endPosition[0] and pos()[1] < endPosition[1]  ) :

	screen.mainloop()



	exitonclick()
  

if __name__ == '__main__':
    main()

