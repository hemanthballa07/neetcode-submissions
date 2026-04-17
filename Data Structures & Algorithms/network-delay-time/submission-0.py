class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        
        distance = {i:float('inf') for i in range(1,n+1)}
        distance[k] = 0
        pq = [(0,k)]
        while pq:
            dist,node = heapq.heappop(pq)
            if dist > distance[node]:
                continue
            for nei,d in adj[node]:
                total_dist = d + dist
                if total_dist < distance[nei]:
                    distance[nei] = total_dist
                    heapq.heappush(pq,(total_dist,nei))
        ans = max(distance.values())
        return ans if ans != float('inf') else -1

        