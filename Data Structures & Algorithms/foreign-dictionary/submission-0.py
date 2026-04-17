class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1)>len(w2):
                if w1[:minLen] == w2[:minLen]:
                    return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])

                    break
        color = [0]*26
        res = []
        def dfs(node):
            idx = ord(node)-ord('a')
            if color[idx] != 0:
                return color[idx] == 2
            color[idx] = 1
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            color[idx] = 2
            res.append(node)
            return True
        for c in adj:
            idx = ord(c) - ord('a')
            if color[idx] == 0:
                if not dfs(c):
                    return ""  # cycle found

        return "".join(reversed(res))
        
        