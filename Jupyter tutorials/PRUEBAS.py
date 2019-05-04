# Aguilar Mayo 02, Ok

#import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def cruces(r,s):
    ''' Función para calcular los valores x de cruce entre el arreglo r y el arreglo s '''
    y = [] ;  x = []
    for i in range (6):
        if r[i]<s[i] and s[i+1]<r[i+1]:
            # calcular ec de recta -> y0 = m * x0 + b
            m1 = r[i+1]-r[i] ; m2 = s[i+1]-s[i]
            b1 = r[i] - m1 * i ; b2 = s[i] - m2 * i
            xc = (b2-b1)/(m1-m2)
            yc = m1*xc+b1
            x.append(xc)
            y.append(yc)        


    return x , y  
def cruces2(r,s):
    x = [] ; y = []
    for i  in range (6):
        if s[i]<r[i] and r[i+1]<s[i+1]:
            # calcular ec de recta -> y0 = m * x0 + b
            m1 = r[i+1]-r[i] ; m2 = s[i+1]-s[i]
            b1 = r[i] - m1 * i ; b2 = s[i] - m2 * i 
            xc = (b2-b1)/(m1-m2)
            yc = m1*xc+b1
            x.append(xc)
            y.append(yc)
        
    return x , y
    
limite = 8
n = 7 # cantidad de puntos
r = np.random.randint(-limite,limite+1,n)  # Números aleatorios enteros
s = np.random.randint(-limite,limite+1,n)

xc2 ,yc2 = cruces2(r,s) 
xc , yc = cruces(r,s)


fig, ax = plt.subplots()
ax.plot(r,'o-')  # graficar puntos
ax.plot(s,'o--')
ax.plot(xc,yc,"ro")
ax.plot(xc2,yc2,"ro")
ax.set(xlabel='Eje X', ylabel='Eje Y',title='Números aleatorios')
ax.grid(); ax.axis([0,n,-limite-1,limite+1])



fig.savefig("aleatorios.png")
plt.show()

    
        
