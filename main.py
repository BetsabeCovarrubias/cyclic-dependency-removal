class Graph:
    def __init__(self, vCount, list = None):
        self.V = vCount
        self.graph = list if list is not None else [[] for _ in range(vCount)]

    def is_Cyclic_Depen(self, vertex, visited, theeStack, inCycle):
        visited[vertex] = True
        theeStack[vertex] = True
        #print(f"theeStack[{vertex}] set to True")

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                if self.is_Cyclic_Depen(neighbor, visited, theeStack, inCycle):
                    inCycle[vertex] = True
                    return True
            elif theeStack[neighbor]:
                inCycle[vertex] = True
                return True
        
        theeStack[vertex] = False
        #print(f"theeStack[{vertex}] set to False (backtracking)")
        return False

    def number_satisfiable_nodes(self):
        visited = [False] * self.V
        theeStack = [False] * self.V
        inCycle = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.is_Cyclic_Depen(i, visited, theeStack, inCycle)

        count = 0;
        for i in range(self.V):
            if not inCycle[i]:
                count += 1

        #for i in range(self.V):
            #print(theeStack[i])

        return count

if __name__ == "__main__":
    #number of vertices
    n = int(input().strip())
    #number of edges
    m = int(input().strip())

    #create a graph with n vertices
    graph_List = {node: [] for node in range(n)}
    #iterate to get the m edges in the dictionary
    for _ in range(m):
        src, dst = (int(x) for x in input().strip().split())
        graph_List[src].append(dst)
        #print(src)
        #print(dst)
    
    g = Graph(n, graph_List)

    print(g.number_satisfiable_nodes())
