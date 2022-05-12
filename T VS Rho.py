#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:24:44 2022

@author: her
"""

import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np


'''grab the data'''
l = mr.MesaLogDir('../LOGS')
p_1 = l.profile_data(profile_number=1)
p_2 = l.profile_data(profile_number=70)
logT1 = list(p_1.logT)
logRho1 = list(p_1.logRho)
logT = list(p_2.logT)
logRho = list(p_2.logRho)
conv = list(p_2.conv_mixing_type)
eps_nuc = list(p_1.eps_nuc)
eps_nuc2 = list(p_2.eps_nuc)
psi4 = np.loadtxt('../psi4.txt',dtype = float)
heburn = np.loadtxt('../helium_burn.txt',dtype = float)
cburn = np.loadtxt('../carbon_burn.txt',dtype = float)
oburn = np.loadtxt('../oxygen_burn.txt',dtype = float)


"""Determine whether it is a convection zone"""
logT_conv = list()
logT_nonconv = list()
logRho_conv = list()
logRho_nonconv = list()
logRho_conv1 = list()
logRho_conv2 = list()
logRho_conv3 = list()
logRho_conv4 = list()
logT_conv1 = list()
logT_conv2 = list()
logT_conv3 = list()
logT_conv4 = list()
logRho_overst = list()
logT_overst = list()
T_eps_nuc7 = list()
Rho_eps_nuc7 = list()
T_eps_nuc3 = list()
Rho_eps_nuc3 = list()
T_eps_nuc1 = list()
Rho_eps_nuc1 = list()
T2_eps_nuc7 = list()
Rho2_eps_nuc7 = list()
T2_eps_nuc3 = list()
Rho2_eps_nuc3 = list()
T2_eps_nuc1 = list()
Rho2_eps_nuc1 = list()
'''divide convection zone,non-convextion zone and overshooting zone'''
for i in range(0,len(conv)):
    if conv[i] == 1:
        logT2 = logT[i]
        logT_conv.append(logT2)
    elif conv[i] == 0:
        logT3 = logT[i] 
        logT_nonconv.append(logT3)
    elif conv[i] == 3:
        logT_overst.append(logT[i])
for i in range(0,len(conv)):
    if conv[i] == 1:
        logRho2 = logRho[i]
        logRho_conv.append(logRho2)
    elif conv[i] == 0:
        logRho3 = logRho[i]
        logRho_nonconv.append(logRho3)       
    elif conv[i] == 3:
        logRho_overst.append(logRho[i])


'''Subdivided Convective Zones for last model'''
for i in range(0,len(logRho_conv)):
    if logRho_conv[i] < 0:
        logRho_conv1.append(logRho_conv[i])
        logT_conv1.append(logT_conv[i])
    elif logRho_conv[i] <6.3:
        logRho_conv2.append(logRho_conv[i])
        logT_conv2.append(logT_conv[i])
    elif logRho_conv[i] < 6.9:
       logRho_conv3.append(logRho_conv[i])
       logT_conv3.append(logT_conv[i])
    else:
        logRho_conv4.append(logRho_conv[i])
        logT_conv4.append(logT_conv[i])

'''Determining whether a nuclear reaction has occurred'''
for i in range(len(eps_nuc)):
    if eps_nuc[i] > 1e7:
        T_eps_nuc7.append(logT1[i])
        Rho_eps_nuc7.append(logRho1[i])
    elif eps_nuc[i] > 1e3:
        T_eps_nuc3.append(logT1[i])
        Rho_eps_nuc3.append(logRho1[i])
    elif eps_nuc[i] > 1:
        T_eps_nuc1.append(logT1[i])
        Rho_eps_nuc1.append(logRho1[i])
for i in range(len(eps_nuc2)):
    if eps_nuc2[i] > 1e7:
        T2_eps_nuc7.append(logT[i])
        Rho2_eps_nuc7.append(logRho[i])
    elif eps_nuc2[i] > 1e3:
        T2_eps_nuc3.append(logT[i])
        Rho2_eps_nuc3.append(logRho[i])
    elif eps_nuc2[i] > 1:
        T2_eps_nuc1.append(logT[i])
        Rho2_eps_nuc1.append(logRho[i])



'''plot'''
plt.xlim(-6,12)
plt.ylim(3,11)
plt.xlabel('log Density(g $cm^{-3} $)')
plt.ylabel('log Temperature(K)')
plt.plot(Rho2_eps_nuc7,T2_eps_nuc7,'o',linewidth='5',c='#8B0000')
plt.plot(Rho2_eps_nuc3,T2_eps_nuc3,'o',linewidth='5',c='#FF6347')
plt.plot(Rho2_eps_nuc1,T2_eps_nuc1,'o',linewidth='5',c='#FFA500')
plt.plot(logRho_conv1,logT_conv1,'b',linewidth='5',label='convction')
plt.plot(logRho_conv2,logT_conv2,'b',linewidth='5')
plt.plot(logRho_conv3,logT_conv3,'b',linewidth='5')
plt.plot(logRho_conv4,logT_conv4,'b',linewidth='5')
plt.plot(logRho_overst,logT_overst,linewidth='5',label='overshooting')
plt.plot(Rho_eps_nuc7,T_eps_nuc7,'o',linewidth='5',c='#8B0000')
plt.plot(Rho_eps_nuc3,T_eps_nuc3,'o',linewidth='5',c='#FF6347')
plt.plot(Rho_eps_nuc1,T_eps_nuc1,'o',linewidth='5',c='#FFA500')
plt.plot(logRho,logT,c='#363636',linewidth='2',label='nonconvction')
plt.legend(frameon=False,fontsize='medium')

'''draw auxiliary lines'''
plt.plot(psi4[:,0],psi4[:,1],'k:')
plt.plot(heburn[:,0],heburn[:,1],'k:')
plt.plot(cburn[:,0],cburn[:,1],'k:')
plt.plot(oburn[:,0],oburn[:,1],'k:')
plt.text(-1.12,8.221,'Helium burn'),plt.text(0.20,8.74,'Carbon burn'),plt.text(1.45,9.115,'Oxygen burn'),plt.text(1.55,5.615,"$\\varepsilon _{F} /kT \\approx 4$",fontsize = 20, rotation = 35)
plt.plot(logRho1,logT1,linewidth='2',c='#363636')
plt.text(-5.3,10.3,'$>10^{7}\\ erg\\ s^{-1}$',c='#8B0000',fontsize=15)
plt.text(-5.3,10,'$>10^{3}\\ erg\\ s^{-1}$',c='#FF6347',fontsize=15)
plt.text(-5.3,9.7,'$>1\\ erg\\ s^{-1}$',c='#FFA500',fontsize=15)
plt.text(-5.3,9,'(1) initial',fontsize=18)
plt.text(-4,5.8,'(1)',fontsize=15)
plt.text(-5.3,8.6,'(2) C ignite',fontsize=18)
plt.text(-4.4,6.2,'(2)',fontsize=15)