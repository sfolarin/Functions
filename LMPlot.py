#!/usr/bin/env python
# coding: utf-8

# In[2]:


from numpy import*
from scipy import*
from numpy.linalg import*
from matplotlib import pylab as plt
import pandas as pd
import numpy as np

def Annealing():
    init_temp = int(input('Enter Initial Value of Temperature: '))
    final_temp = int(input('Enter Final Value of Temperature: '))
    temp = len(np.arange(init_temp,final_temp+10,10))
    nstep =1500
    relax = 0
    m = input('Enter the name of the file in .dat format: ')

    a=open(m)
    b=a.readlines()
    data = zeros((temp*nstep,7))
    for j in range(temp*nstep):
        b[j]=b[j].split()
        data[j,:] = list(map(float,b[j]))
    disp = data[:,:]
    p = zeros((temp,3))





    for i in arange(temp):
        p[i,0] = (average(disp[relax+1500*i:1500*(i+1),1]))*1308
        p[i,1] = (average(disp[relax+1500*i:1500*(i+1),3]))*1308
        p[i,2] = (average(disp[relax+1500*i:1500*(i+1),5]))*1308
        
    dframe = pd.DataFrame(p, columns =['LM_X', 'LM_Y', 'LM_Z'])
    dframe['Temp'] =np.arange(init_temp,final_temp+10,10)
    dframe
    
    
    
    P_x = dframe['LM_X']
    P_y = dframe['LM_Y']
    P_z = dframe['LM_Z']
    Temp = dframe['Temp']



    fig,ax = plt.subplots(figsize=(7,7))
    ax.plot(Temp, P_x, 'r', marker='s',label='P_x')

    ax.plot(Temp, P_y, 'b',marker='s', label ='P_y')

    ax.plot(Temp, P_z, 'g', marker='s',label='P_z')




    ax.set_ylabel('$\chi$', fontsize =16)
    font = {'family': 'serif','color': 'darkred','weight': 'normal','size': 16}
    #plt.gca().invert_yaxis()
    #plt.plot(step, local_mode)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.xaxis.set_tick_params(which='major', size=5, width=0.5, direction='in', bottom=True)
    ax.yaxis.set_tick_params(which='major', size=5, width=0.5, direction='in', left=True)
    #plt.suptitle('$\chi$ against Temperatures for (-2kv/cm to 6kv/cm) with polynomial order 4', fontdict=font)
    ax.set_ylabel('Polarization($\mu C/cm^2$)', fontdict=font, labelpad=10)
    ax.set_xlabel('Temp(K)', fontdict=font, labelpad=10)
    ax.legend(loc='upper left',frameon=True, fontsize=16, bbox_to_anchor=(1.0, 1.0))
    ax.set_title('0% Conc')





    #ax.legend()
    plt.show()
    return ax





