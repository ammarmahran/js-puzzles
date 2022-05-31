January 2014: Sum of Squares
============================

[Link to Puzzle](https://www.janestreet.com/puzzles/sum-of-squares-index/ "Jan 2014: Sum of Squares")

Linear Programming
------------------

We use integer decision variables *0 <= d<sub>ij</sub> <= 9* representing the digits in all 25 cells.
The divisibility constraint can be modelled by introducing integer multipliers *m<sub>r</sub>* and requiring that the number in each row/column be such a multiple of the dividend.
Our LP solver finds the optimal solution (maximizing sum of *d<sub>ij</sub>*) almost instantly.

|  |  |  |  |  |
|---|---|---|---|---|
| 9 | 8 | 9 | 9 | 9 |
| 9 | 9 | 9 | 9 | 8 |
| 7 | 9 | 8 | 9 | 9 |
| 9 | 9 | 8 | 9 | 6 |
| 8 | 9 | 8 | 9 | 0 |

Heuristics
----------

- 10: last digit must be 0, no other restrictions.
- 1: last digit must be 9, no other restrictions.
- 2: last digit must be 8, no other restrictions.
- 3: last digit must be 9, other digits must sum to multiple of 3.
- 4: the last two digits should be 96 or 88, no other restrictions.
- 5: no restrictions (last digit fixed to 0).
- 6: last digit must be 8 (even), and digits must sum to multiple of 3 (suggesting a 7 somewhere).
- 7: 99999 is not divisible by 7, but 89999 is!
- 8: last three digits must be 888, no other restrictions.
- 9: 99999 is divisible by 9, and is compatible with other constraints.

With these observations we can derive the solution by hand.
