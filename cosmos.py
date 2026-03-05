import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 500
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

planets  =[]
trajectories = []
r = 58*10**9, 108*10**9, 150*10**9, 228*10**9, 778*10**9, 1428*10**9, 4498*10**9
u = 48*1000, 32*1000, 30*1000, 24*1000, 13*1000, 9,6**1000, 6,5**1000, 5,4*1000, 4,8**1000
v_x = 0
y0 = 0

s0 = r, v_x, v_x, v_x, v_x, v_x, v_x, v_x, v_x, v_x, y0, y0,y0,y0,y0,y0,y0,y0,u 
M = 3,3*10**23
G = 6.67 * 10**(-11)
for i in range(9):
    planets.append(plt.plot([], [], 'o', color = 'b'))
    trajectories.append(plt.plot([], [], '-', color = 'b'))
plt.plot([0], [0], 'o', color='y', ms =20)
def move_func(s, t):
    x1, x2, x3, x4, x5, x6, x7, x8, vx1, vx2, vx3, vx4, vx5, vx6, vx7, vx8, vx9, y1, y2,y3,y4,y5,y6,y7,y8, vy1, vy2, vy3, vy4, vy5, vy6, vy7, vy8, = s

    dx_dt1 = vx1
    dv_xdt1 = - G * M * x1 / (x1**2 + y1**2)**(3/2)
    dy_dt1 = vy1
    dv_ydt1 = - G * M * y1 / (x1**2 + y1**2)**(3/2)

    dx_dt2 = vx2
    dv_xdt2 = - G * M * x2 / (x2**2 + y2**2)**(3/2)
    dy_dt2 = vy2
    dv_ydt2 = - G * M * y2 / (x2**2 + y2**2)**(3/2)

    dx_dt3 = vx3
    dv_xdt3 = - G * M * x3 / (x3**2 + y3**2)**(3/2)
    dy_dt3 = vy3
    dv_ydt3 = - G * M * y3 / (x3**2 + y3**2)**(3/2)

    dx_dt4 = vx4
    dv_xdt4 = - G * M * x4 / (x4**2 + y4**2)**(3/2)
    dy_dt4 = vy4
    dv_ydt4 = - G * M * y4 / (x4**2 + y4**2)**(3/2)

    dx_dt5 = vx5
    dv_xdt5 = - G * M * x5 / (x5**2 + y5**2)**(3/2)
    dy_dt5 = vy5
    dv_ydt5 = - G * M * y5 / (x5**2 + y5**2)**(3/2)

    dx_dt6 = vx6
    dv_xdt6 = - G * M * x6 / (x6**2 + y6**2)**(3/2)
    dy_dt6 = vy6
    dv_ydt6 = - G * M * y6 / (x6**2 + y6**2)**(3/2)

    dx_dt7 = vx7
    dv_xdt7 = - G * M * x7 / (x7**2 + y7**2)**(3/2)
    dy_dt7 = vy7
    dv_ydt7 = - G * M * y7 / (x7**2 + y7**2)**(3/2)

    dx_dt8 = vx8
    dv_xdt8 = - G * M * x8 / (x8**2 + y8**2)**(3/2)
    dy_dt8 = vy8
    dv_ydt8 = - G * M * y8 / (x8**2 + y8**2)**(3/2)
    return 
def animate(i):
    for j in range(9):
        planets[j][0].set_data([sol[i][j+4]], [sol[i][j*2+2]])
        trajectories[j][0].set_data(sol[:i,j+4], sol[:i, j*2 +2])




sol = odeint(move_func, s0, t)

fig, ax = plt.subplots()

ani = FuncAnimation(fig, animate, frames = frames, interval = 30)
plt.axis('equal')
edge =2 *x0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('earth_sun.gif', writer='pillow')