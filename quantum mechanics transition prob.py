# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:41:22 2023

@author: Enric Garriga
"""

import matplotlib.pyplot as plt
import numpy as np
import cmath as cm

# Constants:
h_bar=1
m=1
e=1
Bx=0.8
B0=1
#d=1
#om=1    #omega
Dom=e*B0/m   #Delta omega
#imag=complex(0,1)
test=np.e**(np.pi*1j)

#Initial conditions:
c1_0=1; c2_0=0

#P_trans=4*d**2/(h_bar**2*(Dom+om)**2)*(np.sin((Dom+om)*t/2))**2

# We define a function to calculate a complex number's modulus squared
def modul2(z):
    return( z.real**2 + z.imag**2 )

t=np.linspace(0, 2*np.pi, num=500000, retstep=True) #t is an array of arrays: t=[ [list of t's], length of t ]
dt=t[len(t)-1]

c1=np.empty(len(t[0]), dtype=np.complex_); c1[0]=c1_0
c2=np.empty(len(t[0]), dtype=np.complex_); c2[0]=c2_0

def velocity_vector(t, c1, c2):
    dc1=1/(1j)*e*Bx*c2/(2*m)*cm.rect(1, Dom*t)
    dc2=1/(1j)*e*Bx*c1/(2*m)*cm.rect(1, -Dom*t)
    return( [dc1,dc2] )

dc1=0
dc2=0

[dc1, dc2] = velocity_vector(0, c1_0, c2_0) #This line is redundant because of how we define the loop below.

steps=50
#%%
for i in range(0, len(t[0])-1):
    # First we calculate the velocity vector (dc1, dc2) which depends on the position vector
    # (c1, c2). We need the current velocity (dc1, dc2) to compute the next position:
    [dc1, dc2] = velocity_vector(t[0][i], c1[i], c2[i])
    
    #And thus we can now update the position vectors:
    c1[i+1]=c1[i]+dt*dc1
    c2[i+1]=c2[i]+dt*dc2
#%%
P_trans=modul2(c2)

exact=Bx**2/(Bx**2 + B0**2) *( np.sin( e*np.sqrt(B0**2 + Bx**2) * t[0] / (2*m) ) )**2
fig, ax = plt.subplots()

ax.plot(t[0], P_trans, label='P_trans')
ax.plot(t[0], modul2(c1), color='orange', label='P_1')
ax.plot(t[0], P_trans + modul2(c1), color='green', label='total')
ax.plot(t[0], exact, color='red', label='EXACT', linestyle='-.')
ax.legend()
#ax.set_xlim([0,t[len(t)-1]])
#ax.set_ylim([-0.15,1.5])

plt.show()