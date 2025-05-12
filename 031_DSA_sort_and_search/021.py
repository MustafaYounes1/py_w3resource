"""

Write a Python program to sort a list of elements using Topological sort.

From Wikipedia: "In computer science, a topological sort or topological ordering of a directed graph is a linear
ordering of its vertices such that for every directed edge (u,v) from vertex u to vertex v, u comes before v in the
ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent
constraints that one task must be performed before another; in this application, a topological ordering is just a valid
sequence for the tasks"

Note: Topological Sorting for a graph is not possible if the graph is not a Directed Acyclic Graph (DAG); DAGs are a
special type of graphs in which each edge is directed such that no cycle exists in the graph.

    * Fails on undirected graphs: undirected edge between two vertices u and v means, there is an edge from u to v as
    well as from v to u. Because of this both the nodes u and v depend upon each other and none of them can appear
    before the other in the topological ordering without creating a contradiction.

    * Fails on cyclic graphs: All the vertices in a cycle are indirectly dependent on each other hence topological
    sorting fails.

Note: Topological order may not be Unique.

========
Approach
========
* Initialize a stack and a visited array of size n.

* For each unvisited vertex in the graph, do the following:
    * Apply DFS (Depth-First Search) on the vertex.
    * Mark the vertex as visited and recursively call DFS for all unvisited neighbors of the vertex.
    * Once all the neighbors have been visited, push the vertex onto the stack.

* After all, vertices have been visited, pop elements from the stack and append them to the output list until the stack
is empty.

* The resulting list is the topologically sorted order of the graph.

Time Complexity: O(V+E)
Auxiliary space: O(V)       (due to creation of the stack)

1. Model the nodes and edges of the graph presented in "021.png".
2. Find the topological sort of the nodes -> 5 4 2 3 1 0

"""

from collections import defaultdict, deque


def dfs(vertex: int, graph: dict[int, list[int]], stack: deque[int], visited: defaultdict[int, bool]) -> None:
    """Apply dfs to solve the topological sort problem
    @:param vertex: the input vertex to be processed
    @:param graph: the input graph where vertices are keys, and the value of each key is a list of adjacent vertices
    @:param stack: the output topological order
    @:param visited: a dict to indicate whether the vertex has been visited before"""

    # if the vertex has been visited before; its children are also visited -> do nothing
    if not visited[vertex]:
        visited[vertex] = True  # Mark the vertex as visited

        # apply dfs on all children
        for neighbor in graph[vertex]:
            dfs(neighbor, graph, stack, visited)

        # once done with children of the current vertex; push it onto the stack; so it would appear on the right,
        # i.e. all of its dependencies are resolved
        stack.appendleft(vertex)


def topological_sort(graph: dict[int, list[int]]) -> list[int]:
    """Find a topological order of a given graph modeled as a dict; vertices are keys, and values are lists of nodes
    that are adjacent to the key"""
    res, visited = deque(), defaultdict(lambda: False)

    for vertex in graph:
        dfs(vertex, graph, res, visited)

    return list(res)


def main():
    graph = {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1],
        5: [0, 2],
    }

    print(topological_sort(graph))


if __name__ == "__main__":
    main()
