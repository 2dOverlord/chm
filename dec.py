import numpy as np

# [L][U] = LUdecomp([A])
def LUdecomp(a):
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam
    return a


print(LUdecomp([[6, 18, 3],
          [2, 12, 1],
          [4, 15, 3]]))
