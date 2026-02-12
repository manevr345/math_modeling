import numpy as np
from scipy.integrate  import odeint
import matplotlib.pyplot as plt
# Пределы изменения переменной величины

t = np.arange(0, 10**6, 100)

def radio_funktion(m, t):# Изменяемая величина, переменная величина
     dmdt = -k * m
     return dmdt
# Опредение начальных услолвий 
m_0 = 10
k = 1.61*10**(-6)

m_t = odeint(radio_funktion, m_0, t)

plt.plot(t, m_t[:, 0])
plt.savefig('fig.png')
