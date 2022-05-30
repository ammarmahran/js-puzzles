#!/usr/bin/env python3.7

import gurobipy as gp

m = gp.Model()

# number of cells, bounds for values
N = 28
L = 1
U = 138

# Z[i,v] == 1 if cell i has value v
Z = m.addVars([(i,v) for i in range(N) for v in range(L,U)], vtype=gp.GRB.BINARY, name='z')

# V[i] = value of cell i
V = m.addVars([i for i in range(N)], vtype=gp.GRB.INTEGER, name='v')
m.addConstrs(V[i] == gp.quicksum(v * Z[i,v] for v in range(L,U)) for i in range(N))

# each cell assumes exactly one value
m.addConstrs(gp.quicksum(Z.select(i,'*')) == 1 for i in range(N))

# each value is taken by at most one cell
m.addConstrs(gp.quicksum(Z.select('*',v)) <= 1 for v in range(L,U))

# rows/cols/diags for each almost magic square
B1 = [[0,1,2],[3,4,5],[9,10,11],[0,3,9],[1,4,10],[2,5,11],[0,4,11],[2,4,9]]
B2 = [[5,6,7],[11,12,13],[17,18,19],[5,11,17],[6,12,18],[7,13,19],[5,12,19],[7,12,17]]
B3 = [[8,9,10],[14,15,16],[20,21,22],[8,14,20],[9,15,21],[10,16,22],[8,15,22],[10,15,20]]
B4 = [[16,17,18],[22,23,24],[25,26,27],[16,22,25],[17,23,26],[18,24,27],[16,23,27],[18,23,25]]
Bs = [B1,B2,B3,B4]

# add "almost-magic" constraints for each square
for B in Bs:
    for i in range(len(B)):
        for j in range(i):
            m.addConstr(gp.quicksum(V.select(B[i])) - gp.quicksum(V.select(B[j])) <= 1)
            m.addConstr(gp.quicksum(V.select(B[j])) - gp.quicksum(V.select(B[i])) <= 1)

# minimize sum of values
m.setObjective(gp.quicksum(V), gp.GRB.MINIMIZE)

m.optimize()

print(', '.join(str(var.x) for var in m.getVars() if 'v' in var.VarName))
print('Sum of Values: {}'.format(m.objVal))
