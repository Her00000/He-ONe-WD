#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:16:58 2022

@author: her
"""

import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np

'''grab the last profile'''
h = mr.MesaData('../LOGS/history.data')
log_Teff = h.log_Teff
log_L = h.log_L
log_Teff1 = []
log_Teff2 = []
log_L1 = list()
log_L2 = list()
for i in range(0,len(log_Teff)):
    if log_Teff[i] < 5.81:
        log_Teff1.append(log_Teff[i])
        log_L1.append(log_L[i])
    else:
        log_Teff2.append(log_Teff[i])
        log_L2.append(log_L[i])
        
#plt.figure(12)
#plt.subplot(222)
plt.plot(log_Teff,log_L,'r')
plt.gca().invert_xaxis()
plt.xlabel('log Effective Temperature')
plt.ylabel('log Luminosity')
plt.title('HR diagram')
plt.plot(log_Teff[1321],log_L[1321],'o')
'''
plt.subplot(224)
plt.plot(log_Teff2,log_L2,'g')
plt.gca().invert_xaxis()
plt.xlabel('log Effective Temperature')
plt.ylabel('log Luminosity')
#plt.title('HR diagram')
plt.subplot(121)
plt.plot(log_Teff,log_L)
plt.gca().invert_xaxis()
plt.plot(log_Teff[9],log_L[9],'o',c='k')
plt.plot(log_Teff[7876],log_L[7876],'o',c='k')

plt.xlabel('log Effective Temperature')
plt.ylabel('log Luminosity')
plt.title('HR diagram')
plt.show()
'''


