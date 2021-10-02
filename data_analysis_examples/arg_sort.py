import pandas as pd
#creating Series
s_1= pd.Series([2,1,4,3])
print(s_1)
print(s_1.argsort())
print(s_1[s_1.argsort()])