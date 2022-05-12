#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:39:01 2022

@author: her
"""

import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np


h = mr.MesaData('../LOGS/history.data')
logcenT = h.log_center_T
logcenRho = h.log_center_Rho
logcenRho1 = []
logcenT1 = []
for i in range(len(logcenRho)):
    if logcenRho[i] <9.934:
        logcenRho1.append(logcenRho[i])
        logcenT1.append(logcenT[i])
plt.plot(logcenRho1,logcenT1,c='k')
plt.xlabel('log Center Density(g $cm^{-3})$')
plt.ylabel('log Center Temperature(K)')