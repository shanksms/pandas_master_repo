# Important Probability concepts
## resources
[Harvard lectures playlist] (https://www.youtube.com/watch?v=KbB0FjPg0mw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo)


## Counting
### choose  without ordering
Imagine you have to choose k people out n. In this case order does not matter. Below formulae can be used:  
![\Large \binom{n}{k}](https://latex.codecogs.com/svg.latex?\Large&space;\binom{n}{k}) 
It is pronounced as n choose k
### Choose with ordering
![\Large \Perm{n}{k}=\frac{n!}{(n-k)!}](https://latex.codecogs.com/svg.latex?\Large&space;\Perm{n}{k}=\frac{n!}{(n-k)!}) 

\documentclass{article}
\usepackage{mathtools}

\newcommand\Myperm[2][^n]{\prescript{#1\mkern-2.5mu}{}P_{#2}}
\newcommand\Mycomb[2][^n]{\prescript{#1\mkern-0.5mu}{}C_{#2}}

\begin{document}

\[
\Myperm{k} = \frac{n!}{(n-k)!}\quad
\Mycomb{k} = \frac{n!}{k!(n-k)!}\quad
\Myperm[m]{k} = \frac{m!}{(m-k)!}\quad
\Mycomb[m]{k} = \frac{m!}{k!(m-k)!}\quad
\]

\end{document}

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



