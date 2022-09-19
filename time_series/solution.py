import pandas as pd

data1 = [['19UUA56642A', 20071107, 40570],
         ['19UUA56642A', 20071113, 40000],
         ['19UUA56642A', 20100601, 49000],
         ['19UUA56642A', 20120529, 57000],
         ['19UUA56642A', 20140519, 60000],
         ['19UUA56642A', 20160523, 64000],
         ['19UUA56642A', 20180524, 68000],
         ['19UUA56642A', 20190321, 70124],
         ['19UUA56642A', 20200602, 73000],
         ['1A4GP45R26B', 20180521, 136032],
         ['1A4GP45R26B', 20180619, 136000],
         ['1A4GP45R26B', 20201021, 159000],
         ['1B4GP44362B', 20131125, 142045],
         ['1B4GP44362B', 20160719, 148000],
         ['1B4GP44362B', 20160727, 180000],
         ['1B4GP44362B', 20180730, 150000],
         ['1B4GP44362B', 20200730, 162000],
         ['1FADP3K20EL', 20150421, 17840],
         ['1FADP3K20EL', 20150904, 23222],
         ['1FADP3K20EL', 20160205, 29700],
         ['1FADP3K20EL', 20160617, 35070],
         ['1FADP3K20EL', 20170124, 44340],
         ['1FADP3K20EL', 20170728, 51825],
         ['1FADP3K20EL', 20180615, 63526],
         ['1FADP3K20EL', 20190307, 74449],
         ['1FADP3K20EL', 20190910, 81630],
         ['1FADP3K20EL', 20200722, 88818],
         ['1FADP3K20EL', 20201208, 91523],
         ['1FADP3K20EL', 20201223, 91522],
         ['1FADP3K20EL', 20210318, 91528],
         ['1FADP3K20EL', 20210429, 91535],
         ['1FAFP42X72F', 20020409, 69],
         ['1FAFP42X72F', 20040529, 2000],
         ['1FAFP42X72F', 20080505, 31000],
         ['1FAFP42X72F', 20100608, 4000],
         ['1FAFP42X72F', 20140624, 5000],
         ['1FAFP42X72F', 20160629, 7000],
         ['1FAHP3K20CL', 20190111, 138734],
         ['1FAHP3K20CL', 20190111, 139000],
         ['1FAHP3K20CL', 20210210, 46000],
         ['1FALP45T5RF', 20090805, 145000],
         ['1FALP45T5RF', 20090805, 145288],
         ['1FALP45T5RF', 20120201, 159000],
         ['1FALP45T5RF', 20140307, 153000],
         ['1FALP45T5RF', 20150721, 165106],
         ['1FALP45T5RF', 20160505, 165000],
         ['1FALP45T5RF', 20180502, 166000],
         ['1FMCU9EG1BK', 20161028, 82039],
         ['1FMCU9EG1BK', 20161105, 82000],
         ['1FMCU9EG1BK', 20190923, 138000],
         ['1FMCU9JX2EU', 20170428, 375280],
         ['1FMCU9JX2EU', 20170530, 37580],
         ['1FMCU9JX2EU', 20171206, 53401],
         ['1FMCU9JX2EU', 20190306, 82036],
         ['1FMEU63E98U', 20150604, 142140],
         ['1FMEU63E98U', 20150609, 143303],
         ['1FMEU63E98U', 20150914, 145285],
         ['1FMEU63E98U', 20151005, 145384],
         ['1FMEU63E98U', 20151006, 145395],
         ['1FMEU63E98U', 20151103, 146045],
         ['1FMEU63E98U', 20160218, 147974],
         ['1FMEU63E98U', 20160504, 149098],
         ['1FMEU63E98U', 20160819, 150625],
         ['1FMEU63E98U', 20161222, 152993],
         ['1FMEU63E98U', 20170515, 155984],
         ['1FMEU63E98U', 20180219, 162003],
         ['1FMEU63E98U', 20180522, 164000],
         ['1FMEU63E98U', 20180726, 165139],
         ['1FMEU63E98U', 20190221, 165200],
         ['1FMEU63E98U', 20190730, 174135],
         ['1FMEU63E98U', 20200121, 178593],
         ['1FMEU63E98U', 20200428, 181032],
         ['1FMEU63E98U', 20200609, 181000],
         ['1FMEU63E98U', 20200908, 184408],
         ['1FMEU63E98U', 20200915, 184594],
         ['1FMEU63E98U', 20210302, 188379],
         ['1FMZU73W55Z', 20170117, 74807],
         ['1FMZU73W55Z', 20170320, 76466],
         ['1FMZU73W55Z', 20171124, 83220],
         ['1FMZU73W55Z', 20171127, 83386],
         ['1FMZU73W55Z', 20171220, 83000],
         ['1FMZU73W55Z', 20180525, 89378],
         ['1FMZU73W55Z', 20181119, 94308],
         ['1FAFP52U93A', 20030912, 3],
         ['1FAFP52U93A', 20040714, 31487],
         ['1FAFP52U93A', 20050726, 28000],
         ['1FAFP52U93A', 20050726, 28968],
         ['1FAFP52U93A', 20111219, 107554],
         ['1FAFP52U93A', 20131228, 108792],
         ['1FAFP52U93A', 20191204, 101452],
         ['1FAFP52U93A', 20200508, 101457],
         ['1FAFP52U93A', 20200511, 101457],
         ['1FAFP34P63W', 20040504, 880],
         ['1FAFP34P63W', 20050914, 2000],
         ['1FAFP34P63W', 20070917, 53000],
         ['1FAFP34P63W', 20090902, 7000],
         ['1FAFP34P63W', 20110907, 9000],
         ['1FAFP34P63W', 20130917, 10000],
         ['1FAFP34P63W', 20151009, 88000],
         ['1FAFP34P63W', 20170814, 6000],
         ['1FAFP34P63W', 20190819, 13000],
         ['1FAFP34P63W', 20200831, 13868]]

pd.set_option('display.max_rows', None)

left = pd.DataFrame(data1, columns=['id', 'date', 'odo'])

data2 = [['1A4GP45R26B', 'GM'],
         ['1B4GP44362B', 'GM'],
         ['1C3EL55U71N', 'GM'],
         ['1D7KS28C77J', 'GM'],
         ['1FADP3E22DL', 'GM'],
         ['1FADP3K20EL', 'GM'],
         ['1FAFP42X72F', 'GM'],
         ['1FAHP3K20CL', 'GM'],
         ['1FALP45T5RF', 'GM'],
         ['1FMCU9EG1BK', 'Nissan'],
         ['1FMCU9JX2EU', 'Nissan'],
         ['1FMEU63E98U', 'Nissan'],
         ['1FMZU73W55Z', 'Nissan'],
         ['1FAFP52U93A', 'Nissan']];

right = pd.DataFrame(data2, columns=['id', 'make'])
# merging two tables
result = pd.merge(left, right, on='id', how='outer')
# drop records with 'odo' missing values
result.dropna(subset=['odo'], how='all', inplace=True)
'''
Anomaly detection
The IsolationForest ‘isolates’ observations by randomly selecting a feature and then randomly selecting a split value 
between the maximum and minimum values of the selected feature.
'''
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=float(0.15))
model.fit(result[['odo']])
result['scores'] = model.decision_function(result[['odo']])
result['anomaly'] = model.predict(result[['odo']])
# grouping by id
grouped = result.groupby("id")
for name, group in grouped:
    print(group)
