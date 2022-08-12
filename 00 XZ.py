# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:12:48 2022

@author: John Zhou
"""

import math
from numpy import*
import matplotlib as m
import pandas as pd
import numpy as np
from numpy.linalg import*
import matplotlib.pyplot as plt
import subprocess

N=54

fO="in"

for i in range(0,2000,200):
    eF=i
    
    coordinates=[]
    def XZ(N,R,label,M,Q):
        initial=eF
        final=initial+200
        for num in range(initial,final,200):
            data1 = np.loadtxt('XZ_piezo_{}.dat'.format(num))
            data2 = np.loadtxt('XZ_{}.dat'.format(num))
            
            plt.rc('axes', linewidth=2)
    
            b = array(data1[:])
            a = array(data2[:])
    
            x = zeros((N*N))
            y = zeros((N*N))
            z = zeros((N*N))
    
            x[:] = a[N*N*M:N*N*(M+1),3]
            y[:] = a[N*N*M:N*N*(M+1),5]
            z[:] = b[N*N*M:N*N*(M+1),R]
    
            x1 = transpose(x.reshape(N,N))
            y1 = transpose(y.reshape(N,N))
            z1 = transpose(z.reshape(N,N))
            
            # Acquiring the data in the range between s1 to s2.`````````````
            
            # Standardization
            s1=2
            s2=N-2
    
            sr=s2-s1
    
            # Creating zero-arrays.
            xs=zeros((sr**2))
            ys=zeros((sr**2))
            zs=zeros((sr**2))
    
            # Reshaping xs, ys, zs into srxsr matrices.
            xs1 = transpose(xs.reshape(sr,sr))
            ys1 = transpose(ys.reshape(sr,sr))
            zs1 = transpose(zs.reshape(sr,sr))
    
            # Slicing the data to find the submatrix.
            xs1[:] = x1[s1:s2 , s1:s2]
            ys1[:] = y1[s1:s2 , s1:s2]
            zs1[:] = z1[s1:s2 , s1:s2]
            
            # Gen.Code~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
            MA=31
            # Finding the angles of dipoles wrt. the x-axis.
            angles=[]
            angles2=[]
    
            for i in arange(sr):
                for j in arange(sr):
                    dx=xs1[i,j]
                    dy=ys1[i,j]
                    coor=[dx,dy]
                    angle = np.arctan2(dy,dx)
                    p = round(np.degrees(angle))
                    angles.append([p,i,j])
                    
            for i in arange(sr):
                for j in arange(sr):
                    dx2=xs1[j,i]
                    dy2=ys1[j,i]
                    coor2=[dx2,dy2]
                    angle2 = np.arctan2(dy2,dx2)
                    p2 = round(np.degrees(angle2))
                    angles2.append([p2,j,i])
    
            # Summoning the Uzumaki monster:
            a2 = array(angles)
            v1=[]
    
            b2 = array(angles2)
    
            uL=[]
    
            for index, i in enumerate(a2):
                if(index<(len(a2)-1)):
                    j=a2[index+1]
                else:
                    j=a2[0]
                
                i[0] = mod(i[0],360)
                j[0] = mod(j[0],360)
                
                normDeg = mod(i[0]-j[0],360)
                absDiffDeg = min(360-normDeg, normDeg)
    
                if absDiffDeg > MA and i[0]>j[0] and i[1]==j[1] and abs(i[2]-j[2])<2:
                    v1.append([j[1],j[2]])
                    
                    uL.append([j[0],j[1],j[2]])
    
            if bool(uL):
                # Potential upper left coordinates
                # uL=array(uL)
                uL=sorted(uL, key = lambda x: (x[2], x[1]), reverse=False)
                uL=array(uL)
                
                v1=sorted(v1, key = lambda x: (x[1], x[0]), reverse=False)
                # Creating a list of potential upper right coordinates
                v2=array(v1)
                v2[:,0] += 1
                v2=[i for i in v2 if i[0]<sr]
    
                # Look for angles of v2 in b2
                v3=[]
                for i in b2:
                    for j in v2:
                        if i[1] == j[0] and i[2] == j[1]:
                            v3.append(i[0])
    
                v3 = mod(v3,360)
                
                uR1=[]
                uR2=[]
                if bool(v2):
                    uR1 = np.column_stack((v3,v2))
                    uR2 = np.row_stack((uL,uR1))
                else: Ll=[]
    
                # Compare uL and uR1 horizontally
                uR3=[]
                for index, i in enumerate(uR2):
                    if(index<(len(uR2)-1)):
                        j=uR2[index+1]
                    else:
                        j=uR2[0]
                    
                    i[0] = mod(i[0],360)
                    j[0] = mod(j[0],360)
                    
                    normDeg = mod(i[0]-j[0],360)
                    absDiffDeg = min(360-normDeg, normDeg)
    
                    if absDiffDeg > MA and i[2]==j[2] and abs(i[1]-j[1])<2:
                        uR3.append([j[0],j[1],j[2]])
    
                # Potential upper right coordinates
                uR = array(uR3)
    
                if bool(uR3):
                    # Creating a list of potential lower right coordinates
                    Lr1=array(uR3)
                    Lr2=Lr1[:,1:3]
                    Lr2[:,1] -= 1
                    Lr2=[i for i in Lr2 if i[1]>=0]
                    
                    Lr2=sorted(Lr2, key = lambda x: (x[1], x[0]), reverse=False)
                    Lr2=array(Lr2)
                    
                    # # Look for angles of Lr2 in b2
                    Lr3=[]
                    for i in b2:
                        for j in Lr2:
                            if i[1] == j[0] and i[2] == j[1]:
                                Lr3.append(i[0])
                    
                    # Lr3 = mod(Lr3,360)
                    Lr4 = np.column_stack((Lr3,Lr2))
                    
                    # Compare uR and Lr4 vertically
                    Lr5 = np.row_stack((uR,Lr4))
                    Lr5=sorted(Lr5, key = lambda x: (x[1], x[2]), reverse=True)
                    Lr5=array(Lr5)
                    
                    Lr6=[]
                    for index, i in enumerate(Lr5):
                        if(index<(len(Lr5)-1)):
                            j=Lr5[index+1]
                        else:
                            j=Lr5[0]
                        
                        i[0] = mod(i[0],360)
                        j[0] = mod(j[0],360)
                        
                        normDeg = mod(i[0]-j[0],360)
                        absDiffDeg = min(360-normDeg, normDeg)
                    
                        if absDiffDeg > MA and i[0]>j[0] and i[1]==j[1] and abs(i[2]-j[2])<2:
                            Lr6.append([j[0],j[1],j[2]])
                    
                    Ll8=[]
                    if bool(Lr6):
                        Lr6 = [i for n, i in enumerate(Lr6) if i not in Lr6[:n]]
                        Lr6=sorted(Lr6, key = lambda x: (x[2], x[1]), reverse=True)
                        
                        # # Potential lower right coordinates
                        Lr = array(Lr6)
                        
                        # # Creating a list of potential lower left coordinates
                        Ll1=array(Lr6)
                        Ll2=Ll1[:,1:3]
                        Ll2[:,0] -= 1
                        Ll2=[i for i in Ll2 if i[0]>=0]
                        Ll2=sorted(Ll2, key = lambda x: (x[1], x[0]), reverse=False)
                        Ll2=array(Ll2)
                        
                        # Look for angles of Ll2 in b2
                        Ll3=[]
                        for i in b2:
                            for j in Ll2:
                                if i[1] == j[0] and i[2] == j[1]:
                                    Ll3.append(i[0])
                        
                        Ll3 = mod(Ll3,360)
                        Ll4 = np.column_stack((Ll3,Ll2))
                        
                        # Compare Lr and Ll4 horizontally
                        Ll5 = np.row_stack((Lr,Ll4))
                        Ll5=sorted(Ll5, key = lambda x: (x[2], x[1]), reverse=True)
                        Ll5=array(Ll5)
                        
                        Ll6=[]
                        for index, i in enumerate(Ll5):
                            if(index<(len(Ll5)-1)):
                                j=Ll5[index+1]
                            else:
                                j=Ll5[0]
                            
                            i[0] = mod(i[0],360)
                            j[0] = mod(j[0],360)
                            
                            normDeg = mod(i[0]-j[0],360)
                            absDiffDeg = min(360-normDeg, normDeg)
                        
                            if absDiffDeg > MA and i[2]==j[2] and abs(i[1]-j[1])<2:
                                Ll6.append([j[0],j[1],j[2]])
                        
                        Ll6 = [i for n, i in enumerate(Ll6) if i not in Ll6[:n]]
                        Ll6=sorted(Ll6, key = lambda x: (x[1], x[2]), reverse=False)
                        
    
                        if bool(Ll6):
                            Ll7=array(Ll6)
                            Ll8=Ll7[:,1:3]
                        else: Ll=[]
                    else: Ll=[]
                    
                    Ll=Ll8
                    
                else: Ll=[]
            else: Ll=[]
    
            # Get rid of out of bounds elements
            Ll=[i for i in Ll if i[0]>1 if i[0]<sr-1 if i[1]>1 if i[1]<sr-1]
            # Ll=array(Ll)
    
            # Get rid of clustered coordinates
            Ll10=[]
            Ll11=[]
            for index, i in enumerate(Ll):
                if(index<(len(Ll)-1)):
                    j=Ll[index+1]
                else:
                    j=Ll[0]
                
                if i[1]==j[1] and j[0]-i[0]==1:
                    Ll10.append(j)
                else: Ll11.append(j)
    
            Ll=array(Ll11)
    
            Ll12=[]
            Ll13=[]
            for index, i in enumerate(Ll):
                if(index<(len(Ll)-1)):
                    j=Ll[index+1]
                else:
                    j=Ll[0]
                
                if i[0]==j[0] and j[1]-i[1]==1:
                    Ll12.append(j)
                else: Ll13.append(j)
    
            Ll=array(Ll13)
            # print(Ll,M)
    
            # Recall that I padded the graph by two, so we have to remove that.
            # Final result.
            L = Ll
    
            for i in L:
                b = (i[0]+2, i[1]+2, M, num)
                print(b)
                coordinates.append(b)
            
            # Gen.Code~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
            fig,ax = plt.subplots(figsize=(10,8))
            cdict = {
            'red'  :  ( (0.0, 0.25, .25), (0.02, .59, .59), (1., 1., 1.)),
            'green':  ( (0.0, 0.0, 0.0), (0.02, .45, .45), (1., .97, .97)),
            'blue' :  ( (0.0, 1.0, 1.0), (0.02, .75, .75), (1., 0.45, 0.45))
            }
    
            cm = m.colors.LinearSegmentedColormap('my_colormap', cdict, 1024)
            
            vmin = np.min(np.array([data1[:,R],data2[:,R]]))
            vmax = np.max(np.array([data1[:,R],data2[:,R]]))
            
            l = arange(0,sr,1)
            q = arange(0,sr,1)
    
            X, Y = meshgrid(l, q)
    
            plot = plt.pcolormesh(l, q, zs1, cmap=cm, shading='gouraud')
            plot.set_clim(vmin,vmax)
            for i in arange(sr):
                for j in arange(sr):
                    ax.arrow(i, j, dx=(xs1[i,j])*0.55, dy=(ys1[i,j])*0.55, width=.06)
            
            clb = plt.colorbar()
            clb.ax.set_title(Q)
    
            plt.ylim(0,sr-1)
            plt.xlim(0,sr-1)
            plt.xticks(arange(0, sr-1, sr/4))
            plt.yticks(arange(0, sr-1, sr/4))
            plt.tick_params(labelbottom=False)
            plt.tick_params(labelleft=False)
            plt.xlabel('X', fontsize = 20)
            plt.ylabel('Z',fontsize = 20)
            plt.tick_params(direction='in', pad=10)
            plt.tick_params('both', length=5, width=2)
            plt.suptitle('Field --> {}Kv/cm and Size {} x {} x {} for Plane_{} 10K'.format(num,N,N,N,M))
            
            for i in Ll:
                plt.scatter(i[0],i[1],color="red")
            
            plt.show(block=True)
    
    for i in range(2,33):
        XZ(N,3,'Planexy_{}'.format(i),i,'e11')
    
    savetxt('xz{}({}) {}kV.dat'.format(N,fO,eF), coordinates, fmt='%4d')
    np.save("xz{}({}) {}kV".format(N,fO,eF), coordinates)