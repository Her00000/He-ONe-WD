#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:12:09 2022

@author: her
"""

import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np

'''grab the data'''
h = mr.MesaData('../LOGS/history.data')
center_T = h.log_center_T
center_Rho = h.log_center_Rho

'''plot'''
plt.plot(center_Rho,center_T)
plt.plot(center_Rho[9],center_T[9],'o',c='b')
plt.plot(center_Rho[7876],center_T[7876],'o',c='b')
plt.xlabel('log Center Density(g $cm^{-3} $)')
plt.ylabel('log Center Temperature(K)')
plt.show()