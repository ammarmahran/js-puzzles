October 2021: Robot Swimming Trials
===================================

[Link to Puzzle](https://www.janestreet.com/puzzles/robot-swimming-trials-index/ "Oct 2021: Robot Swimming Trials")

Balls Into Baskets
------------------

For large *N*, the probability that at least one race is not chosen by any of the *3N* robots tends to one.
In this event, deviating from the discrete strategy by placing positive weight on each race (e.g. uniformly distributed) is profitable.

To compute the probability of this event, consider its complement:
Each race is chosen by at least one of the other robots.
This is akin to the situation of uniformly distributing *3N-1* balls into *N* baskets.
The probability of this is *p<sub>N</sub> = N! S<sub>2</sub>(3N-1,N) / N<sup>3N-1</sup>*, where *S<sub>2</sub>(m,n)* denotes the Stirling partition number, i.e. the number of ways a set of size *m* can be partitioned into *n* non-empty subsets.

By symmetry, the probability of reaching the finals if all robots play the same strategy is *1/3*.
We find the minimal *N* such that *1-p<sub>N</sub> > 1/3* to be *N=8* and the associated probability to be approximately *0.334578*.

Recursive Approach
------------------

Consider the event of hitting exactly *n* out of *N* baskets with *m* throws.
If the last throw hits a new target, we must have hit exactly *n-1* baskets with the first *m-1* throws.
If the last throw does not hit a new target, we have already hit *n* baskets with the first *m-1* throws.
Consequently, we can compute the probability of this event recursively via *p(m,n,N) = p(m-1,n,N) x n/N + p(m-1,n-1,N) x (N-n+1)/N* with the boundary conditions that this probability be zero if *m < n* or *n = 0*, and one if *m = n = 1*.
