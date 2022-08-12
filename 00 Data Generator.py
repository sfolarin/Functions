from numpy import*
import matplotlib as m
import pandas as pd
import numpy as np
from numpy.linalg import*
import matplotlib.pyplot as plt
import subprocess

N=36
R=3
M=15
label='Planexy_{}'.format(M)
Q='e11'

for num in range(0,2000,200):
    # Decreasing field 36
    # data1 = np.loadtxt('decrease_field_10k\dfield_{}_10k\PIEZO_homo_{}'.format(num,num))
    # data2 = np.loadtxt('decrease_field_10k\dfield_{}_10k\VectFieldX'.format(num))
    
    # Decreasing field 54
    # data1 = np.loadtxt('decrease_field_10k\dfield_{}_10k\PIEZO_homo_{}'.format(num,num))
    # data2 = np.loadtxt('decrease_field_10k\dfield_{}_10k\VectFieldX'.format(num))
    
    # Increasing field 36
    # data1 = np.loadtxt('Field10k_Dot\Field_{}_10k\PIEZO_homo_{}'.format(num,num))
    # data2 = np.loadtxt('Field10k_Dot\Field_{}_10k\VectFieldX'.format(num))
    
    # Increasing field 54
    data1 = np.loadtxt('Increase_Field_54_10K\Field_{}_10K\PIEZO_homo_{}'.format(num,num))
    data2 = np.loadtxt('Increase_Field_54_10K\Field_{}_10K\VectFieldX'.format(num))
    
    df = pd.DataFrame(data2)
    # Sort multiple columns
    df2 = df.sort_values([0,2,1])
    df3 = df.sort_values([1,2,0])
    savetxt("YZ_{}.dat".format(num),df2)
    savetxt("XZ_{}.dat".format(num),df3)
    
    df_p = pd.DataFrame(data1)
    
    df4 = df_p.sort_values([0,2,1])
    df5 = df_p.sort_values([1,2,0])

    savetxt("YZ_piezo_{}.dat".format(num),df4)
    savetxt("XZ_piezo_{}.dat".format(num),df5)