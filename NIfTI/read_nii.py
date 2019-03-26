#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:10:15 2019

@author: churi
"""

# Clear workspace
%reset -f

# Set working directory
#import os
#os.chdir("your_path")

# Clase 6 - NIfTI

#Load packages

import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib

# Load T1w volume
# http://fcon_1000.projects.nitrc.org/fcpClassic/FcpTable.html

img = nib.load("t1w.nii.gz")
print(dir(img))

# Export img values
datos = img.get_data()
dim_datos = datos.shape
# Plot every slice
for i in range(dim_datos[2]):
    imgN = datos[:,:,i]
    plt.imshow(imgN, cmap="gray")
    plt.pause(.1)
    plt.draw()

# Load fMRI volume
img = nib.load("bold.nii.gz")
datos = img.get_data()
dim_datos = datos.shape

# Extract one voxel timeseries
ts = datos[35,35,19,:]
plt.plot(ts)

