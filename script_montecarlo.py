from math import *
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


plt.clf()

plt.axis([-0.1, pi+0.1, -0.2, pi/2+0.2])
plt.axhline(c='k')# l'axe des abscisses, en noir
plt.axvline(c='k')# l'axe des ordonnées

# on trace la courbe de sin :
x=np.linspace(0,pi,1000)
y=np.sin(x)
plt.plot(x,y,'go',markersize=0.5) 

# on trace les deux segments :

plt.plot([0,pi/2],[0,pi/2],'go-',markersize=1)
plt.plot([pi/2,pi],[pi/2,0],'go-',markersize=1)

# tester différentes valeurs pour n
n=50
r=0
def f(x):
    if x<(pi/2):
        return x
    else:
        return pi-x
        
for i in range(n):
    x=random.random()*pi
    y=random.random()*pi/2
    if y<=f(x) and y>=sin(x):
        plt.plot(x,y,'ro',markersize=2)
        r=r+1
    else: 
        plt.plot(x,y,'bo',markersize=2)
        
aire_rectangle=pi/2*pi

plt.text(0.3,-0.1,'n= '+str(n)+'; r= '+str(r)+'; proba = '+str(r/n*aire_rectangle),color='red')


#On dessine le rectangle
plt.plot([0,pi,pi,0,0],[0,0,pi/2,pi/2,0],'k',markersize=2)
rectangle = plt.Rectangle((0,0), pi, pi/2, fc='lightblue')
plt.gca().add_patch(rectangle)

plt.show()
plt.close()
