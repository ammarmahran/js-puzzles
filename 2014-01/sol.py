#!/usr/bin/env python3.7

import gurobipy as gp

m = gp.Model()

# digit in cell i
D = m.addVars([(i,j) for i in range(5) for j in range(5)], vtype=gp.GRB.INTEGER, name='d', lb=0, ub=9)

# multiplier
M = m.addVars(range(10), vtype=gp.GRB.INTEGER, name='m')

# divisors
Z = [i for i in range(1,11)]

# row constraints
m.addConstrs(gp.quicksum(10**(4-j) * D[i,j] for j in range(5)) - M[i] * Z[i] == 0 for i in range(5))

# col constraints
m.addConstrs(gp.quicksum(10**(4-i) * D[i,j] for i in range(5)) - M[j+5] * Z[j+5] == 0 for j in range(5))

# feasible solution
m.setObjective(gp.quicksum(D), gp.GRB.MAXIMIZE)

m.optimize()

for i in range(5):
    print(''.join(str(int(D[i,j].x)) for j in range(5)))
