#1________________________________
from math import sin, exp



class Sum:

    def __init__(self, f_k, M, N):
        self.f_k = f_k
        self.M = M
        self.N = N
        self.first_neglected_term = None

    def __call__(self, x):
        S = 0
        f_k, M, N = self.f_k, self.M, self.N
        for k in range(M, N + 1):
            S += f_k(x, k)
        self.first_neglected_term = f_k(x, N + 1)
        return (S)


def table(term, x, M, Nlist, f):
    print ('=' * 58)
    print ('%-14s %-14s %-14s %-14s' \
        % ('x=%g' % x, "f (approx.)", 'Error', 'Next term'))
    print ('-' * 58)
    for N in Nlist:
        S = Sum(term, M, N)
        print ('N = %-8d | %13.6E  %13.6E  %13E' \
            % (N, S(x), f(x) - S(x), S.first_neglected_term))
    print ('=' * 58 + '\n')


def factorial(n):
    if n == 0:
        return (1)
    else:
        return (n * factorial(n - 1))


def term(x, k):
    return ((-x) ** k)
S = Sum(term, M=0, N=100)
x = 0.5
print (S(x))
print (S.first_neglected_term)


from math import *


def term(x, k):
    return ((-1) ** k * x ** (2 * k + 1) / float(factorial(2 * k + 1)))
print ('\nf(x) = sin(x)')
for x in (pi, 30 * pi):
    table(term, x, M=0, Nlist=(5, 10, 20), f=sin)


def term(x, k):
    return (((-x) ** k) / float(factorial(k)))
print ('\nf(x) = exp(-x)')
for x in (1, 3, 5):
    table(term, x, M=0, Nlist=(5, 10, 20), f=lambda x: exp(-x))


def term(x, k):
    return ((1 / float(k)) * (x / float(1 + x)) ** k)
print ('\nf(x) = ln(1 + x)')
for x in (2, 5, 10):
    table(term, x, M=1, Nlist=(5, 10, 20), f=log)