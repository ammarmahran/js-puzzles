April 2022: Almost Magic
========================

[Link to Puzzle](https://www.janestreet.com/puzzles/almost-magic-index/ "April 2022: Almost Magic")

An Exercise in Linear Programming
---------------------------------

We can formulate this problem as a linear program and solve it with the LP solver of our choice (in my case: Gurobi).

Let *s~i, s~j* be the sums of two rows/columns/diagonals in an almost magic square.
The constraint *|s~i - s~j| <= 1* can be broken up into two constraints, *s~i - s~j <= 1* and *s~j - s~i <= 1*.

Modelling uniqueness of each value used is a little trickier, but the example provided let's us restrict the set of possible values to \{1,...,137\}.
We can then use dummy variables *z<sub>iv</sub>* := 1(square *i* assumes value *v*) for *i = 1, ..., 28* and *v = 1, ..., 137*.
Uniqueness now requires that for each *v*, the *z<sub>iv</sub>*'s add to at most 1 (summing over *i*).

Lastly, minimize the sum of values in the 28 squares and let the solver do the rest.

|  | 14 | 17 | 3 |  |  |
|  | 1 | 11 | 22 | 40 | 8 |
| 10 | 19 | 5 | 9 | 23 | 37 |
| 6 | 12 | 16 | 39 | 7 | 24 |
| 18 | 4 | 13 | 21 | 29 |  |
|  |  | 34 | 2 | 26 |  |
