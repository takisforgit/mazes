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


################# Main() #########################

def main():

	pu()
	count = 1
	size_X = 3
	size_Y = 3

	boxSize = 40
	startX = -size_X * 20
	startY = -size_Y * 20

	speed(0)
	ht()
	pensize(2)
	# print(pos()[0], pos()[1]) 
	times = 0
	goto(0,0)

	### For each ROW of rectangles ###
	for i in range(size_Y):
		times = 0 
		## Print ROW NUMBERS on the left side ##
		goto(startX - 40, startY)
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


	
	### FILL the Rectangle with color  ###	
	goto(-(size_X*20)+5 , -(size_Y*20)+boxSize-5 )
	penup()
	begin_fill()
	pendown()
	color("yellow")
	for x in range(4):
		fd(boxSize-10)
		rt(90)
	end_fill()

	goto(-size_X * 20 + boxSize/2 , -size_Y * 20 + boxSize/2 )
	st()	

	pu()		







	exitonclick()
  

if __name__ == '__main__':
    main()

