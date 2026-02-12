import numpy as np
from scipy.integrate  import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 0.1)

def plotter_of_koks(N, t):
    dNdt = k * N
    return dNdt
N_0 = 1
k  = 1/120
difa = 1
N_t = odeint(plotter_of_koks, N_0, t)
lista = list(zip(N_t, t))
for i in lista:
    
    
plt.plot(t, N_t[:, 0])
plt.savefig('koks.png')