class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming = [0]*numCourses
        adj = defaultdict(list)
        for v,u in prerequisites:
            incoming[v]+=1
            adj[u].append(v)
        q = deque([i for i in range(numCourses) if incoming[i] == 0])
        topo_order = []
        while q:
            node = q.popleft()
            topo_order.append(node)
            for nei in adj[node]:
                incoming[nei]-=1
                if incoming[nei] == 0:
                    q.append(nei)
        return topo_order if len(topo_order) == numCourses else []
        