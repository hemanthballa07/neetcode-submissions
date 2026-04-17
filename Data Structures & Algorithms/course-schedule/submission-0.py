class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        incoming = [0]*numCourses
        for u,v in prerequisites:
            incoming[u]+=1
            adj[v].append(u)
        queue = deque([i for i in range(numCourses) if incoming[i] ==0])
        topo_order = []
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for nei in adj[node]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    queue.append(nei)
        return len(topo_order) == numCourses
        
        

        