class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited=set()
        components=0

        def dfs(node:int)->bool:
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                components+=1
                dfs(node)
        
        return components

