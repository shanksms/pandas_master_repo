# Important Stats and Probability concepts
## resources
[Harvard lectures playlist] (https://www.youtube.com/watch?v=KbB0FjPg0mw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo)  
[Oreilly video course] (https://learning.oreilly.com/videos/mastering-probability-and/9781801075091/9781801075091-video3_5/)  
[Probability course] (https://www.probabilitycourse.com/)  
[Bayes Theorem Intuition] (https://www.youtube.com/watch?v=R13BD8qKeTg&t=67s)  
[latex template] (https://wjgan.com/posts/latex.html)

## Counting
### choose  without ordering
Imagine you have to choose p people out n. In this case order does not matter. Below formula can be used:  
![\Large \binom{n}{p}](https://latex.codecogs.com/svg.latex?\Large&space;\binom{n}{p})   
It is pronounced as n choose k. It is written as following as fractions:    
![\Large \frac{n!}{p!(n-p)!}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{n!}{p!(n-p)!}) 
### Choose with ordering
Imagine you have n letters and you have to arrange (permutate) p letters. In this case ordering does matter (AB is different from BA)      
![\Large \frac{n!}{(n-p)!}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{n!}{(n-p)!}) 

### General formulae for counting
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
* ............................................................................................................................  
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
  
### Non naive definition of probability.
A probability sample space consists of S and P where S is a sample space and P is a function which takes A as an event:  
![\Large {A}\subseteq{S}](https://latex.codecogs.com/svg.latex?\Large&space;{A}\subseteq{S})  
and  
P(A) = [0, 1] This means, P(A) can assume values between 0 and 1.  
There are two axioms:  
1. P(??) = 0 and P(S) = 1 where ?? represent empty set. it also means impossible event. S is full sample space.  
2.  Below is the second axiom:  
![\Large P(\cup_{n=1}^{N}A_{n})=\sum_{n=1}^{N}P(An)](https://latex.codecogs.com/svg.latex?\Large&space;P(\cup_{n=1}^{N}A_{n})=\sum_{n=1}^{N}P(A_{n})) if A1, A2.. are disjoint (non overlapping)  
Please note, N can also be ???  
in other words:  
P(A1???A2???A3???)=P(A1)+P(A2)+P(A3)+???  
Alternate notation:  
P(A???B)=P(A and B)=P(A,B)  
P(A???B)=P(A or B)  
### Finding Probabilities
Suppose that we are given a random experiment with a sample space S. To find the probability of an event,  
there are usually two steps: first, we use the specific information that we have about the random experiment. Second,  
we use the probability axioms. Let's look at an example. Although this is a simple example and you might be tempted to  
write the answer without following the steps, we encourage you to follow the steps.    
  

### Solved problems:
#### Presidential election
In a presidential election, there are four candidates. Call them A, B, C, and D. Based on our polling analysis,  
we estimate that A has a 20 percent chance of winning the election, while B has a 40 percent chance of winning. What is  
the probability that A or B win the election?  
P(A) = 0.2, P(B) = 0.4  
We have to find out P(A???B).   
Since P(A) and P(B) are disjoint events (only A or B can win the same election).
P(A???B) = P(A) + P(B) = 0.2 + 0.4 = 0.6  
#### Roll a die
You roll a fair die. What is the probability of E={1,5}?  
P(E) = 2/ 6 = 1 / 3  
Let us solve this using probability axiom. Since both events {1} and {5} are disjoint events.    
P({1???5}) = P({1}) ??? P({5}) =  1 / 6 + 1 / 6 = 2 / 3  
Please note, P(1) and P({1}) are used interchangeably. Although P({1})  is the correct notation.   

#### Using the axioms of probability, prove the following:
#####  For any event A, P(Ac)=1???P(A).
P(S) = 1  ( using axiom 1 )  
  
![\Large P({A}\cup{A}^c) = 1](https://latex.codecogs.com/svg.latex?\Large&space;P({A}\cup{A}^c)=1)     (By the definition of complement)    
![\Large P({A}) + P({A}^c) = 1](https://latex.codecogs.com/svg.latex?\Large&space;P({A})+P({A}^c)=1)    (By axiom#2)  
  

##### The probability of the empty set is zero, i.e., P(???)=0  
P(S) = 1  
P(S???S^c) = 1 (by definition of complement)  
P(S) + P(S^c) = 1  
P(S) +  P(???) = 1  
1 + P(???) = 1  
P(???) = 0  
  
##### For any event A, P(A)???1   
TBD
#####  P(A???B)=P(A)???P(A???B)
P(A???B)=P(A - (A???B))  (using Venn diagram)  
P(A???B)=P(A) - P(A???B) (axiom#2)  

##### P(A???B)=P(A)+P(B)???P(A???B), (inclusion-exclusion principle for n=2).
TBD
##### If A???B then P(A)???P(B)
TBD

##### Rain problem
Suppose we have the following information:

There is a 60 percent chance that it will rain today.
There is a 50 percent chance that it will rain tomorrow.
There is a 30 percent chance that it does not rain either day.  
  
Find the following probabilities:
###### The probability that it will rain today or tomorrow.
TBD
###### The probability that it will rain today and tomorrow.
TBD
###### The probability that it will rain today but not tomorrow.
TBD
###### The probability that it either will rain today or tomorrow, but not both.
TBD 

### inclusion-exclusion principle
#### With two events
![\Large P({A}\cup{B})=P(A)+P(B)-P({A}\cap{B})](https://latex.codecogs.com/svg.latex?\Large&space;P({A}\cup{B})=P(A)+P(B)-P({A}\cap{B}))  
#### With three events
![\Large P({A}\cup{B}\cup{C})=P(A)+P(B)+P(C)-P({A}\cap{B})-P({B}\cap{C})-P({A}\cap{C})+P({A}\cap{B}\cap{C})](https://latex.codecogs.com/svg.latex?\Large&space;P({A}\cup{B}\cup{C})=P(A)+P(B)+P(C)-P({A}\cap{B})-P({B}\cap{C})-P({A}\cap{C})+P({A}\cap{B}\cap{C}))  
#### General formula
![\Large P({A1}\cup{A2}....\cup{A}_{n})=\sum_{i=1}^{n}P({A}_{i})-\sum_{i<j}P({A}_{i}\cap{A}_{j})+\sum_{i<j<k}P({A}_{i}\cap{A}_{j}\cap{A}_{k})+(-1)^{n+1}P({A1}\cap{A2}....\cap{A}_{n})](https://latex.codecogs.com/svg.latex?\Large&space;P({A1}\cup{A2}....\cup{A}_{n})=\sum_{i=1}^{n}P({A}_{i})-\sum_{i<j}P({A}_{i}\cap{A}_{j})+\sum_{i<j<k}P({A}_{i}\cap{A}_{j}\cap{A}_{k})+(-1)^{n+1}P({A1}\cap{A2}....\cap{A}_{n}))  
        
### Matching problem (use of inclusion-exclusion principle)
Consider a deck of cards. Player starts pulling out cards one by one. He wins when the number written in the card is same as the sequence. Find the probability of his win.
e.g. if he pulls first Card having number one, he wins. If he pulls second card having number 2, he wins.  
Let say, A(i) is the event of pulling ith numbered card in the ith attempt. Essentially, we are trying to find out following:
    
**P(A1???A2....???An)**    
![\Large P({A}_{i})=\frac{(n-1)!}{n!}](https://latex.codecogs.com/svg.latex?\Large&space;P({A}_{i})=\frac{(n-1)!}{n!})  
There will be n such probabilities as you can choose any number from 1 to n.  

  
 

    


### Conditional probability
Essentially, conditional probability tries to solve problem, "How do you update probabilities of events once you have new information"  
I roll a fair die. Let A be the event that the outcome is an odd number, i.e., A={1,3,5}. Also let B be the event that the  
outcome is less than or equal to 3, i.e., B={1,2,3}. What is the probability of A, P(A)? What is the probability of A given B, P(A|B)?  
A = {1, 3, 5}  
B = {1, 2, 3}  
S = {1, 2, 3, 4, 5, 6}    
P(A) = |A| / |S|  = 3 / 6 = 1 / 2  

Now, let's find the conditional probability of A given that B occurred. If we know B has occurred, the outcome must be among {1,2,3}.  
For A to also happen the outcome must be in A???B={1,3}. Since all die rolls are equally likely, we argue that P(A|B) must be equal to  
P(A|B)=|A???B| / |B|=2 / 3  
Now, let us generalize the above statement:  
P(A|B) = ( |A???B| / |S| ) / (|B| / |S|)  
P(A|B) = P(A???B) / P(B)  when P(B) > 0  

Here is the intuition behind the formula: When we know that B has occurred, our sample space has reduced to B. Now, only way that A can occur when outcome belongs to set A ??? B.  
Therefore, We divide P(A???B) by P(B), so that the conditional probability of the new sample space becomes 1, i.e.,  
P(B|B)=P(B???B) / P(B)=1  

It is important to note that conditional probability itself is a probability measure, so it satisfies probability axioms. In particular,  

Axiom 1: For any event A, P(A|B)???0.  
Axiom 2: Conditional probability of B given B is 1, i.e., P(B|B)=1.  
Axiom 3: If A1,A2,A3,??? are disjoint events, then P(A1???A2???A3???|B)=P(A1|B)+P(A2|B)+P(A3|B)+???.  

#### solved problems on conditional probability
##### roll die
I roll a fair die twice and obtain two numbers X1= result of the first roll and X2= result of the second roll.  
Given that I know X1+X2=7, what is the probability that X1=4 or X2=4?  
S = {(11), (12), ......(66)}  (total 36)  
A = {(16), (25), (34), (43), (52), (61)}
C = {(14), (24), (34), (44), (54), (64), (41), (42), (43}, (45), (46))

P(A) = 6 / 36 = 1 / 6  
P(C) = 11 / 36  
P(C???A) =  2 / 36  
P(C | A) = P(C???A) / P(A) = 2 / 6 = 1 / 3    
#### Gambler's ruin
[detailed explanation] (https://www.youtube.com/watch?v=NB8atajijoc)


  

    
 
  



  
  





  







## Statistics

### Power sets
Suppose A={1, 2, 3} is a set. Its power sets is defined as all the possible sets which one can make from the elements of
set A.  
Total number of possible sets (including blank set) is 8 which 2**n.  
Possibly this is the reason it is called power sets.
### Set operations
1. Union
2. Intersection
3. Difference 
4. Complement. Complement is Universal Set minus A where A is a set inside the universal set.  

### Demorgan law
![\Large ({A}\cap{B})^{c}={A}^{c}\cup{B}^{c}](https://latex.codecogs.com/svg.latex?\Large&space;({A}\cap{B})^{c}={A}^{c}\cup{B}^{c})  
![\Large ({A}\cup{B})^{c}={A}^{c}\cap{B}^{c}](https://latex.codecogs.com/svg.latex?\Large&space;({A}\cup{B})^{c}={A}^{c}\cap{B}^{c})  

###  Distributive law
![\Large {A}\cap({B}\cup{C})=({A}\cap{B})\cup({A}\cap{C})](https://latex.codecogs.com/svg.latex?\Large&space;{A}\cap({B}\cup{C})=({A}\cap{B})\cup({A}\cap{C}))  
![\Large {A}\cup({B}\cap{C})=({A}\cup{B})\cap({A}\cup{C})](https://latex.codecogs.com/svg.latex?\Large&space;{A}\cup({B}\cap{C})=({A}\cup{B})\cap({A}\cup{C}))    

### Inclusion-Exclusion principle
The cardinality of a set (A) is denoted by |A|  
Following is inclusion and exclusion principle.  
![\Large |{A}\cup{B}|=|{A}| + |{B}| - |{A}\cap{B}|](https://latex.codecogs.com/svg.latex?\Large&space;|{A}\cup{B}|=|{A}|+|{B}|-|{A}\cap{B}|)  
<br>
![\Large |{A}\cup{B}\cup{C}|=|{A}| + |{B}| + |{C}|- |{A}\cap{B}| - |{A}\cap{C}| - |{B}\cap{C}| + |{A}\cap{B}\cap{C}|](https://latex.codecogs.com/svg.latex?\Large&space;|{A}\cup{B}\cup{C}|=|{A}|+|{B}|+|{C}|-|{A}\cap{B}|-|{A}\cap{C}|-|{B}\cap{C}|+|{A}\cap{B}\cap{C}|)    


### Random experiment
A random experiment is an experiment in which outcome is not known in advance.  
Toss of a fair coin may give: {H, T}  
An outcome is a result of a random experiment.  
When we repeat a random experiment several times, we call each one of them a trial. Thus, a trial is a particular  
performance of a random experiment. In the example of tossing a coin, each trial will result in either heads or tails.  
Note that the sample space is defined based on how you define your random experiment.  

#### Sample Space
Set of all outcomes is known as sample space.  
1. You toss a coin. In this experiment, sample space:  
S={H, T}
2. You toss two coins. In this experiment, sample space:
S = {HH, HT, TH, TT}  
To put it in word, when you toss a coin, you could get either of H or T. So sample space is {H, T}.  
3. You keep tossing a coin until you get H.  In this experiment, sample space could be:  
S = {H, TH, TTTTH, ....}. in this case cardinality of the set is infinite. It is not countable set.  

#### Event
Event is a subset of sample space.
Every subset if sample space is Event including empty set. In other words, Event is a member of Power set of the sample space.  
Let us take an experiment in which we roll two six sided fair dices.  
S = {(1, 1), (1, 2), (1, 3), .......(6, 6)}
Cardinality of S = |S| = 36 = 6 ^ 2  
This can be derived from multiplication rule. Assume, there are 6 roots, numbering 1 to 6. Now from each root, 6 branches numbering 1 to 6, can be taken out.  
number of roots are the possibilities i.e. 36  
 
Let us say you are interested in an event where sum of numbers on dice is an even number.  
E = {(1,1), (1, 3), (1, 5), (2, 2), (2, 4), (2, 6), (3, 1), (3, 3), (3, 5), (4, 2), (4, 4), (4, 6), (5, 1), (5, 3), (5, 5), (6, 2), (6, 4), (6, 6)}
Cardinality of E = |E| = 18  
This can, again, be derived from multiplication rule. 

#### Union and intersection
If A and B are events, then A???B and A???B are also events. By remembering the definition of union and intersection, we observe that A???B  
occurs if A or B occur. Similarly, A???B occurs if both A and B occur. Similarly, if A1,A2,???,An are events, then the event A1???A2???A3??????An occurs  
if at least one of A1,A2,???,An occurs. The event A1???A2???A3??????An occurs if all of A1,A2,???,An occur. It can be helpful to remember that the key words "or"  
and "at least" correspond to unions and the key words "and" and "all of" correspond to intersections.   

### Discreet random variable
it is random variable which can be counted. in other words DRV belongs a finite set.  
Suppose you throw two fair dice.  
S: Random variable which is the sum of numbers on the dices: 
Possible outcomes: {(1, 1), (1, 2).......(6, 6)} (total 36 possible events) 
| S  | P(S)   |  Favoured outcomes  |
|---|---|---|
| 2  | 1 / 36  | {(1,1)}  |
| 3  | 2 / 36  | {(1, 2), (2, 3)}  |
| 4  | 3 / 36  | {(1, 3), (2, 2), (3, 1)}   |
|  . |  .      |.  |  

Let us think about coin toss as an event:  
Define X as the random variable which is number of heads every time you toss the coin.    
X = 0,  P(X=0) = 1 / 2  
X = 1,  P(X=1) = 1 / 2  
A random variable which can only take two values, is called as Bernaulli's random variable.  
#### Geometric Random variable
you keep on tossing a  fair coin until you get a head.  
X: number of trials  
| X  | P(X)   |    |
|---|---|---|
| 1  | 1 / 2 | {(H)}  |
| 2  | (1 / 2)*(1 / 2)  | {(TH)}  |
| 3  |  (1 / 2)*(1 / 2)*(1 / 2)  | {(TTH)}   |
|  . |  .      |.  |    


Let us understand why we are multiplying the probabilities.  
for X = 2, we need T in the first toss and H in the second toss. Probability of T is 1 / 2. And Probability of H is 1 / 2   
since each coin toss is an independent event, We need to multiply the probabilities.  

We can show that:  
P(X=1)  + P(X=2) + P(X=3) + ....... = 1  
you can check the proof in the video.  

#### Binomial Random variable
you toss a fair coin n number of times.  
X: number of heads in n tosses.  
e.g. n = 3  
S = {HHH, HHT, HTT, HTH, THH, THT, TTH, TTT}  
This is a countable set as opposed to Geometric random variable example.  
![\Large P(X=0) = \frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}](https://latex.codecogs.com/svg.latex?\Large&space;P(X=0)=\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2})  
![\Large P(X=1) = 3\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}](https://latex.codecogs.com/svg.latex?\Large&space;P(X=1)=3\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2})  
We can generalize as below:  
![\Large P(X=k) = \binom{n}{k}\times\frac{1}{2}^{k}\times\frac{1}{2}^{n-k}](https://latex.codecogs.com/svg.latex?\Large&space;P(X=k)=\binom{n}{k}\times\frac{1}{2}^{k}\times\frac{1}{2}^{n-k})  
  
  
#### PMF and PDF
PMF - probability mass function is created for discreet random variable.  
PDF - probability density function is created for continuous random variable.


  








  















