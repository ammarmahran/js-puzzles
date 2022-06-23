from math import factorial
from sympy.functions.combinatorial.numbers import stirling

def p(n):
    m = 3*n-1
    return factorial(n) * stirling(m,n) / (n ** m)

def p_rec(m,n,N):
    if m < n:
        return 0
    elif m == 1 and n == 1:
        return 1
    elif n == 0:
        return 0

    return p_rec(m-1,n,N) * n/N + p_rec(m-1,n-1,N) * (N-n+1)/N

if __name__ == '__main__':
    i = 1
    while True:
        r = 1-p(i)
        s = 1-p_rec(3*i-1,i,i)
        if min(r,s) > 1/3:
            print('N p')
            print(i, float(s))
            print(i, float(r))
            break
        i += 1
