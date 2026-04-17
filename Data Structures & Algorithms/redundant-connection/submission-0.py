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
        if self.size[pu]>=self.size[pv]:
            self.size[pu]+=self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv]+=self.size[pu]
            self.parent[pu] = pv
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            nodes.add(u)
            nodes.add(v)

        dsu = UnionSet(len(nodes))
        for u,v in edges:
            if not dsu.union(u-1,v-1):
                return [u,v]


