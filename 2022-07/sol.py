import numpy as np

def e_soccer():
    """
    expected time to reach original tile on soccer ball
    = 20
    """
    E = np.identity(6)
    E[0,1] = E[5,4] = -1
    E[2,1] = E[2,3] = E[3,2] = E[3,4] = E[4,5] = -1/3 # not E[1,0] !
    E[1,2] = E[4,3] = -2/3
    E[2,2] = E[3,3] = 2/3

    B = np.ones(6)

    return np.linalg.solve(E,B)[0]

class Hex:
    def __init__(self, x, y, z, d=None):
        self.x = x
        self.y = y
        self.z = z
        self.d = d

        self.r = max(self.x, self.y, self.z)

    def __str__(self):
        return str((self.pos(), self.d))
    
    def __repr__(self):
        return self.__str__()

    def pos(self):
        return (self.x, self.y, self.z)

    def rotate(self):
        return Hex(self.z, self.x, self.y, self.d)

    def blocked(self):
        return (self.z-self.y) % 3 == 1

    def neighbours(self):
        x, y, z = self.pos()
        d = self.d + 1

        N = [Hex(x, y-1, z+1, d),
             Hex(x, y+1, z-1, d),
             Hex(x+1, y, z-1, d),
             Hex(x-1, y, z+1, d),
             Hex(x-1, y+1, z, d),
             Hex(x+1, y-1, z, d)]

        self.N = [n.rep() for n in N if not n.blocked()]
        return self.N

    def rep(self):
        h = self
        while h.x != h.r:
            h = h.rotate()

        return h

def find_tiles(D=11):
    """
    find tiles up to a distance of D away from origin
    """
    O = Hex(0,0,0,0)
    G = {}
    Q = [O]

    while Q:
        c = Q.pop(0)
        
        if c.pos() in G or c.d == D+1:
            continue

        Q += c.neighbours()
        G[c.pos()] = c

    return G

def p_kitchen(D=11):
    """
    probability of taking more than 20 steps to reach original tile

    compute distribution after 20 steps starting from O (i.e. 19 steps from 1-tile)
    """
    G = find_tiles(D)
    T = list(G.keys())
    n = len(T)
    P = np.zeros((n,n))

    idx0 = T.index((0,0,0))
    idx1 = T.index((1,0,-1))

    for i in range(n):
        c = G[T[i]]
        
        # (artificial) absorbing states
        if i == idx0 or c.d == D:
            P[i,i] = 1
            continue

        # each neighbour visitied with same probability
        for x in c.N:
            P[i, T.index(x.pos())] += 1/3

    # initial distribution: start at 1-tile
    d1 = np.zeros(n)
    d1[idx1] = 1

    d20 = d1 @ np.linalg.matrix_power(P,19)

    return d20[idx0]

if __name__ == '__main__':
    E = e_soccer()
    P = p_kitchen()
    print(f'Expected time to return to origin on ball = {E:.0f}')
    print(f'Probability of being at origin after 20 steps = {P}.')

    print(f'Solution: {1-P:.7f}')
