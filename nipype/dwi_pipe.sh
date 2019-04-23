#!/bin/bash

print_help() {
echo " 
Preprocessing pipeline for diffusion weighted images (DWI).
Usage: add a DWI NIfTI file and its vectors (.bvec and .bval) 
       and return diffusion tensor images (DTI) into an
       output directory
       dwi_pipe.sh dwi.nii.gz dwi.bvec dwi.bval outdir
Zeus Chiripa
14 Mar 2018
zgtabuenca@gmail.com
"
}

########################################################################
# 0) Help
if [ $# -eq 0  -o "$1" == "-h" -o "$1" == "--help" ]; then
	print_help;
	exit 0;
fi

########################################################################
# 1) Get initial parameters

# Start running time
res1=$(date +%s.%N)

echo -e "##############################"
echo -e "DWI preprocessing pipeline"
echo -e "##############################"

echo -e "\n1) Getting initial parameters\n"

dwinii=$1
bvec=$2
bval=$3
outdir=$4

#Set MRtrix v3 & FSL v5.0.9
source /home/inb/lconcha/fmrilab_software/tools/setup_mrtrix3_git.sh
source /home/inb/lconcha/fmrilab_software/tools/setup_fsl509

########################################################################
# 2) DWI preprocessing pipeline

echo -e "\n2) Preprocessing"

if [ ! -d "${outdir}" ]; then
	# If ouput directory does not exists create it.
        mkdir -p ${outdir}
fi

# First, noise correction
echo -e "\n\t-Noise correction\n"
dwidenoise -force ${dwinii} ${outdir}DWI_dn.nii.gz

# Second, eddy currents and motion correction
echo -e "\n\t-Eddy currents and motion correction\n"
dwipreproc -force -rpe_none -fslgrad ${bvec} ${bval} AP ${outdir}DWI_dn.nii.gz ${outdir}DWI_pp.nii.gz

########################################################################
# 3) Compute tensor model

echo -e "\n3) Compute tensor model\n"
dwi2mask -force -fslgrad ${bvec} ${bval} ${outdir}DWI_pp.nii.gz ${outdir}DWI_mask.nii.gz
dwi2tensor -force -mask ${outdir}DWI_mask.nii.gz -fslgrad ${bvec} ${bval} ${outdir}DWI_pp.nii.gz ${outdir}DTI.nii.gz
tensor2metric -force -adc ${outdir}DTI_ADC.nii.gz -fa ${outdir}DTI_FA.nii.gz -mask ${outdir}DWI_mask.nii.gz ${outdir}DTI.nii.gz

########################################################################
# 4) Remove intermediate files

echo -e "\n4) Remove intermediate files\n"
rm ${outdir}DWI_dn.nii.gz

########################################################################
# 5) Print running time


# End running time
# https://unix.stackexchange.com/questions/52313/how-to-get-execution-time-of-a-script-effectively
res2=$(date +%s.%N)
dt=$(echo "$res2 - $res1" | bc)
dd=$(echo "$dt/86400" | bc)
dt2=$(echo "$dt-86400*$dd" | bc)
dh=$(echo "$dt2/3600" | bc)
dt3=$(echo "$dt2-3600*$dh" | bc)
dm=$(echo "$dt3/60" | bc)
ds=$(echo "$dt3-60*$dm" | bc)

printf "Total runtime: %d:%02d:%02d:%02.4f\n" $dd $dh $dm $ds


