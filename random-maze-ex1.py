from random import *

seed = 12345

#### Main #####
# height = randint(4,10)
# width = randint(4,10)

height = 14
width = 14
print(height,width)

mazeR = []
rowR = []

## Fill Walls ( first row ) ###
for i in range(width):
	rowR.append(0) ## first row wall
mazeR.append(rowR)


for i in range(2,height):
	rowR = []
	rowR.append(0) ## first column wall
	for j in range(1,width-1):
		x = randint(0,1)
		rowR.append(x)
	rowR.append(0) ## last column wall
	# print(rowR)
	mazeR.append(rowR)

## Fill Walls ( last row ) ###
rowR = []
for i in range(width):
	rowR.append(0) ## last row wall
mazeR.append(rowR)

count = 0
for row in mazeR:
	print("Row: %2d   %s"%(count,row))
	count+=1

# print(mazeR)