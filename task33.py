import numpy as np
from scipy.integrate  import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 25, 1)
g = 10
y = 0.25
m = 10
u0 = 0
def upadata(u, t):
    dudt = g - y*u**2/m
    return dudt
u_t = odeint(upadata, u0,  t)
plt.plot(t, u_t[:, 0])
plt.savefig('parashut.png')