## important links

## Descriptive and inferential statistics
lorem ipsum
### Descriptive statistics

#### mean and weighed mean
mean is the average of set of values. he operation is simple to do: sum the values and divide by the number of values.  
The mean is useful because it shows where the “center of gravity” exists for an observed set of values.

```python
from math import fsum
# Number of pets each person owns
sample = [1, 3, 2, 5, 7, 0, 2, 3]

mean = fsum(sample) / len(sample)

print(mean) # prints 2.875
```
Following is how weighted mean is computed.  
```python
sample = [90, 80, 63, 87]
weights = [.20, .20, .20, .40]

weighted_mean = sum((s * w for s, w in zip(sample, weights)))/ sum(weights)
print(weighted_mean)
```
#### median
median is the middle most value in an ordered list of values. in case there are two center, we take the average of two numbers and   
call it median.
```python
sample = [0, 1, 5, 7, 9, 10, 14]

if len(sample) % 2 == 0:
    median = (sample[len(sample) // 2] + sample[len(sample) // 2 - 1]) / 2
else:
    median = sample[len(sample) // 2]

```
median can be a helpful alternative to the mean when data is skewed by outliers.
In 1986, the mean annual starting salary of geography graduates from the University of North Carolina at Chapel Hill was $250,000.
Other universities averaged $22,000. Wow, UNC-CH must have an amazing geography program!  

But in reality, what was so lucrative about UNC’s geography program? Well…Michael Jordan was one of their graduates. One  
of the most famous NBA players of all time indeed graduated with a geography degree from UNC. However, he started his career  
playing basketball, not studying maps. Obviously, this is a confounding variable that has created a huge outlier, and it majorly  
skewed the income average.  

When your median is very different from your mean, that means you have a skewed dataset with outliers.

#### mode
The mode is the most frequently occurring set of values. It primarily becomes useful when your data is repetitive and  
you want to find which values occur the most frequently.

When no value occurs more than once, there is no mode. When two values occur with an equal amount of frequency, then the  
dataset is considered bimodal. In Example 3-5 we calculate the mode for our pet dataset, and sure enough we see this is bimodal  
as both 2 and 3 occur the most (and equally) as often.  
```python
from collections import defaultdict

sample = [1, 3, 2, 5, 7, 0, 2, 3]

def mode(values):
    counts = defaultdict(lambda: 0)

    for s in values:
        counts[s] += 1

    max_count = max(counts.values())
    modes = [v for v in set(values) if counts[v] == max_count]
    return modes

print(mode(sample)) # [2, 3]
```

