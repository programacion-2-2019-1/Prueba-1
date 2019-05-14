def rotar(x,y,angulo):
    ''' Se retorna un arreglo x, y modificado rotando el valor de angulo (en rads) respecto a (0,0) '''
    xr = [];   yr = []
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

def pendiente(x,y):
    ''' retorna la pendiente en rads de los arreglos x,y (dos elementos)'''
    dy = y[1]-y[0]
    dx = x[1]-x[0]
    m  = dy/dx
    return m
