import numpy as np
from tridiagonal import tridiagonal

def problimite(N, Q, R, a, b, alpha, beta):
     """
    N: nombre d'arguments
    Q: vecteur contenant les évaluations de la fonction q(x)
    R: vecteur contenant les évaluations de la fonction r(x)
    a: scalaire
    b: scalaire
    alpha: scalaire
    beta: scalaire
    """
     b_vect = np.zeros(N)
     h = (b-a)/(N+1)
     D = np.zeros(N)
     for i in range(0, N):
          D[i] = -2 - h**2 * Q[i]
          b_vect[i] = h**2 * R[i]
          if i==0:
               b_vect[0] = h**2 * R[0] - alpha
          elif i==N-1:
               b_vect[N-1] = h**2 * R[N-1] - beta
     I = np.ones(N-1)
     S = np.ones(N-1)


     y_prob = tridiagonal(N, D, I, S, b_vect)
     y= np.zeros(N+2)
     y[0] = alpha
     y[N+1] = beta
     y[1:N+1] = y_prob

     return y