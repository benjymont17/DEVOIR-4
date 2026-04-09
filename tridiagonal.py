def tridiagonal(N, D, I, S, b):
    """
    N: nombre d'arguments
    D: vecteur contenant la diagonale principale
    I: vecteur contenant la diagonale inférieure
    S: vecteur contenant la diagonale supérieure
    b: vecteur contenant le terme constant
    """
    y[0] = b[0] / D[0]
    for i in range (1, N):
        D[i] = D[i] - I[i-1] * S[i-1]
        S[i-1] = S[i-1] / D[i-1]
        y[i] = (b[i] - I[i-1] * y[i-1]) / D[i]
    x[N-1] = y[N-1]
    for i in range (N-2, 1):
        x[i] = y[i] - S[i] * x[i+1]
    return x
