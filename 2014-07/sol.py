#!/usr/bin/env python3.7

import gurobipy as gp

def longest_path(s,t,N=100):
    """longest s-t-path in graph"""
    m = gp.Model()
    m.Params.LogToConsole = 0

    V = [i+1 for i in range(N)]
    E = [(v,w) for v in V for w in V 
                if v != w and (v % w == 0 or w % v == 0)]
    
    Z = m.addVars(E, vtype=gp.GRB.BINARY, name='z')
    P = m.addVars(V, vtype=gp.GRB.INTEGER, name='p', lb=0)

    for v in V:
        b = (v==s) - (v==t)
        m.addConstr(gp.quicksum(Z.select('*',v)) + b == gp.quicksum(Z.select(v,'*')))
        m.addConstr(gp.quicksum(Z.select(v,'*')) <= 1)
        m.addConstr(gp.quicksum(Z.select('*',v)) <= 1)

    for v,w in E:
        if v==s or w==t:
            continue
        m.addConstr(P[w] >= P[v] + 1 + (N-1)*(Z[v,w]-1))

    m.setObjective(gp.quicksum(Z), gp.GRB.MAXIMIZE)
    m.optimize()

    return m

def format_path(m,s):
        path = [v.VarName for v in m.getVars() if 'z' in v.VarName and v.x > 0]
        tups = [x.replace('z[','').replace(']','').split(',') for x in path]
        succ = [list(map(int,x)) for x in tups]
        d = {v: w for v,w in succ}
        res = f'{s}'
        while s in d:
            res += f' -> {d[s]}'
            s = d[s]

        return res

if __name__ == '__main__':
    # 52 ... 69 achieves max length
    P = longest_path(52,69)
    print(format_path(P,52))
