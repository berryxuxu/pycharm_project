import json
from collections import Counter
from pandas import DataFrame, Series
import pandas as pd
import numpy as np


fileh= open('c:\python27\pydata\ch02\usagov.txt','r')
records = [json.loads(line) for line in fileh]
time_zones = [ rec['tz'] for rec in records if 'tz' in rec]
#print time_zone
dic = {}
for i in time_zones:
    dic[i] = dic.get(i,0)+1
#print dic
counts = Counter(time_zones)
tp10 = counts.most_common(10)

#print tp10
frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
#print tz_counts
#print clean_tz
clean_tz[clean_tz == ''] = 'Unknow'
tz_counts = clean_tz.value_counts()
# print tz_counts[:10]
#tz_counts[:10].plot(kind='barh',stacked = True)