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
To solve this, imagine you have n positions. n possible letters can come on the first position. on the second position  
n-1 letters can come. and so on. Following is the number of ways:  
![\Large (n)\times(n-1)....\times(1)](https://latex.codecogs.com/svg.latex?\Large&space;(n)\times(n-1)....\times(1))  
This is nothing but factorial(n)  
<br>
  

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

### Story Proofs
it is proof by interpretation, rather than algebra or Calculus.  
Lets proof following equality:  
![\Large \binom{n}{k}=\binom{n}{n-k}](https://latex.codecogs.com/svg.latex?\Large&space;\binom{n}{k}=\binom{n}{n-k})   

Suppose there are 10 players and you would like to form two teams - one having 6 members other having 4 members.  
There are n choose 6 ways you can make team one. Every time you are making team one, 4 left members will become part of team 2. So in this case answer is n choose 6
Now, lets flip the making of team.  
There are 4 ways you can make team 2. Every time you are making team 2, 6 left members will become part of team 1. So the answer is n chooose 4.  
This proves that:  
n choose 4 = n choose 6  
<br>
Let us prove another equality:  
![\Large n\times\binom{n-1}{k-1}=k\times\binom{n}{k}](https://latex.codecogs.com/svg.latex?\Large&space;n\times\binom{n-1}{k-1}=k\times\binom{n}{k})   
Let us say, there are n people and you want to make a club of k people with 1 person designated as president.  
One way to think about it is, first choose k people from n people. Now, each group, one of the member can be designated as president. So, that gives k possibilities for each group.
This is an application of multiplication rule.    
![\Large k\times\binom{n}{k}](https://latex.codecogs.com/svg.latex?\Large&space;k\times\binom{n}{k})  
  
  
The other way to solve this problem is to designate each one of the n person as president. Now, we are left with n-1 people and we have to choose k-1 people from n-1.  
Let us represent it mathematically:  
![\Large \sum_{1}^{n}\binom{n-1}{k-1}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{1}^{n}\binom{n-1}{k-1})  
Which is nothing but:  
![\Large n\times\binom{n-1}{k-1}](https://latex.codecogs.com/svg.latex?\Large&space;n\times\binom{n-1}{k-1})  
  
  
Let us story proof another equality:  
![\Large \binom{m+n}{k}=\sum_{0}^{k}\binom{m}{j}\times\binom{n}{k-j}](https://latex.codecogs.com/svg.latex?\Large&space;\binom{m+n}{k}=\sum_{0}^{k}\binom{m}{j}\times\binom{n}{k-j})  
let side of the equality is self annotating. It is like saying: choose k people from a group of m+n people.  
To understand, right side of the equality, let us assume two rooms having m and n people respectively in them.  
* Pick 0 from first room and k from second room. By application of multiplication rule, total number of ways is: n choose 0 multiplied by m choose k
* Pick 1 from first room and k-1 from second room. By application of multiplication rule, total number of ways is: n choose 1 multiplied by m choose k-1
* Pick j from first room and k-j from second room. By application of multiplication rule, total number of ways is: n choose  multiplied by m choose k-j
............................................................................................................................  
* Pick k from first room and 0 from second room. By application of multiplication rule, total number of ways is: n choose k multiplied by m choose 0

All the above have to be added since they are disjoint set. Adding them will give you right side of the equality.  


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
  





