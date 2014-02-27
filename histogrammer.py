import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()
import numpy as np
from variables import pheno_dict, meta_subs
from collections import defaultdict

#discrete labels
sex = 4
H = 5
site = 73
site_name = 74
dx = 1
#continuous labels
meanFD = 75
age = 3

phenoage = defaultdict(list)
phenoFD = defaultdict(list)

for subject in meta_subs:
    info = pheno_dict.get(subject)
    if not int(info[dx])==1: # only healthy controls
        phenoage[info[site_name].rstrip('.csv')].append(float(info[age])) #age dictionary
        phenoFD[info[site_name].rstrip('.csv')].append(float(info[meanFD])) #head motion dictionary

agebins = np.linspace(0,40,40)   

for x in phenostats.viewkeys():
    plt.hist(phenostats[x], agebins, alpha=0.3, label=x)

plt.show()
plt.legend(loc='upper right',fontsize='xx-small')
#plt.savefig('/home2/aimiwat/histogram.png')

#Stats
# 12-18 
# meanFD<0.2

# 557 healthy controls
# 282 in age range
# 429 in FD range
# 220 in both ranges


# age_in_range = np.multiply(age>11, age<19)
# final_list = healthy_subs[total_in_range] 
