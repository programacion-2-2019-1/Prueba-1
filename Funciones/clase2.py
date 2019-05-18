import numpy as np

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
		return xr,yr

	def otro(self):
		pass
		