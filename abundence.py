#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:48:15 2022

@author: her
"""
""" plot abundence of element """

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
plt.subplot(121)
plt.xlim(0,1.7)
plt.ylim(-5,0.5)
plt.plot(mass_1re,he4_1,label='he4'),plt.plot(mass_1re,mg24_1,label='mg24',c='b'),plt.plot(mass_1re,c12_1,label='c12'),plt.plot(mass_1re,ne20_1,label='ne20'),plt.plot(mass_1re,o16_1,label='o16'),plt.plot(mass_1re,si28_1,label='si28'),plt.plot(mass_1re,n14_1,label='n14'),plt.plot(mass_1re,he3_1,label='he3'),plt.plot(mass_1re,na24_1,label='na24'),plt.plot(mass_1re,ne24_1,label='ne24')
plt.xlabel('$m/M\odot$')
plt.ylabel('log mass fraction')
plt.title('Abundance')
plt.text(1.3,0.6,'model 29800')
plt.legend()

plt.subplot(122)
plt.xlim(0,1.7)
plt.ylim(-5,0.5)
plt.plot(mass_44re,he4_44,label='he4'),plt.plot(mass_44re,mg24_44,label='mg24',c='b'),plt.plot(mass_44re,c12_44,label='c12'),plt.plot(mass_44re,ne20_44,label='ne20'),plt.plot(mass_44re,o16_44,label='o16'),plt.plot(mass_44re,si28_44,label='si28'),plt.plot(mass_44re,n14_44,label='n14'),plt.plot(mass_44re,he3_44,label='he3'),plt.plot(mass_44re,o20_44,label='o20'),plt.plot(mass_44re,ne24_44,label='ne24'),plt.plot(mass_44re,na24_44,label='na24'),plt.plot(mass_44re,f20_44,label='f20')
plt.xlabel('$m/M\odot$')
plt.ylabel('log mass fraction')
plt.title('Abundance')
plt.text(1.5,0.6,'model 41800')
plt.legend()