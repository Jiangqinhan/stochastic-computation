import matplotlib.pyplot as plt
import random
import numpy as np
import math

def W(T):
	W=np.zeros(len(T))
	w=np.zeros(len(T)-1)
	diff_T=np.diff(T)
	for i in range(len(T)-1):
		w[i]=np.random.normal(0,math.sqrt(diff_T[i]))
	W[1:]=np.cumsum(w)
	return W
		
def Euler(T,W,a,b,X_0):
	Y=np.zeros(len(T))
	Y[0]=X_0
	diff_T=np.diff(T)
	diff_W=np.diff(W)
	for i in range(len(diff_T)):
		Y[i+1]=Y[i]+a*Y[i]*diff_T[i]+b*diff_W[i]*Y[i]
	return Y
#######################################################################################
def func(T,W,a,b,X_0):
	return X_0*np.exp((a-b*b/2)*T+b*W)

def func2(T):
	return np.exp(T+0.5*W(T))

a=1.5
b=1
X_0=1.0
T=np.linspace(0,1,1000)
W1=W(T)
Y1=func(T,W1,a,b,X_0)
Y2=Euler(T,W1,a,b,X_0)
#plt.plot(T,Y1,label="yuan")
#plt.plot(T,Y2)
#plt.legend()
A=np.zeros(len(T))
for i in range(4000):
	A=A+func2(T)
A=A/4000
plt.plot(T,A)
plt.plot(T,np.exp(9*T/8))
#plt.plot(T,W1)
plt.show()
print('done')
