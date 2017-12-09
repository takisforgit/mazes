# -*- coding: utf8 -*-
class def_const:
	"""
	Definitions des constantes en python
	"""
	def __getattr__(self,attr):
		return Const.__dict__[attr]
		
	def __setattr__ (self , attr,value):
		if attr in self.__dict__.keys ():
			raise Exception("Impossible de redÃ©finir une constante")
		else :
			self.__dict__[attr] = value
		
	def __str__ (self):
		return self.__dict.__str__ ()
