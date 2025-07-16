import numpy as np
import matplotlib.pyplot as plt

def fPUMA(theta1, theta2, theta3, theta4, theta5, theta6):
    #Parâmetros DH
    J = [theta1, theta2, theta3, theta4, theta5, theta6]
    A = [-90, 0, 90, -90, 90, 0] #Ângulo de torção(alfa), em graus
    #a = [0, 0.432, -0.020, 0, 0, 0] #Deslocamento(offset) no eixo, em metros
    #d = [0.672, 0.140, 0, 0.432, 0, 0.056] #offset no eixo z, em metros
    a = [0, 431.80, -20.32, 0, 0, 0]  # offset no eixo x (a), em milímetros
    d = [671.83, 139.70, 0, 431.80, 0, 56.50]  # offset no eixo z (d), em milímetros

    #Verificando limites articulades
    if(
        -160 <= J[0] <= 160 and
        -225 <= J[1] <= 45 and
        -45 <= J[2] <= 225 and
        -110 <= J[3] <= 170 and
        -100 <= J[4] <= 100 and
        -266 <= J[5] <= 266   
    ):
        T = []
        #Matriz homogênea de cada elo
        for n in range(6):
            theta = np.radians(J[n])
            alpha = np.radians(A[n])
            a_n = a[n]
            d_n = d[n]

            matT = np.array([
                [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a_n*np.cos(theta)],
                [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a_n*np.sin(theta)],
                [0, np.sin(alpha), np.cos(alpha), d_n],
                [0, 0, 0, 1]
            ])
            T.append(matT)

        P = []
        for i in range(6):
            if i == 0:
                P.append(T[0])
            else:
                P.append(P[i-1] @ T[i])

        #Posições dos elos para plot
        x = [0]
        y = [0]
        z = [0]
        for i in range(6):
            x.append(P[i][0, 3])
            y.append(P[i][1, 3])
            z.append(P[i][2, 3])
        
        #Plot 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k']

        for i in range(6):
            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [z[i], z[i+1]], color=colors[i], linewidth=5)
        
        ax.plot(x, y, z, 'ko') #Juntas
        ax.set_xlabel('Eixo X')
        ax.set_ylabel('Eixo Y')
        ax.set_zlabel('Eixo Z')
        ax.set_title('Cinemática Direta do Manipulador PUMA 560 (6Dof)')
        ax.view_init(elev = 0, azim = 0)
        plt.grid(True)
        plt.show()

        #Posição final do efetuador
        print("A posição do efetor final é:")
        valuex, valuey, valuez = P[5][0, 3], P[5][1, 3], P[5][2, 3]
        print(f"Px = {valuex:.2f}, Py = {valuey:.2f}, Pz = {valuez:.2f}")
        print("\nO modelo DH final (matriz homogênea) é:")
        #np.set_printoptions(precision=3, suppress=True)
        print(P[5])
    else:
        print("Ângulo conjunto fora do alcance!")

# Definindo os thetas
#posição Inicial
fPUMA(0, 0, 0, 0, 0, 0)

#theta2 = 45°(ombro)
#fPUMA(0, 45, 0, 0, 0, 0)

#theta3 = 45°(cotovelo)
#fPUMA(0, 0, 45, 0, 0, 0)

#theta1 = 90°(cintura)
#fPUMA(90, 0, 0, 0, 0, 0)

