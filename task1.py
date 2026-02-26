import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)
def move_func(z, t):
    y, vy = z 
    dy_dt = vy
    dvy_dt = -g - vy
    return dy_dt, dvy_dt
g = 9.8
v = 20
alpha = 80 * np.pi/180

y0= 0
z0 = y0, v
solve = odeint(move_func, z0, t)
solverh = [solve[i][0] for i in range(len(solve))]
solvervy = [solve[i][1] for i in range(len(solve))]


plt.plot(t, solverh, color='r')
print(solve)
plt.savefig('fig1.jpg')
plt.plot(t, solvervy)
plt.savefig('fig2.jpg')