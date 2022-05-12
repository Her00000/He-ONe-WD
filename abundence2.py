#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:25:13 2022

@author: her
"""

import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np

# load entire LOG directory information
l = mr.MesaLogDir('../LOGS')

# grab the last profile
p_1 = l.profile_data(profile_number=68)
p_44 = l.profile_data(profile_number=284)

# the abundence of p_1 main element
mass_1re = p_1.mass
he4_1 = np.log10(p_1.he4)
mg24_1 = np.log10(p_1.mg24)
c12_1 = np.log10(p_1.c12)
o16_1 = np.log10(p_1.o16)
ne20_1 = np.log10(p_1.ne20)
si28_1 = np.log10(p_1.si28)
n14_1 = np.log10(p_1.n14)
he3_1 = np.log10(p_1.he3)
na24_1 = np.log10(p_1.na24)
ne24_1 = np.log10(p_1.ne24)
# the abundence of p_44 main element
mass_44re =p_44.mass
he4_44 = np.log10(p_44.he4)
mg24_44 = np.log10(p_44.mg24)
c12_44 = np.log10(p_44.c12)
o16_44 = np.log10(p_44.o16)
ne20_44 = np.log10(p_44.ne20)
si28_44 = np.log10(p_44.si28)
n14_44 = np.log10(p_44.n14)
he3_44 = np.log10(p_44.he3)
o20_44 = np.log10(p_44.o20)
ne24_44 = np.log10(p_44.ne24)
na24_44 = np.log10(p_44.na24)
f20_44 = np.log10(p_44.f20)

''' draw the picture with ax
fig = plt.Figure()
ax1 = fig.add_subplot(211)
ax1.plot(mass_1re,he4_1,label='he4'),ax1.plot(mass_1re,mg24_1,label='mg24',c='b'),ax1.plot(mass_1re,c12_1,label='c12'),ax1.plot(mass_1re,ne20_1,label='ne20'),ax1.plot(mass_1re,o16_1,label='o16'),ax1.plot(mass_1re,si28_1,label='si28'),ax1.plot(mass_1re,n14_1,label='n14'),ax1.plot(mass_1re,he3_1,label='he3')
'''

#drow the picture
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
plt.subplot(221)
plt.xlim(0,1.7)
plt.ylim(-5,0.5)
plt.plot(mass_1re,he4_1,label='he4'),plt.plot(mass_1re,mg24_1,label='mg24',c='b'),plt.plot(mass_1re,c12_1,label='c12'),plt.plot(mass_1re,ne20_1,label='ne20'),plt.plot(mass_1re,o16_1,label='o16'),plt.plot(mass_1re,si28_1,label='si28'),plt.plot(mass_1re,n14_1,label='n14'),plt.plot(mass_1re,he3_1,label='he3')
plt.xlabel('$m/M\odot$')
plt.ylabel('log mass fraction')
plt.title('Abundance')
plt.text(1.4,0.6,'model 6600')
plt.text(0.83,-6.2,'(a)',fontsize=15)
plt.legend(frameon=True,fontsize='medium')

plt.subplot(222)
plt.xlim(1.15,1.35)
plt.ylim(-5,0.5)
plt.plot(mass_1re,he4_1,label='he4'),plt.plot(mass_1re,mg24_1,label='mg24',c='b'),plt.plot(mass_1re,c12_1,label='c12'),plt.plot(mass_1re,ne20_1,label='ne20'),plt.plot(mass_1re,o16_1,label='o16'),plt.plot(mass_1re,si28_1,label='si28'),plt.plot(mass_1re,n14_1,label='n14'),plt.plot(mass_1re,he3_1,label='he3')
plt.xlabel('$m/M\odot$')
plt.ylabel('log mass fraction')
plt.title('Enlarged Abundance')
plt.text(1.32,0.6,'model 6600')
plt.text(1.25,-6.2,'(b)',fontsize=15)
plt.legend(frameon=True,fontsize='medium')

plt.subplot(223)
plt.xlim(0,1.7)
plt.ylim(-5,0.5)
plt.plot(mass_44re,he4_44,label='he4'),plt.plot(mass_44re,mg24_44,label='mg24',c='b'),plt.plot(mass_44re,c12_44,label='c12'),plt.plot(mass_44re,ne20_44,label='ne20'),plt.plot(mass_44re,o16_44,label='o16'),plt.plot(mass_44re,si28_44,label='si28'),plt.plot(mass_44re,n14_44,label='n14'),plt.plot(mass_44re,he3_44,label='he3')
plt.xlabel('$m/M\odot$')
plt.ylabel('log mass fraction')
plt.title('Abundance')
plt.text(1.4,0.6,'model 29800')
plt.text(0.83,-6.2,'(c)',fontsize=15)
plt.legend(frameon=True,fontsize='medium')

plt.subplot(224)
plt.xlim(1.15,1.45)
plt.ylim(-5,0.5)
plt.plot(mass_44re,he4_44,label='he4'),plt.plot(mass_44re,mg24_44,label='mg24',c='b'),plt.plot(mass_44re,c12_44,label='c12'),plt.plot(mass_44re,ne20_44,label='ne20'),plt.plot(mass_44re,o16_44,label='o16'),plt.plot(mass_44re,si28_44,label='si28'),plt.plot(mass_44re,n14_44,label='n14'),plt.plot(mass_44re,he3_44,label='he3')
plt.xlabel('$m/M\odot$')
plt.ylabel('log mass fraction')
plt.text(1.4,0.6,'model 29800')
plt.title('Enlarged Abundance')
plt.text(1.3,-6.2,'(d)',fontsize=15)
plt.legend(frameon=True,fontsize='medium')
