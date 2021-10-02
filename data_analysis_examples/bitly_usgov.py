import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
path = 'bitly_usgov_example.txt'
records = [json.loads(line) for line in open(path)]
#records is a list of dictionaries
frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()
print(tz_counts)
print('#' * 70)
clean_tz = frame['tz'].fillna('missing')
clean_tz[clean_tz == ''] = 'unknowns'
print(clean_tz.value_counts()[:10])
print('#' * 70)
subset = clean_tz.value_counts()[:10]
sns.barplot(y=subset.index, x = subset.values)
#plt.show()

# Lets find out browsers used to shorten the urls
print(frame['a'][1])
print(frame['a'][50])
print('#' * 70)

# it seems, if we split it by space and take 0th element, that will be browser type
browsers = pd.Series([x.split(' ')[0] for x in frame['a'].dropna()])
print(browsers.value_counts()[:5])
