import pandas as pd
data = {'state':['ohio','ohio','ohio','nevada','nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = pd.DataFrame(data, columns=['year','state','pop'],index=['1','2','3','4','5'])
#print frame
#print frame.ix['1']
frame['nima']=range(5)
print frame.T