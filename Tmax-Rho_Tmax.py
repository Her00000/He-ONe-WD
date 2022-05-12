#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:14:47 2022

@author: her
"""

import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np

'''grab the data'''
h = mr.MesaData('../LOGS/history.data')
Tmax = h.log_max_T
Rho_tmax = h.max_T_lgRho
mass = h.star_mass

fig, ax1 = plt.subplots()
ax1.plot(mass,Tmax,label=u'Tmax')
plt.plot(mass[8536],Tmax[8536],'o',c='#000080')
ax1.set_xlabel('$m/M\odot$')
ax1.set_ylabel('Tmax')
ax1.legend()
plt.legend(loc='upper left')
ax2 = ax1.twinx()
ax2.plot(mass,Rho_tmax,c='r',label='$\\rho _{Tmax} $')
plt.plot(mass[8536],Rho_tmax[8536],'o')
ax2.set_ylabel('$\\rho _{Tmax} $')
ax1.set_ylim(2,11)
ax2.set_ylim(2,11)
ax2.legend()
plt.legend()
