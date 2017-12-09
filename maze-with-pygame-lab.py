"""
http://codes-sources.commentcamarche.net/source/view/51293/1217736#browser

Laby , par Mehdi Cherti 2010 (mehdidc): 
	- generation d'un labyrinthe
	- utilisation de l'algorithme astar pour trouver le chemin le plus court (selection de la destination avec la souris)
"""

from  random import randint , choice
import pygame
from pygame.locals import *
import def_const
from math import sqrt

const = def_const.def_const ()
""" definitions des constantes """

# Couleurs
const.white  = (255 , 255 , 255)
const.pink   = (255 , 0 , 255)
const.black  = (0 , 0 , 0)
const.yellow = (255 , 255 , 0)

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
		self.portes = [True , True , True , True] # Right, Left, Up, Down
		
""" distance : retourne la distance euclidienne entre deux points """
def distance (p1 , p2):
	return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


""" classe Personnage """
class Perso:
	def __init__ (self,lab):
		self.x = 1
		self.y = 1
		self.chemin =None
		self.laby = lab
		self.color = const.yellow
	""" affichage """	
	def show(self,buffer):
		a,b = const.perso_radius , const.perso_radius
		pygame.draw.circle (buffer, self.color , (a+self.laby.sx+self.x*self.laby.wc,b+self.laby.sy+self.y*self.laby.hc) , 
		int(const.perso_radius) )
		
	""" mouvement selon la direction"""
	def move (self,dir):
			
		if not self.laby.get_cell (self.x , self.y).portes[dir]:
			if dir == const.right and self.x+1 < self.laby.w :
				self.x += 1
			if dir == const.left and self.x-1 >=0:
				self.x -= 1
			if dir == const.up and self.y-1 >=0:
				self.y -= 1
			if dir == const.down and self.y+1 < self.laby.h:
				self.y += 1
				
	""" fonction utilisÃ©e par astar pour traiter une des cases adjacentes"""
	def traitement (self ,  liste_fermee , liste_ouverte , x ,  y , dir ,parent ,dest):
		if parent.portes[dir] : return
		c = self.laby.get_cell (x,y)
		if c in liste_fermee : return
		
		if c in liste_ouverte:
			G = distance ( (x,y) , (parent.x , parent.y))
			c.dir = self.laby.notdir (dir)
			if G < c.G:
				c.G = G
				c.F = c.H + c.G
				c.parent = parent
		else:
			c.parent = parent
			c.dir = self.laby.notdir (dir)
			c.G = distance ( (x,y) , (parent.x , parent.y))
			c.H = distance ( (x,y) , (dest.x ,dest.y))
			c.F = c.G + c.H
			liste_ouverte.append (c)
	""" retourne , aprÃ¨s avoir trouvÃ© le chemin avec astar , un tableau contenant le chemin"""
	def  get_astar (self, csource , cdest):
		
		source = self.laby.get_cell (csource[0] , csource[1])
		dest = self.laby.get_cell (cdest[0] , cdest[1])
		cur=dest
		chemin = []
		while cur and (cur.x != source.x or cur.y != source.y):
			if cur.x == cur.parent.x-1 :
				chemin.append (const.right)
			if cur.x == cur.parent.x+1:
				chemin.append (const.left)
			if cur.y == cur.parent.y+1:
				chemin.append (const.up)
			if cur.y == cur.parent.y-1:
				chemin.append (const.down)
			cur = cur.parent
		
		ret = []
		id = len(chemin) - 1
		while id>=0:
			ret.append (self.laby.notdir(chemin[id]))
			id-=1
		return ret
		
	""" mise a jour de la position du personnage """
	def poll(self):
		if self.chemin:
			self.move (self.chemin.pop (0))
			
	""" permet de se deplacer selon le chemin """
	def aller(self,chemin):
		self.chemin = chemin
			
	"""
	algorithme de pathfinding Astar , desti represente le tuple de la destination
	"""
	def astar (self , desti):
		dest = Point(desti)
		liste_ouverte = []
		liste_fermee = []


		debut = self.laby.get_cell (self.x , self.y)
		liste_ouverte.append (debut)
		debut.F = distance ((self.x,self.y) , (dest.x,dest.y))
		debut.G = 0
		debut.H = debut.F
		debut.parent = None
		
		
		while 1:
			if len(liste_ouverte) <= 0 : 
				break
			min , min_id= liste_ouverte[0].F,0
					
			for id,v in enumerate(liste_ouverte[1:]):
				if v < min :
					min = v
					min_id = id +1
			liste_fermee.append (liste_ouverte[min_id])
			
			if liste_ouverte[min_id].x == dest.x and liste_ouverte[min_id].y == dest.y : break
			
			self.traitement (liste_fermee,liste_ouverte,liste_ouverte[min_id].x +  1 , liste_ouverte[min_id].y , const.right , liste_ouverte[min_id] , dest)
			self.traitement (liste_fermee,liste_ouverte,liste_ouverte[min_id].x -  1 , liste_ouverte[min_id].y , const.left , liste_ouverte[min_id] , dest)
			self.traitement (liste_fermee,liste_ouverte,liste_ouverte[min_id].x  , liste_ouverte[min_id].y-1 , const.up , liste_ouverte[min_id] , dest)
			self.traitement (liste_fermee,liste_ouverte,liste_ouverte[min_id].x  , liste_ouverte[min_id].y+1 , const.down , liste_ouverte[min_id] , dest)
			liste_ouverte.remove (liste_ouverte[min_id])


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
		cell_act = self.get_cell (x,y)
		
		if not cell_act.state :
			cell_act.state = True
			tab = []
			if x+1<self.w and not self.get_cell(x+1,y).state : tab.append((x+1,y,const.right))
			if x-1>=0  and not self.get_cell(x-1,y).state    : tab.append((x-1,y,const.left))
			if y-1>=0  and not self.get_cell(x,y-1).state   : tab.append((x  ,y-1,const.up))
			if y+1<self.h and not self.get_cell(x,y+1).state : tab.append((x  ,y+1,const.down))
			if tab:
				
				while tab:
					C = choice (tab)
					if not self.get_cell(C[0] , C[1]).state:
						
						cell = self.get_cell (C[0] , C[1])
						cell_act.portes[C[2]] = False
						cell.portes[self.notdir(C[2])] = False
						self.generate_laby (C[0] , C[1])
					tab.remove (C)
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
					pygame.draw.line (buffer , const.white , (sx+(x+1)*W,sy+y*H),(sx+(x+1)*W,sy+(y+1)*H))
				if c.portes[const.down] :
					pygame.draw.line (buffer , const.white , (sx+(x)*W,sy+(y+1)*H),(sx+(x+1)*W,sy+(y+1)*H))

		x = self.w - 1

		for y in range(self.h-1):
			c = self.get_cell (x , y)
			if c.portes[const.down]:
				pygame.draw.line (buffer , const.white , (sx+x*W,sy+(y+1)*H),(sx+(x+1)*W,sy+(y+1)*H) )

		y = self.h - 1
		for x in range(self.w-1):
			c = self.get_cell (x , y)
			if c.portes[const.right]:
				pygame.draw.line (buffer , const.white , (sx+(x+1)*W,sy+(y)*H),(sx+(x+1)*W,sy+(y+1)*H) )
		pygame.draw.rect (buffer , const.pink , (sx , sy , W * self.w , H * self.h),2)
		


if __name__ == "__main__":
	
	mylaby = laby(20,20) # crÃ©ation d'un labyrinthe de 20x20 cellules
	pygame.init ()
	pygame.display.set_mode ( (640,480))
	screen = pygame.display.get_surface ()
	
	mylaby.generate_laby() # gÃ©neration alÃ©atoire du labyrinthe

	perso = Perso (mylaby)
	keys = None
	move_time = 0
	perso_time = 0


	while True:
		screen.fill (const.black)
		events = pygame.event.get ()
		
		for event in events:
		
			""" click de la souris """
			if event.type == MOUSEBUTTONDOWN:
				mx , my = pygame.mouse.get_pos ()
				x = (mx - mylaby.sx) / mylaby.wc
				y = (my - mylaby.sy) / mylaby.hc
				if x>=0 and y>=0 and x < mylaby.w and y < mylaby.h:
					perso.astar ((x,y)) # trouve le chemin avec astar
					chemin = perso.get_astar ((perso.x,perso.y) , (x,y)) # reÃ§oit le chemin en tableau qui donne les directions Ã  prendre sequentiellement
					perso.aller (chemin) # ordonne au personnage d'aller au chemin sans arrÃªter la boucle principale
					
		keys = pygame.key.get_pressed ()
		
		""" Mouvement du personnage """
		if pygame.time.get_ticks () - move_time >= const.time_perso:
			move_time = pygame.time.get_ticks ()	
			if keys[pygame.K_RIGHT]:
				perso.move (const.right)
			if keys[pygame.K_LEFT]:
				perso.move (const.left)
			if keys[pygame.K_UP]:
				perso.move (const.up)
			if keys[pygame.K_DOWN]:
				perso.move (const.down)
			
		if keys[pygame.K_ESCAPE] :
			break
			
		""" mise a jour de la position du personnage """
		if pygame.time.get_ticks () - perso_time >= const.time_perso_poll:
			perso_time = pygame.time.get_ticks ()
			perso.poll ()
			
		""" affichage """
		mylaby.show (screen)
		perso.show (screen)
		pygame.display.flip ()
