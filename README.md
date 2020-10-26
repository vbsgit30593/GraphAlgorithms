# GraphAlgorithms
## Kosaraju useful data
https://www.youtube.com/watch?v=Rs6DXyWpWrI
* Can be used for find mother vertex
* We can find a mother vertex in O(V+E) time. The idea is based on Kosaraju’s Strongly Connected Component Algorithm. 
* In a graph of strongly connected components, mother vertices are always vertices of source component in component graph.
* If there exist mother vertex (or vertices), then one of the mother vertices is the last finished vertex in DFS. (Or a mother vertex has the maximum finish time in DFS traversal).
* A vertex is said to be finished in DFS if a recursive call for its DFS is over, i.e., all descendants of the vertex have been visited. 
