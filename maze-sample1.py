from  random import randint , choice
import pygame
from pygame.locals import *
import def_const
from math import sqrt

import time


const = def_const.def_const ()
""" definitions des constantes """

# Couleurs
const.white  = (255 , 255 , 255)
const.pink   = (255 , 0 , 255)
const.black  = (0 , 0 , 0)
const.yellow = (255 , 255 , 0)
const.red = (255 , 0 , 0)


#directions 
const.right = 0
const.left = 1
const.up = 2
const.down = 3

# autres

const.wc = 20 # width d'un seul carreau du laby
const.hc = 20# height d'un seul carreau du laby

const.perso_radius = const.wc//2 # rayon du personnage (qui est un cercle)
const.time_perso = 100 # temps en ms avant chaque test du clavier pour les touches qui concernent le perso
const.time_perso_poll = 50 # temps en ms avant chaque mise a jour de la position du perso
""" fin definitions des constantes"""

class Point:
	def __init__ (self,xy):
		self.x = xy[0]
		self.y = xy[1]

""" Definition de la classe cellule de labyrinthe"""
class cellule:
	def __init__(self):
		self.state = False
		self.portes = [True , True , True , True] # Droite , Gauche , Haut , Bas
		
""" distance : retourne la distance euclidienne entre deux points """
def distance (p1 , p2):
	return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)



""" classe du labyrinthe """
class laby:
	def __init__ (self,w,h,sx=0,sy=0):
		self.w = w
		self.h = h
		self.cellules = []
		self.wc = const.wc
		self.hc = const.hc
		self.sx = sx
		self.sy = sy
		""" initialisation des cellules , pour chaque cellule , il initialise sa position dans le labyrinthe """
		for v in range(self.w*self.h):
			a = cellule()
			a.x = v % self.w
			a.y = v / self.w
			self.cellules.append (a)
			# print(a.x, a.y, a.state, a.portes)
			# print(v,self.cellules[v])
	""" retourne la cellule correspondante Ã  la position (x,y) """
	def get_cell (self,x,y):
		return self.cellules[x +  y * self.w]
	""" retourne direction de sens contraire d'une direction """
	def notdir(self,dir):
		if dir == const.right : return const.left
		if dir == const.left : return const.right
		if dir == const.up : return const.down
		if dir == const.down : return const.up
		
	""" generation du labyrinthe """
	def generate_laby (self,x=-1,y=-1):
		if x==-1:
			x = randint(0,self.w-1)
			y = randint(0,self.h-1)
			print("Random Col=",x,"Row=",y)
		cell_act = self.get_cell (x,y)
		
		if not cell_act.state :
			cell_act.state = True
			tab = []
			if x+1<self.w and not self.get_cell(x+1,y).state : tab.append((x+1,y,const.right))
			if x-1>=0  and not self.get_cell(x-1,y).state    : tab.append((x-1,y,const.left))
			if y-1>=0  and not self.get_cell(x,y-1).state   : tab.append((x  ,y-1,const.up))
			if y+1<self.h and not self.get_cell(x,y+1).state : tab.append((x  ,y+1,const.down))
			
			print(x,y,tab)

			if tab:
				
				while tab:
					C = choice (tab)
					print("Choice :", C, C[0], C[1], self.get_cell(C[0] , C[1]).state)
					if not self.get_cell(C[0] , C[1]).state:
						
						cell = self.get_cell (C[0] , C[1])
						cell_act.portes[C[2]] = False
						cell.portes[self.notdir(C[2])] = False
						# self.generate_laby (C[0] , C[1])

					print(x,y,tab)

					tab.remove (C)
					# print(tab)	
				return True
			else : 
				return False
		

	""" affiche le labyrinthe """
	def show(self,buffer):
		W,H = self.wc , self.hc
		sx,sy = self.sx , self.sy
		for y in range(self.h-1):
			for x in range(self.w-1):
				c = self.get_cell (x,y)
				if c.portes[const.right] :
					pygame.draw.line (buffer , const.red , (sx+(x+1)*W,sy+y*H),(sx+(x+1)*W,sy+(y+1)*H))
				if c.portes[const.down] :
					pygame.draw.line (buffer , const.white , (sx+(x)*W,sy+(y+1)*H),(sx+(x+1)*W,sy+(y+1)*H))

		# x = self.w - 1

		# for y in range(self.h-1):
		# 	c = self.get_cell (x , y)
		# 	if c.portes[const.down]:
		# 		pygame.draw.line (buffer , const.white , (sx+x*W,sy+(y+1)*H),(sx+(x+1)*W,sy+(y+1)*H) )

		# y = self.h - 1
		# for x in range(self.w-1):
		# 	c = self.get_cell (x , y)
		# 	if c.portes[const.right]:
		# 		pygame.draw.line (buffer , const.white , (sx+(x+1)*W,sy+(y)*H),(sx+(x+1)*W,sy+(y+1)*H) )
		# pygame.draw.rect (buffer , const.pink , (sx , sy , W * self.w , H * self.h),2)
		


if __name__ == "__main__":
	
	mylaby = laby(3,4) # crÃ©ation d'un labyrinthe de 20x20 cellules
	pygame.init ()
	pygame.display.set_mode ( (640,480))
	screen = pygame.display.get_surface ()
	
	mylaby.generate_laby() # gÃ©neration alÃ©atoire du labyrinthe

	# perso = Perso (mylaby)
	keys = None
	move_time = 0
	perso_time = 0
	flag = True
	while flag:
		mylaby.show (screen)
		# perso.show (screen)
		pygame.display.flip ()
		time.sleep(5)    # pause 5.5 seconds
		flag = False