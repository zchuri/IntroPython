#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:20:15 2019

@author: zchuri
"""

# Clear workspace
#%reset -f

# Set working directory
import os
os.chdir("/misc/sherrington/zgtabuenca/nipype/Scripts/")

print("####################################################")
print("Nipype - DWI preprocessing pipeline")
print("####################################################")

########################################################################
# 1) Get initial parameters
print("1) Getting initial parameters")

dwinii = "/misc/sherrington/zgtabuenca/nipype/BIDS/sub-ado50129/ses-1/dwi/sub-ado50129_ses-1_acq-B800_run-1_dwi.nii.gz"
bvec = "/misc/sherrington/zgtabuenca/nipype/BIDS/sub-ado50129/ses-1/dwi/sub-ado50129_ses-1_acq-B800_run-1_dwi.bvec"
bval = "/misc/sherrington/zgtabuenca/nipype/BIDS/sub-ado50129/ses-1/dwi/sub-ado50129_ses-1_acq-B800_run-1_dwi.bval"
outdir = "/misc/sherrington/zgtabuenca/nipype/prep/sub-ado50129/ses-1/"

########################################################################
# 2) DWI preprocessing pipeline

print("2) Preprocessing")

# If ouput directory does not exists create it.
if(not os.path.isdir(outdir)):
	os.makedirs(outdir)

print("2.1) Convert to MRtrix3 data type")

# Import packages
import nipype.interfaces.mrtrix3 as mrtrix3

# Outfile
dwimif = outdir + "dwi.mif"
# Convert to .mif
mrconvert = mrtrix3.MRConvert()
mrconvert.inputs.in_file = dwinii
mrconvert.inputs.grad_fsl = (bvec, bval)
mrconvert.inputs.out_file = dwimif
mrconvert.cmdline
mrconvert.run()

print("2.2) Denoise (PCA)")

# Outfile
dwidn = outdir + "dwi_dn.mif"
# Denoise
denoise = mrtrix3.DWIDenoise()
denoise.inputs.in_file = dwimif
denoise.inputs.out_file = dwidn
denoise.cmdline
denoise.run()

print("2.3) Eddy currents and motion correction")

# Outfile
dwipp = outdir + "dwi_pp.mif"
eddyqc = outdir + "eddyqc"
# Eddy currents and motion correction
preproc = "/home/inb/lconcha/fmrilab_software/mrtrix3.git//bin/dwipreproc"
cmd = preproc + " " + dwidn + " " + dwipp + " -rpe_none -pe_dir PA -eddyqc_text " + eddytxt
print(cmd)
os.system(cmd)

print("2.4) Inhomogenety correction")

print("Work in progress...")

########################################################################
# 3) Compute tensor model

print("3) Compute tensor model")

print("3.1) Convert to FSL data type")

# Outfiles
dwinii_pp = outdir + "dwi_pp.nii.gz"
bvec_pp = outdir + "dwi_pp.bvec"
bval_pp  = outdir + "dwi_pp.bval"
# Convert to .nii.gz
mrconvert = "/home/inb/lconcha/fmrilab_software/mrtrix3.git//bin/mrconvert"
cmd = mrconvert + " -export_grad_fsl " + bvec_pp + " " + bval_pp + " " + dwipp + " " + dwinii_pp
print(cmd)
os.system(cmd)

print("3.2) Mask DWI")

# Outfile
dwimsk = outdir + "mask.nii.gz"
# Brain mask
bmsk = mrtrix3.BrainMask()
bmsk.inputs.in_file = dwipp
bmsk.inputs.out_file = dwimsk
bmsk.cmdline
bmsk.run()

print("3.3) Compute tensor model")

# Outfile
dtinii = outdir + "dti.nii.gz"
# Fit tensor
tsr = mrtrix3.FitTensor()
tsr.inputs.in_file = dwinii_pp
tsr.inputs.in_mask = dwimsk
tsr.inputs.grad_fsl = (bvec_pp, bval_pp)
tsr.inputs.out_file = dtinii
tsr.cmdline
tsr.run() 

print("3.4) Calculate tensor metrics")

# Outfiles
fanii = outdir + "fa.nii.gz"
adcnii = outdir + "adc.nii.gz"
# Tensor to metric
tsr2met = mrtrix3.TensorMetrics()
tsr2met.inputs.in_file = dtinii
tsr2met.inputs.in_mask = dwimsk
tsr2met.inputs.grad_fsl = (bvec_pp, bval_pp)
tsr2met.inputs.out_fa = fanii
tsr2met.inputs.out_adc = adcnii
tsr2met.cmdline
tsr2met.run()

print("3.4) Remove intermediate files")

print("Work in progress...")

