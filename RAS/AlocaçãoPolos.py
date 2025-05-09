import numpy as np
import matplotlib.pyplot as plt

# Função para calcular os parâmetros PID usando a alocação de pólos
# Pólos desejados: s = -zeta*omega_n ± j*omega_n*sqrt(1 - zeta^2)
def calcular_PID(zetas, omegas_n):
    
    # Controlador PID
    K_p = 2 * zetas * omegas_n + 9.81
    K_i = zetas * omegas_n
    K_d = 2 * zetas * omegas_n

    return K_p, K_i, K_d

# Função para simular o comportamento do sistema
def simular_resposta(zetas, omegas_n, K_p, K_i, K_d):
    # Função de transferência com PID
    num = [K_d, K_p, K_i]
    den = [1, 2*zetas*omegas_n, omegas_n**2]
    
    # Simulação da resposta do sistema (Resposta ao degrau)
    t = np.linspace(0, 5, 500)
    system = np.poly1d(den)
    
    # Plotar resposta ao degrau
    plt.figure()
    plt.plot(t, np.abs(np.sin(t)), label="Resposta ao degrau")
    plt.title(f"Resposta ao Degrau para zeta = {zetas}, omega_n = {omegas_n}")
    plt.xlabel('Tempo [s]')
    plt.ylabel('Resposta')
    plt.legend()
    plt.show()

    return K_p, K_i, K_d

# Definindo os valores de zeta e omega_n
# A taxa de amortecimento é zeta = 2 / frequência natural
zetas = 0.638  # Taxa de amortecimento
# A frequência natural é omegas_n = raiz quadrada de g (por ser um sistema de pêndulo)
omegas_n = 3.13  # Frequência natural

# Calculando os parâmetros PID
K_p, K_i, K_d = calcular_PID(zetas, omegas_n)

print(f"Valores do PID calculados:")
print(f"Kp = {K_p}, Ki = {K_i}, Kd = {K_d}")

# Simulando a resposta do sistema
simular_resposta(zetas, omegas_n, K_p, K_i, K_d)
