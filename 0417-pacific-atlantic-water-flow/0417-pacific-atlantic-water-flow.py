class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):

            visited.add((r, c))

            for dr, dc in directions:

                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # Pacific DFS
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        # Common cells
        result = []

        for cell in pacific:
            if cell in atlantic:
                result.append(list(cell))

        return result
        