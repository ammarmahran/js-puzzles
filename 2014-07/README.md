July 2021: Chain Reaction
=========================

[Link to Puzzle](https://www.janestreet.com/puzzles/chain-reaction-index/ "Jul 2021: Chain Reaction")

Longest Path
------------

Consider the graph with nodes *\{1, ..., 100\}*, where *i ~ j* if *i* divides *j* or vice versa.
The problem of finding a longest integer sequence as described in the puzzle is then the same as finding a longest simple path in this graph.
There is no known efficient way of solving the longest path problems in general graphs (there is for DAGs, which this graph is not).
We can setup an LP formulation of the problem (e.g. Miller-Tucker-Zemlin) for fixed start and end points, *s* and *t*.
For a given pair of points, this takes only a few seconds to solve.
Alas, there is 4,950 of these pairs to consider, so this approach may take a few hours to run...

However, we can now be sure that lenght of a longest chain is 77.

Our solution: 52 -> 26 -> 13 -> 39 -> 78 -> 6 -> 36 -> 18 -> 54 -> 27 -> 81 -> 9 -> 63 -> 21 -> 42 -> 84 -> 28 -> 56 -> 14 -> 98 -> 49 -> 7 -> 77 -> 11 -> 99 -> 33 -> 66 -> 22 -> 44 -> 88 -> 8 -> 64 -> 32 -> 96 -> 16 -> 48 -> 24 -> 72 -> 12 -> 60 -> 30 -> 90 -> 45 -> 15 -> 75 -> 25 -> 50 -> 100 -> 20 -> 80 -> 40 -> 10 -> 70 -> 35 -> 1 -> 58 -> 29 -> 87 -> 3 -> 93 -> 31 -> 62 -> 2 -> 34 -> 68 -> 17 -> 85 -> 5 -> 95 -> 19 -> 38 -> 76 -> 4 -> 92 -> 46 -> 23 -> 69.
