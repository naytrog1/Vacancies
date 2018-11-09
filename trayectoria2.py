#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
d, vis = .1,0.00149
ro = 1.22/4000. #fluido/esfera

''' Reinolds Esfera '''

def Cd(v):
    Re=float(v*d/vis)
    if Re<=0.0:
        return 0.0 
    elif Re>0.0 and Re<=1.:
        return 24.0/Re
    elif Re>1.0 and Re<=400.0:
        return 24.0/(Re**0.646)
    elif Re>400 and Re<=3e5:
        return 0.5
    elif Re>3e5 and Re<=2e6:
        return 3.66e-4*Re**0.4275
    elif Re>2e6:
        return 0.18

''' Fuerzas en X e Y '''

def f(r,t):
	ro = 1.22/4000. #fluido/esfera
	A = 1+(ro/2)
	B = (1-ro)*9.8
	C = (3*ro)/(4*d)
	x = r[0]
	y = r[1]
	z = r[2]
	w = r[3]
	vfx,vfy=Vv[0],Vv[1]
	vx = z-vfx
	vy = w-vfy
	v=np.sqrt((vx)**2+(vy)**2)
	fx = z
	fy = w
	fz =  -(C*vx*v*Cd(vx))/A
	fw =  -(B+(C*vy*v*Cd(vy)))/A
	return np.array([fx,fy,fz,fw],float)

Vv=[10.0,10.0]
ve = 50.#velocidad lansamiento
h=.001
tpoints = np.arange(0,20,h)
xpoints = []
ypoints = []
zpoints = []
wpoints = []
rad = np.arange(1,12.)*np.pi/24
degrees = np.degrees(rad)
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
number_of_plots=len(rad)
colors=plt.cm.rainbow(np.linspace(0,1,number_of_plots))
for i,c in zip(range(len(rad)),colors):
	ange = rad[i]
	angulo = degrees[i]
	r = np.array([0.,0.,(ve*np.cos(ange)),(ve*np.sin(ange))],float)
	for t in tpoints:
		xpoints.append(r[0])
		ypoints.append(r[1])
		zpoints.append(r[2])
		wpoints.append(r[3])
		k1 = h*f(r,t)
		k2 = h*f(r+0.5*k1,t+0.5*h)
		k3 = h*f(r+0.5*k2,t+0.5*h)
		k4 = h*f(r+k3,t+h)
		r +=(k1+2*k2+2*k3+k4)/6
		if(r[1]<0):
			break
	plt.plot(xpoints,ypoints,color=c)
	#legend(f'{angulo:.1f}')
	#print(colors[i])
	#,color=colors[i])
#plt.legend(loc='best')
#plt.savefig('bla.png')
plt.xlabel("Distancia x")
plt.ylabel("Distancia y")
plt.ylim(0,)
plt.show()
