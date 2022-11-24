import numpy
import math

#Butterworth using Cauer's topology
def BWKthElement(n,k):
    gk = 2 * math.sin(( (2*k - 1)/2*n ) * k)
    return gk

def Beta():
    res = numpy.log(math.atanh(sigma / 17.37))
    return res

def Omega(n):
    res = math.sinh(Beta() / 2 * n)
    return res

def A(k): #A depends only on the parameter K
    res = math.sin((2 * k - 1) * math.pi)
    return res

def B(k,n):
    beta = Beta()
    omega = Omega(n)
    res = Omega(n)**2 + math.sin((k*math.pi)/n)**2
    return res

def Gfunc(k,n):
    global g
    beta = Beta()
    omega = Omega(n)
    gprev = 2 * A(k) / omega
    if k == 1:
        g = 2 * A(k) /omega
    else:
        for i in range(2,k):
            g = 4 * ( A(k-1) * A(k) )/ (B(k,n) * gprev)
            gprev = g
    return g


#The inductor or capacitor values of a nth-order Chebyshev prototype filter may be calculated from the following equations:
def ChevyNthElement(n):
    #sigma is the passband ripple in decibels
    beta = Beta()
    omega = Omega(n)
    msg = ""
    if (n % 2)==0:
        r=1
        msg = "N est paire, r = "+str(r)+" ."
    else:
        r=math.atanh(beta/4)
        Beta()
        msg = "N est impaire, r= "+str(r)+" avec Beta = "+str(Beta())+" ."
    return msg

#Main program
print("##### --- #####")
print("this program will calculate the Nth element value using the Cauer topology")
n=-999
# Getting n
while n < 0:
    n = int(input("What's the order of the Low Pass Filter?"))
# Getting K : order of the device
k=-999
while k>n or k<0:
    k = int(input("What's the order of the device you wish to get?"))
print(" --- Butterworth Method --- ")
print("The capacity of the Kth element :  Ck = ", BWKthElement(n, k), " F")
print("The Inductance of the Kth element : Lk = ", BWKthElement(n, k), " Henry")

print(" --- Chevychev Method --- ")
sigma=-999
while sigma<0:
    sigma = int(input("Sigma is the passband ripple in decibels: Sigma = ? | usually 3dB "))

print(ChevyNthElement(n))
