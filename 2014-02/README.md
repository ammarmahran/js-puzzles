February 2014: Hooks
====================

[Link to Puzzle](https://www.janestreet.com/puzzles/hooks-index/ "Feb 2014: Hooks")

Solving by Hand
---------------

1. Row 2: Row sum of 42 &rarr; 3/5/6/7/8/9 must be present and then either 2,2 or 4.
2. Hook 5: Col sum of 5 &rarr; 4x 5 in row 5. Row sum of 42 &rarr; 6/7/9 present.
3. Row 6: Cannot have 6x 6 because of col 5 &rarr; need 7/8/9 present (sum divisible by 6). Thus either 4x or 5x 6 in col 6. Must have 5x 6 and 8/9 in col 6.
4. Row 7: Row sum of 29 &rarr; 3x 7 and 8. Col sum of 28 &rarr; 4x 7, rest of col blocked.
5. ...

From here it's straight-forward to fill up the remaining cells:

|  | 31 | 19 | 45 | 16 | 5 | 47 | 28 | 49 | 45 |
|---|---|---|---|---|---|---|---|---|---|
| 26 | 1 |  | 3 |  |  | 6 | 7 |  | 9 |
| 42 | 2 | 2 | 3 |  | 5 | 6 | 7 | 8 | 9 |
| 11 | 3 |  |  |  |  |  |  | 8 |  |
| 22 | 4 | 4 | 4 | 4 |  | 6 |  |  |  |
| 42 | 5 | 5 | 5 | 5 |  | 6 | 7 |  | 9 |
| 36 |  |  | 6 |  |  | 6 | 7 | 8 | 9 |
| 29 | 7 |  | 7 | 7 |  |  |  | 8 |  |
| 32 |  | 8 | 8 |  |  | 8 |  | 8 |  |
| 45 | 9 |  | 9 |  |  | 9 |  | 9 | 9 |

Solving as LP
-------------

Alternatively, we can formulate the problem as an LP. 
Let *z<sub>ij</sub>* = 1(cell *ij* is filled) be an indicator variable, and let *C<sub>k</sub>* be the set of cells belonging to hook *k*. 
The hook constraints then require that the sum of the *z<sub>ij</sub>* over the set *C<sub>k</sub>* equal *k*.
Similarly, the row and col sums constraint the sum (over *j* or *i*) of *z<sub>ij</sub> k<sub>ij</sub>*, where *k<sub>ij</sub>* = max(*i,j*) denotes the hook/digit to which cell *i,j* belongs.
