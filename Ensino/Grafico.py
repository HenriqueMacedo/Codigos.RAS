import numpy as np
import matplotlib.pyplot as plt

# Define a função
def y(t):
    return (-t + np.log(t + 1) + t * np.log(t + 1)) * np.exp(-t)

# Intervalo de tempo de 0 a 10 (com 1000 pontos para suavidade)
t = np.linspace(0.001, 10, 1000)  # começa em 0.001 para evitar log(0)

# Calcula y(t)
yt = y(t)

# Plota o gráfico
plt.figure(figsize=(10, 6))
plt.plot(t, yt, label=r'$y(t) = (-t + \ln(t+1) + t\ln(t+1)) e^{-t}$', color='blue')
plt.title('Gráfico da Solução $x(t)$ no intervalo $[0, 10]$')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.show()
