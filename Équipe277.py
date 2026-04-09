from problimite import problimite
import numpy as np
import matplotlib.pyplot as plt

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

A = [np.exp(k*0), np.exp(-k*0)], [np.exp(k*6), np.exp(-k*6)]
b_sol = premier[0:2]
solution = np.linalg.solve(A, b_sol)
def T_exacte(x):
     return T_a+solution[0]*np.exp(k*x)+solution[1]*np.exp(-k*x)
print(premier)
print(deuxieme)
print(solution)
x_1 = np.linspace(0, 6, N_1+2)
x_2 = np.linspace(0, 6, N_2+2)
x_exacte = np.linspace(0, 6, 200)


plt.plot(x_1, premier, label='h=2)')
plt.plot(x_2, deuxieme, label='h=1)')
plt.plot(x_exacte, T_exacte(x_exacte), label='solution exacte')
plt.xlabel('x')
plt.ylabel('T(x)')
plt.title('Solution de l\'équation différentielle avec les valeurs de h=1 et h=2')
plt.legend()
plt.show()