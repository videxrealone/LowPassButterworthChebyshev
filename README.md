# LowPassButterworthChevy
``import numpy
import math


#Butterworth using Cauer's topology
def BWKthElement(n,k):
    gk = 2 * math.sin(( (2*k - 1)/2*n ) * k)
    return gk

def Gfunc(i):
    if i == 0:
        g = 0
#to complete
    return




#The inductor or capacitor values of a nth-order Chebyshev prototype filter may be calculated from the following equations:
def ChevyNthElement(n,k,sigma):
    #init
    #sigma is the passband ripple in decibels
    beta = numpy.log(math.atanh(sigma/17.37))
    omega = math.sinh(beta / 2 * n)
    if (n % 2)==0:
        r=1
    else:
        r=math.atanh(beta/4)

    Ak = math.sin((2 * k - 1) * math.pi)
    Bk = omega**2 + math.sin((k*math.pi)/n)**2
    #main

    #G0=1
    #G1= (2 * Ak)/omega
    #Gk=()


#main
print("##### --- #####")
print("this program will calculate the Nth element value using the Cauer topology")
n=-999
while n < 0:
    n = int(input("What's the order of the Low Pass Filter?"))
k=-999
while k>n or k<0:
    k = int(input("What's the order of the device you wish to get?"))

print("Ck = ", BWKthElement(n, k), " F")
print("Lk = ", BWKthElement(n, k), " Henry")
sigma=-999
while sigma<0:
    sigma = int(input("Sigma = ? | Sigma is the passband ripple in decibels"))

print(ChevyNthElement(n,k,sigma))
``
