# -*- coding:utf-8 -*-
import time
import numpy as np
import matplotlib.pyplot as plt
def Brown_motion(T,m):
	diff_T=np.diff(T)
	diff_W=np.random.randn(m,len(diff_T))
	diff_W=diff_W*np.sqrt(diff_T)
	W=np.zeros((m,len(T)))
	W[:,1:]=np.cumsum(diff_W,1)
	return W

def Euler(T,W,a,b,X_0):
	Y=np.zeros(np.shape(W))
	Y[0]=X_0
	diff_T=np.diff(T)
	diff_W=np.diff(W)
	for i in range(len(diff_T)):
		Y[:,i+1]=Y[:,i]+a*Y[:,i]*diff_T[i]+b*diff_W[:,i]*Y[:,i]
	return Y
######################
N=5
m=1
lam=2
mu=1
X_0=1
T=np.linspace(0,1,pow(10,N)+1)
5
n=1
W=Brown_motion(T,m)
X_true=X_0*np.exp((lam-0.5*mu*mu)*T+mu*W)
plt.plot(T,X_true.transpose())
T1=np.linspace(0,1,pow(10,n)+1)
W1=W[:,::pow(10,N-n)]
X=Euler(T1,W1,lam,mu,X_0)
plt.scatter(T1,X,color="red")
plt.show()

###############################
'''
s1=time.time()
for n in range(N):
	error=0
	for j in range(1000):
		W=Brown_motion(T,m)
		X_true=X_0*np.exp((lam-0.5*mu*mu)*T+mu*W)
		T1=np.linspace(0,1,pow(10,n)+1)
		W1=W[:,::pow(10,N-n)]
		X=Euler(T1,W1,lam,mu,X_0)
		error+=abs(X_true[:,-1]-X[:,-1])
	print(error/1000)
s2=time.time()		
print(s2-s1)		
'''	

