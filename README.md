# pandas-homework
These are the results of the executed codes:

/usr/local/bin/python3.7 /Users/thiorofaty/Dev/pandas-homework/pandas-exercises2.py
Index(['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'], dtype='object')
RangeIndex(start=0, stop=1338, step=1)
age           int64
sex          object
bmi         float64
children      int64
smoker       object
region       object
charges     float64
dtype: object
(1338, 7)

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 7 columns):

age         1338 non-null int64
sex         1338 non-null object
bmi         1338 non-null float64
children    1338 non-null int64
smoker      1338 non-null object
region      1338 non-null object
charges     1338 non-null float64
dtypes: float64(2), int64(2), object(3)
memory usage: 73.3+ KB
None
      
      
       age          bmi     children       charges
count  1338.000000  1338.000000  1338.000000   1338.000000
mean     39.207025    30.663397     1.094918  13270.422265
std      14.049960     6.098187     1.205493  12110.011237
min      18.000000    15.960000     0.000000   1121.873900
25%      27.000000    26.296250     0.000000   4740.287150
50%      39.000000    30.400000     1.000000   9382.033000
75%      51.000000    34.693750     2.000000  16639.912515
max      64.000000    53.130000     5.000000  63770.428010
0       19
1       18
2       28
3       33
4       32
        ..
1333    50
1334    18
1335    18
1336    21
1337    61


Name: age, Length: 1338, dtype: int64
      age  children      charges
0      19         0  16884.92400
1      18         1   1725.55230
2      28         3   4449.46200
3      33         0  21984.47061
4      32         0   3866.85520
...   ...       ...          ...
1333   50         3  10600.54830
1334   18         0   2205.98080
1335   18         0   1629.83350
1336   21         0   2007.94500
1337   61         0  29141.36030

[1338 rows x 3 columns]
   age  children      charges
0   19         0  16884.92400
1   18         1   1725.55230
2   28         3   4449.46200
3   33         0  21984.47061
4   32         0   3866.85520
Average: 13270.422265141257
Minimum: 1121.8739
Maximum: 63770.42801
    age     sex smoker
16   52  female     no
     age
543   54
           age
region        
northeast  324
northwest  325
southeast  364
southwest  325
1338
               age       bmi  children   charges
age       1.000000  0.109272  0.042469  0.299008
bmi       0.109272  1.000000  0.012759  0.198341
children  0.042469  0.012759  1.000000  0.067998
charges   0.299008  0.198341  0.067998  1.000000

Process finished with exit code 0
