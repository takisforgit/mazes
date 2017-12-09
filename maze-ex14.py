#by Derek Vidovic
#draws a maze
#todo: convert from python to tkinter
#todo: make the maze always solvable
#todo: navigate the maze
from turtle import *
from random import *
import tkinter

#turtle note: x increases to the right; y increases up

EAST = 0;
NORTH = 90;
WEST = 180;
SOUTH = 270;

class Cell:
    SIDE = 25
    
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid

    #draw the cell with the provided Turtle
    #only draws north and west walls; other cells will do south and east
    #(unless this is a top or right cell)
    def draw(self, t):
        pos = self.getLowerLeftCorner()
        if self.grid.horizontals[self.y][self.x]:
            t.goto(pos[0], pos[1])
            t.setheading(EAST)
            t.pendown()
            t.fd(Cell.SIDE)
            t.penup()
        if self.grid.verticals[self.y][self.x]:
            t.goto(pos[0], pos[1])
            t.setheading(NORTH)
            t.pendown()
            t.fd(Cell.SIDE)
            t.penup()
        #top cell must handle top wall
        if self.y + 1 == self.grid.height and \
                self.grid.horizontals[self.y + 1][self.x]:
            pos = self.getUpperRightCorner()
            t.goto(pos[0], pos[1])
            t.setheading(WEST)
            t.pendown()
            t.fd(Cell.SIDE)
            t.penup()
        #right cell must handle right wall
        if self.x + 1 == self.grid.width and \
                self.grid.verticals[self.y][self.x + 1]:
            pos = self.getUpperRightCorner()
            t.goto(pos[0], pos[1])
            t.setheading(SOUTH)
            t.pendown()
            t.fd(Cell.SIDE)
            t.penup()
        #start cell must fill itself
        #TODO; need tkinter for this
            

    def getLowerLeftCorner(self):
        return (Cell.SIDE * (self.x - self.grid.halfwidth - 1/2),
                Cell.SIDE * (self.y - self.grid.halfheight - 1/2))
    def getUpperRightCorner(self):
        pos = self.getLowerLeftCorner()
        return (pos[0] + Cell.SIDE, pos[1] + Cell.SIDE)

class Grid:
    #startCell: cell where you begin, in a tuple (r,c)    
    def __init__(self, width, height, startCell=(0,0)):
        self.width = width
        self.height = height
        self.halfwidth = width/2
        self.halfheight = height/2
        self.cells = []#array of arrays: [r][c], going up and right
        
        for r in range(height):
            self.cells.append([]);
            for c in range(width):
                self.cells[r].append(Cell(y=r, x=c, grid=self))
        
        #array of arrays. [r][c] is the west wall of cell[r][c]
        self.verticals = []
        #array of arrays. [r][c] is the south wall of cell[r][c]
        self.horizontals = []
        for r in range(height + 1):
            self.verticals.append([])
            self.horizontals.append([])
            for c in range(width + 1):
                self.verticals[r].append(False)
                self.horizontals[r].append(False)
        self.startCell = self.cells[startCell[0]][startCell[1]]
                

    #(re)draw the entire grid with the provided Turtle
    def draw(self, t):
        t.penup()
        for row in self.cells:
            for cell in row:
                cell.draw(t)

    def randomizeWalls(self, wallChance):
        for r in range(len(self.verticals)):
            for c in range(len(self.verticals[r])):
                self.verticals[r][c] = random() < wallChance
                self.horizontals[r][c] = random() < wallChance

    #sets all exterior walls to wallsOn
    #call this with True to make the maze completely enclosed
    def putExteriorWalls(self, wallsOn=True):
        for r in range(len(self.verticals)):
            self.verticals[r][0] = wallsOn
            #print 'V['+str(r)+'][0]'
            self.verticals[r][len(self.verticals[r]) - 1] = wallsOn
            #print 'V['+str(r)+']['+str(len(self.verticals[r])-1)+']'
        for c in range(len(self.horizontals[0])):
            self.horizontals[0][c] = wallsOn
            #print 'H[0]['+str(c)+']'
            self.horizontals[len(self.horizontals) - 1][c] = wallsOn
            #print 'H['+str(len(self.horizontals)-1)+']'

window = tkinter.Tk()
window.title('Derek Vidovic: Maze Program')
g = Grid(4,4)
t = Turtle()
t.speed(0)
t.hideturtle()
g.randomizeWalls(0.45)
g.putExteriorWalls()
g.draw(t)
