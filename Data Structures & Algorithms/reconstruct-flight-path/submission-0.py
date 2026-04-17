class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, des in tickets:
            adj[src].append(des)
        for src in adj:
            adj[src].sort(reverse=True)
        
        route = []
        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())

            route.append(airport)


        dfs("JFK")
        return(route[::-1])


        