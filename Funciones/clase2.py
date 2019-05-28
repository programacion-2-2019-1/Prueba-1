import numpy as np
import operator

class Figura(object):
	"""docstring for Figura"""
	def __init__(self):
		super(Figura, self).__init__()
		self.arg = 1
		self.x = [-1,1,0,-1]
		self.y = [0,0,1.5,0]

	def rotar(self,angulo):
		''' Se retorna un arreglo x, y modificado rotando el valor de angulo (en rads) respecto a (0,0) '''
		xr = [];   yr = []
		x = self.x
		y = self.y
		for i in range(len(x)):
			if x[i] == 0:
				if y[i] >0:
					ang = np.pi/2
				else:
					ang = -np.pi/2
				r   = y[i]
			else:
				ang = np.math.atan(y[i]/x[i])
				r   = x[i]/np.math.cos(ang)
			xt  = r*np.math.cos(ang+angulo)
			yt  = r*np.math.sin(ang+angulo)
			xr.append(xt);   yr.append(yt);
		self.x = xr
		self.y = yr
		#return xr,yr

	def reset(self):
		self.x = [-1,1,0,-1]
		self.y = [0,0,1.5,0]

	def mover(self,x,y):
		''' Esta función permite desplazar la figura '''
		x2 = np.ones(len(self.x))*x
		tmp = map(operator.add,self.x,x2)
		self.x = list(tmp)
		y2 = np.ones(len(self.y))*y
		tmp = map(operator.add,self.y,y2)
		self.y = list(tmp)
		pass

	def ampliar(self,k_x,k_y):
		for i in range(len(self.x)):
			self.x[i] = self.x[i]*k_x
			self.y[i] = self.y[i]*k_y
		
		