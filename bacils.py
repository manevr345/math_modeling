import numpy as np
from scipy.integrate  import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
t = np.arange(0, 10**6, 100)
fig, ax = plt.subplots()
def radio_funktion(m, t):# Изменяемая величина, переменная величина
     dmdt = -k * m
     return dmdt
# Опредение начальных услолвий 
m_0 = 10
k = 1.61*10**(-6)
anim_object = plt.plot([], [])
def update(i) 
m_t = odeint(radio_funktion, m_0, t)

ani = FuncAnimation(fig, anim_object, t, update)