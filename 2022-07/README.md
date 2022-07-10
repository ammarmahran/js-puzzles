July 2022: Andy's Morning Stroll
================================

Random Walk on a Soccer Ball
----------------------------

The soccer ball has 20 white hexagonal panels.
The underlying graph is 3-regular and it turns out that all nodes of the same distance to the origin are in a sense equivalent;
i.e. we can reduce the complexity of the problem from one with 20 distinct nodes to one with only 6 distinct nodes (with distance 0, 1, ..., 5 to the origin).

The expected times to absorption of the underlying Markov process are then readily computed for each state, and we find that it takes on average 20 steps for the ant to return to the origin.

Random Walk on a Hex Grid
-------------------------

Alas, the flat kitchen floor, though eerily similar to the surface of the ball, does not have the same nice property.
For a distance of 3, we can already see that tiles are not characterized by their distance to the origin alone: some of them have two neighbours with a distance of 2, others have two neighbours with a distance of 4.
This complicates things a little, but we can still exploit some symmetries to reduce the complexity of the problem.

For example, rotation by 120 degrees leaves the layout unchanged, reducing the number of distinct tiles to (roughly) a third.
There are more symmetries that could be exploited, but this already makes the problem tractable.

The question asks for the probability that a random walk on the floor takes more than 20 steps before the ant returns to the origin.
In other words, we are interested in where the ant is after 20 steps (assuming that it stays at the origin once it gets there).
This is another classical Markov chain problem!

In the transition matrix, the origin is an absorbing state.
Moreover, we can turn every tile with a distance of 11 to the origin into an absorbing state, too:
If the ant reaches such a tile, it will not make it back to the origin in 20 steps, allowing us to reduce the complexity further. 

Lastly, we need to identify the different kind of tiles that are up to a distance of 11 away from the origin.
[This Post](https://www.redblobgames.com/grids/hexagons/ "Hexagonal Grids") on hexagonal grids proved immensely helpful for this.

With this, we set up our transition matrix and compute the state distribution after 20 steps (starting from a degenerate distribution after the first step).
The probability of the ant being at the origin is about 0.55, meaning that it takes it more than 20 steps with probability 0.45 (0.4480326).
