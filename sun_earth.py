import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 500
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)


def move_func(s, t):
    x, v_x, y, v_y = s
    dx_dt = v_x
    dv_xdt = - G * M * x / (x**2 + y**2)**(3/2)
    dy_dt = v_y
    dv_ydt = - G * M * y / (x**2 + y**2)**(3/2)
    return dx_dt, dv_xdt, dy_dt, dv_ydt
G = 6.67 * 10**(-11)
M = 1.998 * 10 ** 30
x0 = 149 * 10**9
v_x = 0
y0 = 0
v_y = 30000
s0 = x0, v_x, y0, v_y
sol = odeint(move_func, s0, t)

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'b')
ball_line, = plt.plot([], [], 's', color = 'b')
plt.plot([0], [0], 'o', color='y', ms =20)
def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])
ani = FuncAnimation(fig, animate, frames = frames, interval = 30)
plt.axis('equal')
edge =2 *x0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('earth_sun.gif', writer='pillow')
