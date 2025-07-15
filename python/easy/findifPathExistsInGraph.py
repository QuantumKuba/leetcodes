from typing import List
import collections

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Store all edges in 'graph'.
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # store all the nodes to be visited in 'queue'
        seen = [False] * n
        # set source as seen
        seen[source] = True
        # add source to the queue
        queue = collections.deque([source])

        while queue:
            # pop the first element
            curr_node = queue.popleft()
            if curr_node == destination:
                return True

            # For all the neighors of the current node, if we haven't visited it before
            # add it to 'queue' and mark it as visited.
            for neighbour in graph[curr_node]:
                print(graph[curr_node])
                if not seen[neighbour]:
                    seen[neighbour] = True
                    queue.append(neighbour)

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))  # Example usage
    
    print(s.validPath(6, [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5]], 0, 5))  # Example usage
    print(s.validPath(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 0, 4))  # Example usage