# Créé par ARTHUR, le 15/04/2025 en Python 3.7
import matplotlib.pyplot as plt
from maths_proba import factorielle,C,exp

def binomial(x,n,p,sign):
    if x>n or p>1 or p<0:
        return "error x>n or p not in [0;1]"
    if sign=="=":
        return (C(n,x))*(p**x)*(1-p)**(n-x)
    if sign=="<="or sign=="<":
        a=0
        for i in range(x+1):
            a+=(C(n,i))*(p**i)*(1-p)**(n-i)
        return a
    if sign==">="or sign==">":
        b=0
        for i in range(x):
            b+=(C(n,i))*(p**i)*(1-p)**(n-i)
        return 1-b
    else:
        return "sign not in parameter try <,>,<=,>="

assert(binomial(6,10,0.5,"=")==105/512)

def poisson(x,n,p,sign):
    Lambda=n*p
    if x>n or p>1 or p<0:
        return "error x>n or p not in [0;1]"
    if sign=="=":
        return exp(-Lambda)*((Lambda**x)/factorielle(x))
    if sign=="<="or sign=="<":
        a=0
        for i in range(x+1):
            a+=exp(-Lambda)*((Lambda**i)/factorielle(i))
        return a
    if sign==">="or sign==">":
        b=0
        for i in range(x):
            b+=exp(-Lambda)*((Lambda**i)/factorielle(i))
        return 1-b
    else:
        return "sign not in parameter try <,>,<=,>="
assert(poisson(2,1000,0.002,"=")==2*exp(-2))


def comparaison(f1,f2,x,n,p,sign):
    L1=[]
    L2=[]
    for i in range(x+1):
        L1.append(f1(i,n,p,sign))
    for j in range(x+1):
        L2.append(f2(j,n,p,sign))
    plt.plot([i for i in range(x+1)],L1,[i for i in range(x+1)],L2)
    #plt.axis((0,x+1,0,1,))
    plt.grid()
    plt.show()
#comparaison(binomial,poisson,9,10,0.5,"=") #n et p trop grand donc approximation non valable
#comparaison(binomial, poisson, 15, 100, 0.05, "=")
comparaison(binomial, poisson, 159, 1000, 0.02, "=")

