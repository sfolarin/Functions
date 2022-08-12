import math
from numpy import*
import numpy as np
from numpy.linalg import*
import matplotlib.pyplot as plt

# Change these values```````````````````````````
fO="in" #Field orientation

N=36 #Change for-loop to range(0,2200,200)
# N=54 #Change for-loop to range(0,2000,200)

# Size 36
for i in range(0,2200,200): #for increasing field
# for i in range(1800,-200,-200): #for decreasing field

# Size 54
#for i in range(0,2000,200): #for increasing field
# for i in range(1600,-200,-200): #for decreasing field
    eF=i    #Electric field strength
    
    # ```````````````````````````````````````````````
    data = np.load("xy{}({}) {}kV.npy".format(N,fO,eF))
    data1 = np.load("xz{}({}) {}kV.npy".format(N,fO,eF))
    data2 = np.load("yz{}({}) {}kV.npy".format(N,fO,eF))
    
    if len(data1)!=0 and len(data2)!=0:
        fig = plt.figure()
        ax = plt.axes(projection ='3d')
        
        # Data for three-dimensional scattered points
        #XY cross section
        xdata = data[:,0]
        ydata = data[:,1]
        zdata = data[:,2]
        
        #XZ cross section
        xdata1 = data1[:,0]
        ydata1 = data1[:,2]
        zdata1 = data1[:,1]
        
        #YZ cross section
        xdata2 = data2[:,2]
        ydata2 = data2[:,0]
        zdata2 = data2[:,1]
        
        d = np.sqrt(xdata**2+ydata**2+zdata**2)
        d = d/d.max()
        d1 = np.sqrt(xdata1**2+ydata1**2+zdata1**2)
        d1=d1/d1.max()
        d2 = np.sqrt(xdata2**2+ydata2**2+zdata2**2)
        d2=d2/d2.max()
        
        ax.scatter3D(xdata, ydata, zdata, c=d, cmap="Reds", edgecolors='black', depthshade=False)
        ax.scatter3D(xdata1, ydata1, zdata1, c=d1, cmap="Reds", edgecolors='black',depthshade=False)
        ax.scatter3D(xdata2, ydata2, zdata2, c=d2, cmap="Reds", edgecolors='black',depthshade=False)
        
        ax.scatter3D(xdata, ydata, zdata, facecolors=plt.cm.Reds(d), edgecolors='black')
        ax.scatter3D(xdata1, ydata1, zdata1,facecolors = plt.cm.Reds(d1), edgecolors='black')
        ax.scatter3D(xdata2, ydata2, zdata2,facecolors = plt.cm.Reds(d2), edgecolors='black')
        
        ax.view_init(20,120)
        
        ax.set_title('{}x{}x{} 3-in-1 {}kV/cm ({})'.format(N,N,N,eF,fO))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        plt.xticks()
        plt.yticks()
        
        # plt.xlim(max(xdata), min(xdata))
        # plt.ylim(min(ydata), max(ydata))
        plt.xlim(N, 0)
        plt.ylim(0, N)
        
        # plt.gca().set_xticklabels(['']*10)
        # plt.gca().set_yticklabels(['']*10)
        # plt.gca().set_zticklabels(['']*10)
        
        # plt.show()
    else:
        #Only the XY cross section persists
        fig = plt.figure()
        ax = plt.axes(projection ='3d')
        
        xdata = data[:,0]
        ydata = data[:,1]
        zdata = data[:,2]
        
        d = np.sqrt(xdata**2+ydata**2+zdata**2)
        d = d/d.max()
        
        ax.scatter3D(xdata, ydata, zdata, c=d, cmap="Reds", edgecolors='black', depthshade=False)
        ax.scatter3D(xdata, ydata, zdata, facecolors=plt.cm.Reds(d), edgecolors='black')
        ax.view_init(20,120)
        
        ax.set_title('{}x{}x{} 3-in-1 {}kV/cm ({})'.format(N,N,N,eF,fO))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        plt.xticks()
        plt.yticks()
        
        # plt.xlim(max(xdata), min(xdata))
        # plt.ylim(min(ydata), max(ydata))
        
        plt.xlim(N, 0)
        plt.ylim(0, N)
        
        # plt.gca().set_xticklabels(['']*10)
        # plt.gca().set_yticklabels(['']*10)
        # plt.gca().set_zticklabels(['']*10)
        
        plt.show()