#Tecent Competetion Answer:Version 2.0
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

prob = [random.random() for i in range(338489)]# all equals to 0.024875 average values
for i in range(338489):
   prob[i] = 0.024875

import csv    
with open('submission.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(instanceID, prob))

print('submission complete')

