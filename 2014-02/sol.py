#!/usr/bin/env python3.7

import gurobipy as gp

m = gp.Model()

# digits
D = range(1,10)

# Z[i,j] == 1 if cell ij is active
Z = m.addVars([(i,j) for i in D for j in D], vtype=gp.GRB.BINARY, name='z')

# hook constraints
for k in D:
    m.addConstr(gp.quicksum(Z[i,k] for i in range(1,k)) +
        Z[k,k] + gp.quicksum(Z[k,j] for j in range(1,k)) == k)

# row constraints
R = [26,42,11,22,42,36,29,32,45]
m.addConstrs(gp.quicksum(max(i,j) * Z[i,j] for j in D) == R[i-1] for i in D)

# col constraints
C = [31,19,45,16,5,47,28,49,45]
m.addConstrs(gp.quicksum(max(i,j) * Z[i,j] for i in D) == C[j-1] for j in D)

# feasible solution
m.setObjective(1)

m.optimize()

for i in D:
    print(''.join(str(max(i,j)) if Z[i,j].x > 0 else " " for j in D))
