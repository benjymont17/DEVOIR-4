from problimite import problimite
import numpy as np
import matplotlib.pyplot as plt

L=6
k = 1.2
T_a = 20
T = 350

N_1 = int((6/2)-1)
N_2 = int((6/1)-1)
Q_1 = [k**2]*N_1
Q_2 = [k**2]*N_2
R_1 = [-k**2*T_a]*N_1
R_2 = [-k**2*T_a]*N_2
premier = problimite(N_1, Q_1, R_1, 0, 6, T, T_a)
deuxieme = problimite(N_2, Q_2, R_2, 0, 6, T, T_a)

A = [1, 1], [np.exp(k*L), np.exp(-k*L)]
b_sol = [T-T_a, 0]
solution = np.linalg.solve(A, b_sol)


def T_exacte(x):
     return T_a+solution[0]*np.exp(k*x)+solution[1]*np.exp(-k*x)
print(premier)
print(deuxieme)
print(solution)
x_1 = np.linspace(0, 6, N_1+2)
x_2 = np.linspace(0, 6, N_2+2)
x_exacte = np.linspace(0, 6, 200)


plt.plot(x_1, premier, label='h=2')
plt.plot(x_2, deuxieme, label='h=1')
plt.plot(x_exacte, T_exacte(x_exacte), label='solution exacte')
plt.xlabel('x')
plt.ylabel('T(x)')
plt.title('Solution de l\'équation différentielle avec \n les valeurs de h=1, h=2 et la solution exacte')
plt.legend()
plt.show()


h_1 = L/3
h_2 = L/6
h_3 = L/100
h_4 = L/1000
h_5 = L/10000
N_1 = int((6/h_1)-1)
N_2 = int((6/h_2)-1)
N_3 = int((6/h_3)-1)
N_4 = int((6/h_4)-1)
N_5 = int((6/h_5)-1)
Q_1 = [k**2]*N_1
Q_2 = [k**2]*N_2
Q_3 = [k**2]*N_3
Q_4 = [k**2]*N_4
Q_5 = [k**2]*N_5
R_1 = [-k**2*T_a]*N_1
R_2 = [-k**2*T_a]*N_2
R_3 = [-k**2*T_a]*N_3
R_4 = [-k**2*T_a]*N_4
R_5 = [-k**2*T_a]*N_5

limite_1 = problimite(N_1, Q_1, R_1, 0, 6, T, T_a)
limite_2 = problimite(N_2, Q_2, R_2, 0, 6, T, T_a)
limite_3 = problimite(N_3, Q_3, R_3, 0, 6, T, T_a)
limite_4 = problimite(N_4, Q_4, R_4, 0, 6, T, T_a)
limite_5 = problimite(N_5, Q_5, R_5, 0, 6, T, T_a)

x_1 = np.linspace(0, 6, N_1+2)
x_2 = np.linspace(0, 6, N_2+2)
x_3 = np.linspace(0, 6, N_3+2)
x_4 = np.linspace(0, 6, N_4+2)
x_5 = np.linspace(0, 6, N_5+2)

erreur_max_1 = max(abs(limite_1 - T_exacte(x_1)))
erreur_max_2 = max(abs(limite_2 - T_exacte(x_2)))
erreur_max_3 = max(abs(limite_3 - T_exacte(x_3)))
erreur_max_4 = max(abs(limite_4 - T_exacte(x_4)))
erreur_max_5 = max(abs(limite_5 - T_exacte(x_5)))

h_valeurs = [h_1, h_2, h_3, h_4, h_5]
erreurs_max = [erreur_max_1, erreur_max_2, erreur_max_3, erreur_max_4, erreur_max_5]

plt.loglog(h_valeurs, erreurs_max, marker='o', label = 'E(h)')

plt.xlabel('h')
plt.ylabel('Erreur maximale')
plt.title('Erreur maximale de l\'approximation en fonction de h')
plt.legend()
plt.grid()
plt.show()