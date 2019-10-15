import csv
import pandas as pd
import numpy as np

"""
    left_outer_join(file_a, 1, file_b, 3) -->
    a,1,q,j,p,4,1
    b,3,7,NULL,NULL,NULL,NULL
    c,2,t,a,d,g,2
"""

file_a = pd.read_csv('file_a.txt', header=None)
file_b = pd.read_csv('file_b.txt', header=None)

print(file_b)
print(file_a)

left_join = pd.merge(file_a, file_b, how='left', suffixes=('_fa', '_fb'), left_on=1, right_on=3)
left_join = left_join.replace(np.nan, 'NULL')

print(left_join.to_string())
