class Solution:
    def cloneGraph(self, node):

        if not node:
            return None

        clones = {}

        def dfs(node):

            # Already cloned
            if node in clones:
                return clones[node]

            # Create clone
            copy = Node(node.val)
            clones[node] = copy

            # Clone neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)

        