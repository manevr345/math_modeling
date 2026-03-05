import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
m = 0.8 
k = 500
T = 2 * np.pi * np.sqrt(m/k)
t = np.linspace(0, 2*T, frames)
def move_func(z, t):
    
    y, vy, x, vx = z 
    dy_dt = vy

    dvy_dt = g - k*vy*t / m

    dx_dt = x
    dvx_dt = vx
    
    return dy_dt, dvy_dt, x, dvx_dt
g = 9.8
x0 = 0
y0= 0
x0 = 0
vx0 = 0
vy0 = 5
z0 = y0, vy0, x0, vx0
solve = odeint(move_func, z0, t)

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'red')
ball_line, = plt.plot([], [], '-', color='red')

def animate(i):
    ball.set_data([solve[i][0]], [solve[i][1]])
ani = FuncAnimation(fig, animate, frames=frames, interval=100)

edge = 15
ax.set_ylim(-3*edge,  3*edge)
ax.set_xlim(-3*edge, 3*edge)
ani.save('ani2.gif', writer='pillow')