class UnionSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,u,v):
        pu,pv = self.find(u),self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        elif self.size[pu] > self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        return True
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        un = UnionSet(n)
        res = n
        for u,v in edges:
            if un.union(u,v):
                res-=1
        return(res)

        