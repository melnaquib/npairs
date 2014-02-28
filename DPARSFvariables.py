import os
import csv
import glob
import numpy as np
from collections import defaultdict

dataset = 'NIAK'

#workingdir = '/home/rschadmin/Data/'+dataset+'working_dir'
workingdir = '/data/Projects/ABIDE_Initiative/CPAC/abide/for_grant/SVC_workingdir_dparsf'
#datadir = '/home/rschadmin/Data/'+dataset
datadir = '/home2/data/Projects/ABIDE_Initiative/DPARSF/ReNormalize'

dg_template = dict(dr_files= os.path.join(datadir,'%s/dual_regression/*%s*.nii'),
                   reho_files= os.path.join(datadir,'*%s/reho/*%s*.nii'),
                   falff_files=os.path.join(datadir,'*%s/falff/*%s*.nii'),
                   mask_file = os.path.join(datadir,'/data/Projects/ABIDE_Initiative/CPAC/abide/for_grant/rois/mask_100percent.nii.gz'))

dg_args = dict(falff_files= [['preproc_id','subject_id']],
                                            reho_files= [['preproc_id','subject_id']],
                                            dr_files= [['preproc_id','subject_id']])
                                            
#outputdir = '/home/rschadmin/Data/ABIDE_SVC_output'
outputdir = '/data/Projects/ABIDE_Initiative/CPAC/abide/for_grant/SVC_output_dparsf'

#phenodir = '/home/rschadmin/Data/DOCs/'
phenodir = '/home2/data/Originals/ABIDE/Docs/Phenotypics_motion_scannerProtocols/PhenotypicDataForConsortiumUse/'
phenofiles = os.listdir(phenodir)
#motiondir = '/home2/data/Projets/ABIDE_Initiative'
motiondir = '/home2/data/Projects/ABIDE_Initiative/CPAC/Output_2013-11-22/pipeline_MerrittIsland'

motionfiles = glob.glob(os.path.join(motiondir+'/*/power_params/_scan_rest_1_rest/_threshold_0.2/*'))

subjects =  list(np.load('/data/Projects/ABIDE_Initiative/CPAC/abide/for_grant/abideSubjects_HC_12-19_mFD2_reviZed.npy'))
scans = ['1']
pipelines = pipelines = ['pipeline_RameyBorough','pipeline_MerrittIsland']
#ABIDE
preprocs = ['filt_globalW','filt_noglobalW','nofilt_globalW','nofilt_noglobalW']
#phenotype data
#ADHD = 'ScanDir ID'
#ABIDE = 'SubID'
phenotyped_subs = set()
motiontyped_subs = set()
pheno_dict = defaultdict(list)
for i, phenofile in enumerate(phenofiles):
    with open(os.path.join(phenodir,phenofile),'rU') as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            pheno_dict[row[0]]=row
            if phenofile == 'UM1_P2FRV.csv':#'Leuven2_P1.5.csv'
                pheno_dict[row[0]].append('')
                pheno_dict[row[0]].append('')
            #if phenofile == 'Leuven2_P1.5.csv':
                #pheno_dict[row[0]].append('')
            pheno_dict[row[0]].append(str(i))
            pheno_dict[row[0]].append(phenofile)
	    phenotyped_subs.add(str(row[0]))

for motionfile in motionfiles:
    with open(motionfile,'rU') as f:
        reader = csv.reader(f,delimiter=",")
        pheno_dict['Subject'] = reader.next()
        for row in reader:
            subject = row[0].split('_')[0].lstrip('0') #subject_id
            pheno_dict[subject].append(row[2])
            motiontyped_subs.add(str(subject))

meta_subs = phenotyped_subs & motiontyped_subs
