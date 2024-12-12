class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Build the tree as an adjacency list
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Arrays to store results and subtree sizes
        res = [0] * n  # res[i] will be the sum of distances for node i
        count = [1] * n  # count[i] will be the size of the subtree rooted at node i
        
        # Step 3: First DFS to calculate the subtree sizes and res[0]
        def dfs1(node, parent):
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    count[node] += count[neighbor]  # Add the size of the child's subtree
                    res[node] += res[neighbor] + count[neighbor]  # Add the distance contributions

        # Step 4: Second DFS to calculate the result for all nodes
        def dfs2(node, parent):
            for neighbor in tree[node]:
                if neighbor != parent:
                    # Recompute the result for the neighbor based on the parent's result
                    res[neighbor] = res[node] - count[neighbor] + (n - count[neighbor])
                    dfs2(neighbor, node)
        
        # Start DFS from node 0
        dfs1(0, -1)
        dfs2(0, -1)
        
        return res
    
solution = Solution()
print(solution.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))