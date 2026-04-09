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
    h = (b-a)/(N+1)
    D= -2-h**2*Q
    I = np.ones(N-1)
    S= np.ones(N-1)

    b_vect= h**2*R
    b_vect[0] = b_vect[0] - alpha
    b_vect[N-1] = b_vect[N-1] - beta

    y_prob = tridiagonal(N, D, I, S, b_vect)
    
    y= np.zeros(N+2)
    y[0] = alpha
    y[N-1] = beta
    y[1:N+1] = y_prob

    return y