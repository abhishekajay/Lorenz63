from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib  import animation

def lorenzfunc(x,t):
    d=np.zeros(3)
    sigma=10
    rho=28
    beta=8/3
    d[0]=sigma*(x[1]-x[0])
    d[1]=x[0]*(rho-x[2])-x[1]
    d[2]=x[0]*x[1]-beta*x[2]
    return d
  
step=0.01
#t=np.arange(0,30,0.01)
x0=np.ones(3)
#x1=odeint(lorenzfunc,x0,t)
#print(len(x1))
fig=plt.figure()
ax=Axes3D(fig)
timeval=np.arange(0,30,0.01)
x=odeint(lorenzfunc,x0,timeval)
def gen(n):
    index=0
    while index < 3000:
        #print(x[index,0],x[index,1],x[index,2])
        yield np.array([x[index,0], x[index,1], x[index,2]])
        index=index+1
        

def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])
    
    
N = 100
data = np.array(list(gen(N))).T
line, = ax.plot(data[0,0:1] ,data[1,0:1], data[2,0:1])
# Setting the axes properties
ax.set_xlim3d([-15.0, 20.0])
ax.set_xlabel('X')

ax.set_ylim3d([-15.0, 50.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-15, 30.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, update, 5000*N, fargs=(data, line), interval=5000/N, blit=False)   
ani.save('lorenzanimation.mp4', writer='ffmpeg')
#ax.plot(x[:,0],x[:,1],x[:,2])
plt.show()


