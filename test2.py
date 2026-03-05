import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 50

t = np.linspace(0, 10, frames)


def move_func(s, t):
    x, v_x, y, v_y = s
    dx_dt = v_x
    dv_xdt =  k * Q *q * x / (x**2 + y**2)**(3/2)
    dy_dt = v_y
    dv_ydt =  k * Q * q * y / (x**2 + y**2)**(3/2)
    return dx_dt, dv_xdt, dy_dt, dv_ydt

M = 40*10**(-3)
k = 9*10**9
Q = 3 * 10**(-6)
q = -6.67 * 10**(-8)
x0 = -1
v_x0 = 0.1
y0 = 0.5
v_y0 = 0
s0 = x0, v_x0, y0, v_y0
sol = odeint(move_func, s0, t)

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'b')
ball_line, = plt.plot([], [], '-', color = 'b')
plt.plot([0], [0], 'o', color='y', ms =20)
def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])
ani = FuncAnimation(fig, animate, frames = frames, interval = 30)
plt.axis('equal')
edge = 3
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('earth_sun.gif', writer='pillow')