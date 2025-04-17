# Créé par boini, le 17/04/2025 en Python 3.7
"""
def factorielle(x):
    if not(isinstance(x,int)) or x<0:
        return "error, x supposed to be non negative int"
    if x==1 or x==0:
        return 1
    else:
        return x*factorielle(x-1)
"""

def factorielle(x):
    res=1
    for i in range(1,x+1):
        res*=i
    return res
def C(n,k):
    return factorielle(n)/(factorielle(k)*factorielle(n-k))
def exp(x):
    e=2.7182818285
    return e**x