# -*- coding:utf-8 -*-
import time
import numpy as np
import matplotlib.pyplot as plt
def Brown_motion(T,m):
	diff_T=np.diff(T)
	diff_W=np.random.randn(m,len(diff_T))
	diff_W=diff_W*np.sqrt(diff_T)
	#布朗运动有m个分量，T是时间剖分
	W=np.zeros((m,len(T)))
	W[:,1:]=np.cumsum(diff_W,1)
	return W

def Euler(T,W,a,b,X_0):
	Y=np.zeros((len(X_0),len(T)))
	Y[0]=X_0
	diff_T=np.diff(T)
	diff_W=np.diff(W)
	for i in range(len(diff_T)):
		Y[:,i+1]=Y[:,i]+a(T[i],Y[:,i])*diff_T[i]+np.dot(b(T[i],Y[:,i]),diff_W[:,i])
	return Y

def Milstein(T,W,a,b,db,X_0):
	Y=np.zeros((len(X_0),len(T)))
	Y[0]=X_0
	diff_T=np.diff(T)
	diff_W=np.diff(W)
	for i in range(len(diff_T)):
		Y[:,i+1]=Y[:,i]+a(T[i],Y[:,i])*diff_T[i]+np.dot(b(T[i],Y[:,i]),diff_W[:,i])+0.5*np.dot(np.dot(b(T[i],Y[:,i]),db(T[i],Y[:,i])),diff_W[:,i]**2-diff_T[i])
	return Y
def order_(T,W,a,b,da,db,dda,ddb,at,bt,X_0):
	Y=np.zeros((len(X_0),len(T)))
	Y[0]=X_0
	diff_T=np.diff(T)
	diff_W=np.diff(W)
	diff_Z=(1/np.sqrt(3)*np.random.randn(np.shape(diff_W)[0],np.shape(diff_W)[1])+diff_W/np.sqrt(diff_T))*0.5*diff_T**1.5
	for i in range(len(diff_T)):
		Y[:,i+1]=Y[:,i]+a(T[i],Y[:,i])*diff_T[i]+np.dot(b(T[i],Y[:,i]),diff_W[:,i])+0.5*np.dot(np.dot(b(T[i],Y[:,i]),db(T[i],Y[:,i])),diff_W[:,i]**2-diff_T[i])
		Y[:,i+1]=Y[:,i+1]+diff_T[i]**2/2*(at(T[i],Y[:,i])+a(T[i],Y[:,i])*da(T[i],Y[:,i])+0.5*b(T[i],Y[:,i])**2*dda(T[i],Y[:,i]))+b(T[i],Y[:,i])*da(T[i],Y[:,i])*diff_Z[:,i]
		Y[:,i+1]=Y[:,i+1]+(bt(T[i],Y[:,i])+a(T[i],Y[:,i])*db(T[i],Y[:,i])+0.5*b(T[i],Y[:,i])**2*ddb(T[i],Y[:,i]))*(diff_T[i]*diff_W[:,i]-diff_Z[:,i])
		Y[:,i+1]=Y[:,i+1]+0.5*(b(T[i],Y[:,i])*db(T[i],Y[:,i])**2+b(T[i],Y[:,i])**2*ddb(T[i],Y[:,i]))*(1/3*diff_W[:,i]**3-diff_W[:,i]*diff_T[i])
	return Y
		

