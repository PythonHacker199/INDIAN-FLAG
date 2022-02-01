# HEY GUYS WELCOME BACK 
# LET'S GET Started

pip install matplotlib 

import matplotlib.pyplot as plt
import matplotlib.patches as patch

a=patch.Rectangle((0,1),width=12,height=2,facecolor='green',edgecolor='grey')
b=patch.Rectangle((0,3),width=12,height=2,facecolor='white',edgecolor='grey')
c=patch.Rectangle((0,5),width=12,height=2,facecolor='#FF9933',edgecolor='grey')

n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

radius=0.8
py.plot((6,4),marker='o',makerfacecolor='000088ff',markersize=9.5)
chakra=py.Circle((6,4),radius,color='000088ff',fill=False,linewidth=7)

n.add_artist(chakra)

for i in range (0,24):
	p=6+radius/2 * np.cos(np.pi*i/12+ np.pi/48)
	q=6+radius/2 * np.cos(np.pi*i/12+ np.pi/48)
	r=4+radius/2 * np.sin(np.pi*i/12+ np.pi/48)
	p=4+radius/2 * np.sin(np.pi*i/12+ np.pi/48)
	p=6+radius/2 * np.cos(np.pi*i/12)
	p=4+radius/2 * np.sin(np.pi*i/12)

n.add_patch(patch.polygon([[6,4],[p,r],[t,u],[q,s]],fill=True , closed=True,color='#000088ff'))
py.axis('equal')
py.show()  
 # thank you for watching till then bye