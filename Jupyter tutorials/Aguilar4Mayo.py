
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as ns

    
limite = 10
n = ns.randint(1,10) # cantidad de puntos
m = ns.randint(1,10)

r = np.random.randint(-limite,limite+1,n)  # Números aleatorios enteros
s = np.random.randint(-limite,limite+1,m)

#contador=0
def cruces1 (r,s):
    x = [] ; y = []
    if len(r)<=len(s):
        for i in range (len(r)-1):
            if r[i]<s[i] and s[i+1]<r[i+1]:
                # calcular ec de recta -> y0 = m * x0 + b
                m1 = r[i+1]-r[i] ; m2 = s[i+1]-s[i]
                b1 = r[i] - m1 * i ; b2 = s[i] - m2 * i
                xc = (b2-b1)/(m1-m2)
                yc = m1*xc+b1
                x.append(xc)
                y.append(yc)
    

    z = [] ; w = []
    if len(s)<=len(r):
        for i in range (len(s)-1):
            if r[i]<s[i] and s[i+1]<r[i+1]:
                # calcular ec de recta -> y0 = m * x0 + b
                m1 = r[i+1]-r[i] ; m2 = s[i+1]-s[i]
                b1 = r[i] - m1 * i ; b2 = s[i] - m2 * i
                xc = (b2-b1)/(m1-m2)
                yc = m1*xc+b1
                z.append(xc)
                w.append(yc)
    
    return x,y,z,w

def cruces2 (r,s):
    x = [] ; y = []
    if len(r)<=len(s):
        for i in range (len(r)-1):
            if s[i]<r[i] and r[i+1]<s[i+1]:
                # calcular ec de recta -> y0 = m * x0 + b
                m1 = r[i+1]-r[i] ; m2 = s[i+1]-s[i]
                b1 = r[i] - m1 * i ; b2 = s[i] - m2 * i
                xc = (b2-b1)/(m1-m2)
                yc = m1*xc+b1
                x.append(xc)
                y.append(yc)
    

    z = [] ; w = []
    if len(s)<=len(r):
        for i in range (len(s)-1):
            if s[i]<r[i] and r[i+1]<s[i+1]:
                # calcular ec de recta -> y0 = m * x0 + b
                m1 = r[i+1]-r[i] ; m2 = s[i+1]-s[i]
                b1 = r[i] - m1 * i ; b2 = s[i] - m2 * i
                xc = (b2-b1)/(m1-m2)
                yc = m1*xc+b1
                z.append(xc)
                w.append(yc)
    
    return x,y,z,w

xc2 , yc2 , zc2 , wc2 = cruces2(r,s)

xc1 , yc1 , zc1 , wc1 = cruces1(r,s)

fig, ax = plt.subplots()
ax.plot(r,'o-')  # graficar puntos
ax.plot(s,'o--')
ax.plot(xc1,yc1,"ro")
ax.plot(zc1,wc1,"ro")
ax.plot(xc2,yc2,"ro")
ax.plot(zc2,wc2,"ro")

ax.set(xlabel='Eje X', ylabel='Eje Y',title='Números aleatorios')
ax.grid(); ax.axis([0,n,-limite-1,limite+1])



fig.savefig("aleatorios.png")
plt.show()




