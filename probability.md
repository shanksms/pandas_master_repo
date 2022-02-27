# Important Probability concepts
## resources
[Harvard lectures playlist] (https://www.youtube.com/watch?v=KbB0FjPg0mw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo)


## Counting
### choose  without ordering
Imagine you have to choose p people out n. In this case order does not matter. Below formula can be used:  
![\Large \binom{n}{p}](https://latex.codecogs.com/svg.latex?\Large&space;\binom{n}{p})   
It is pronounced as n choose k. It is written as following as fractions:    
![\Large \frac{n!}{p!(n-p)!}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{n!}{p!(n-p)!}) 
### Choose with ordering
Imagine you have n letters and you have to choose k letter. In this case ordering does matter (AB is different from BA)      
![\Large \frac{n!}{(n-p)!}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{n!}{(n-p)!}) 

### replacement and ordering
Lets say we have n objects and we have to choose p:  
#### with replacement, order matters:  
![\Large n^{k}](https://latex.codecogs.com/svg.latex?\Large&space;n^{p})  
#### without replacement, order matters:  
![\Large \frac{n!}{(n-p)!}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{n!}{(n-p)!}) 
#### without replacement, order does not matter:  
![\Large \frac{n!}{p!(n-p)!}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{n!}{p!(n-p)!})  
#### with replacement, order does not matter:  
![\Large \binom{n+k-1}{k}](https://latex.codecogs.com/svg.latex?\Large&space;\binom{n+k-1}{k})   

### Arrange letters
Suppose you have n letters. How many ways you can arrange them?  
To solve this, imagine you have n positions. there n possible letters can come on the first position. on the second position  
n-1 letters can come. and so on. Following is the number of ways:  
![\Large (n)\times(n-1)....\times(1)](https://latex.codecogs.com/svg.latex?\Large&space;(n)\times(n-1)....\times(1))  
This is nothing by factorial(n)
  

## Probability
### Sample space
A sample space is the set of all possible outcomes of an experiments
### Event
An event is a subset of a sample space

### Naive definition of Probability
P(A) = # favorable outcomes / # positive outcomes
P(A) - is the probability of event A which is favorable outcomes  
Assumptions:  
1. All the outcomes are equally likely  
2. Finite sample space  

Remember that you need strong justification to use naive definition of probability.

### Birthday problem
Given a group of k people, find out probability of two people sharing birthday. exclude leap year from the sample space.  
We will apply naive probability definition. In this is case it is easier to compute the complement.  
So, now problem is to find out probability of two people not sharing birthday.  
Going by the definition, in this case:    
#### count of positive outcomes:
![\Large 365^{k}](https://latex.codecogs.com/svg.latex?\Large&space;365^{k})  
Let us take example of k=2. So, first person can have birthday as any of the 365 days. Lets imagine a tree with 365 root nodes.  
These 365 root nodes are the possibilities of birthday of first person. Second person can also have birthday as any of the 365 days.  
Therefore, there will be 365 branches springing out from each of the 365 root nodes. 
#### count of favourable outcomes:       
![\Large \sum_{1}^{365}365](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{1}^{365}365)  
#### Which is nothing but:   
![\Large 365^{2}](https://latex.codecogs.com/svg.latex?\Large&space;365^{2})  

Now let us figure out count of favorable outcomes. It should be equal to:  
![\Large \frac{n!}{(n-k)!}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{n!}{(n-k)!})  

This case is exactly similar to the case "without replacement, order matters"  
There is one more way to think about this. out of k persons, first person can  have his birthday on one of 365 days,  
second can have his birthday on one of 364 days. and so on  
number of favorable outcomes = A^c  
![\Large A^c = 365\times364\times....\times(365-k+1)](https://latex.codecogs.com/svg.latex?\Large&space;A^c=365\times364\times....\times(365-k+1))

It is equivalent to:  
![\Large \frac{n!}{(n-k)!}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{n!}{(n-k)!})
    
Putting all of above together:  
![\Large P(A) = 1 - \frac{365\times\364\times....\times(365-k+1)}{365^{k}}](https://latex.codecogs.com/svg.latex?\Large&space;P(A)=1-\frac{365\times\364\times...\times(365-k+1)}{365^{k}})
  





