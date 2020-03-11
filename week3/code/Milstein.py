import head
import time
import numpy as np
import matplotlib.pyplot as plt
N=5
m=1
lam=np.array([2])
mu=np.array([1])
X_0=np.array([1])
T=np.linspace(0,1,pow(10,N)+1)
n=1
W=head.Brown_motion(T,m)
X_true=X_0*np.exp((lam-0.5*np.inner(mu,mu))*T+np.dot(mu,W))
plt.plot(T,X_true.transpose())
T1=np.linspace(0,1,pow(10,n)+1)
W1=W[:,::pow(10,N-n)]
X=head.Milstein(T1,W1,lambda t,y:y*lam,lambda t,y:mu*y,lambda t,y:mu,X_0)
plt.scatter(T1,X,color="red")
plt.show()
##########################################################
'''
s1=time.time()
for n in range(N):
	error=0
	for j in range(1000):
		W=head.Brown_motion(T,m)
		X_true=X_0*np.exp((lam-0.5*mu*mu)*T+mu*W)
		T1=np.linspace(0,1,pow(10,n)+1)
		W1=W[:,::pow(10,N-n)]
		X=X=head.Milstein(T1,W1,lambda t,y:y*lam,lambda t,y:mu*y,lambda t,y:mu,X_0)
		error+=abs(X_true[:,-1]-X[:,-1])
	print(error/1000)
s2=time.time()		
print(s2-s1)		
'''
