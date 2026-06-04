class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: create graph nodes for every unique character
        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for ch in word:
                indegree[ch] = 0

        # Step 2: compare adjacent words to build ordering rules
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))

            # Invalid prefix case: "abc" before "ab"
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    parent = word1[j]
                    child = word2[j]

                    # Add edge only once
                    if child not in graph[parent]:
                        graph[parent].add(child)
                        indegree[child] += 1

                    break

        # Step 3: start with letters having 0 prerequisites
        queue = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)

        result = []

        # Step 4: BFS topological sort
        while queue:
            ch = queue.popleft()
            result.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        # Step 5: if result does not include all letters, cycle exists
        if len(result) != len(indegree):
            return ""

        return "".join(result)