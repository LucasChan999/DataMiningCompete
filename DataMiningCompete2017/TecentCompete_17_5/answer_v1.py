#Tecent Competetion Answer:Version 1.0
#lucas
#2017/5/10

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import random
from itertools import izip

instanceID = np.linspace(1,338489,338489)
instanceID = list(instanceID)
for i in range(338489):
   instanceID[i] = round(instanceID[i],0)
instanceID.insert(0,'instanceID')

prob = [random.random() for i in range(338489)]# 0~1 random default
for i in range(338489):
   prob[i] = round(prob[i],4)
prob.insert(0,'prob')

import csv    
with open('submission.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(instanceID, prob))

print 'sugmission complete'


#useless code bellow 
#import csv
#with open('submission.csv', 'w') as f:
# writer = csv.writer(f, delimiter='\t')
# writer.writerows(zip(instanceID,prob))

#app_clicked = zip(instanceID,prob)
#wf = open('submission.csv','w')
#wf.write('instanceID\vprob\n')
#for i in range(0,338489):   #去除第一行列名字
#    #item = app_clicked[i]
#    wf.writerow(app_clicked)