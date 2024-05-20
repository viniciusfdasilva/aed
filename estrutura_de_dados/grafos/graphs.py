import math

class Vertex():

    def __init__(self, vertexID):
        self.ID = vertexID
        
class VertexPair():

    def __init__(self, first_vertex: Vertex, second_vertex: Vertex):
        
        self.first_vertex  = first_vertex
        self.second_vertex = second_vertex

class Edge():

    def __init__(self, first_vertex: Vertex, second_vertex: Vertex):
        self.vertex_pair = VertexPair(first_vertex, second_vertex)

class Graph():

    def __init__(self, vertex_size: int, is_digraph=False, adjacency_flag=1):

        self.graph          = self.__init_graph(vertex_size)
        self.is_digraph     = is_digraph
        self.vertex_size    = vertex_size
        self.adjacency_flag = adjacency_flag

    def __vertex_in_graph(self, vertexID: int):
        return vertexID in range(0, self.vertex_size)

    def set_adjacency(self, edge: Edge, adjacency_flag=-1):

        if adjacency_flag == -1:
            adjacency_flag = self.adjacency_flag

        first_vertexID  = int(edge.vertex_pair.first_vertex.ID)
        second_vertexID = int(edge.vertex_pair.second_vertex.ID)

        if self.__vertex_in_graph(first_vertexID) and self.__vertex_in_graph(second_vertexID):
            
            self.graph[first_vertexID][second_vertexID]     = adjacency_flag
            
            if not self.is_digraph:
                self.graph[second_vertexID][first_vertexID] = adjacency_flag
        else:
            raise Exception('Vertex out of bounds')

    def __init_graph(self, vertex_size: int, inital_val=0):

        return [[inital_val]*vertex_size for _ in range(vertex_size)]
    
    def __mark_as_visited(self,visited, element, graph):
            for i in range(0, len(graph)):
                if graph[i][element] == self.adjacency_flag: 
                    graph[i][element] = visited
            return graph

    def clear(self, inital_val=0):
        self.graph = self.__init_graph(self.vertex_size, inital_val)

    def bfs(self, source_vertex: Vertex):
        

        assert self.is_digraph and self.__vertex_in_graph(int(source_vertex.ID))

        visited = self.adjacency_flag+1
        graph   = self.graph.copy()
        queque  = [source_vertex.ID]

        while len(queque) > 0:
            
            element = queque[0]
            queque  = queque[1:]

            print(f"Current vertex {element}")
            graph = self.__mark_as_visited(visited, element, graph)
            
            for i in range(0, len(graph[element])):
                if graph[element][i] == self.adjacency_flag:
                    print(f"    ({element}) -> ({i})")
                    graph = self.__mark_as_visited(visited, i, graph)
                    queque.append(i)
                elif graph[element][i] == visited:
                    print(f"    ({element}) -> ({i}) - Already visited")
    
    def get_parents(self, source_vertex, graph):
        assert self.__vertex_in_graph(source_vertex)
        parents = []
        
        for i in range(0, len(graph[source_vertex])):
            if self.graph[source_vertex][i] != 0:
                parents.append(i)
        return parents

    def dfs(self, source_vertex):
        
        graph   = self.graph
        visited = self.adjacency_flag+1

        parents_from_source = self.get_parents(source_vertex, graph)

        if len(parents_from_source) != 0:

            graph = self.__mark_as_visited(visited, source_vertex, graph)

            for i in range(0, len(parents_from_source)):

                if graph[source_vertex][i] != visited:
                    print(f"    ({source_vertex}) -> ({parents_from_source[i]})")
                    self.dfs(parents_from_source[i])
                    graph = self.__mark_as_visited(visited, i, graph)
                else:
                    print(f"    ({source_vertex}) -> ({parents_from_source[i]})")


    def dijkstra(self, source_vertex):
        assert self.is_digraph and self.__vertex_in_graph(int(source_vertex.ID))

        visited = math.inf
        graph   = self.graph.copy()
        queque  = [source_vertex.ID]
        visited = []
        weight  = [math.inf]*self.vertex_size

        weight[source_vertex.ID] = 0

        while len(queque) > 0:
            
            element = queque[0]
            queque  = queque[1:]

            print(f"Current vertex {element}")
            
            visited.append(element)
     
            for i in range(0, self.vertex_size):

                if graph[element][i] != -1 and i not in visited:

                    if weight[i] > (weight[element]+graph[element][i]):
                        
                        print(f"    ({element}) -> ({i}) <-> Weight {(weight[element]+graph[element][i])}")
                        weight[i] = (weight[element]+graph[element][i])
                        
                    visited.append(i)
                    queque.append(i)
                    
                elif graph[element][i] != -1 and i in visited:

                    print(f"    ({element}) -> ({i}) - Already visited", end=" <-> ")
                    
                    if weight[i] > (weight[element]+graph[element][i]):
                        print(f"New Weight {(weight[element]+graph[element][i])}")
                        weight[i] = (weight[element]+graph[element][i])
        
        return weight

    def show_matrix(self):
        for i in range(0, self.vertex_size):
            for j in range(0, self.vertex_size):
                print(f'{self.graph[i][j]}', end='')
            print('')
if __name__ == '__main__':

    vertex_size = 6

    graph = Graph(vertex_size, True)

    print('================================= BFS ====================================')
    graph.set_adjacency(Edge(Vertex(0),Vertex(2)))
    graph.set_adjacency(Edge(Vertex(0),Vertex(4)))
    graph.set_adjacency(Edge(Vertex(0),Vertex(3)))

    graph.set_adjacency(Edge(Vertex(1),Vertex(2)))
    graph.set_adjacency(Edge(Vertex(1),Vertex(4)))

    graph.set_adjacency(Edge(Vertex(2),Vertex(4)))

    graph.set_adjacency(Edge(Vertex(3),Vertex(4)))
    graph.set_adjacency(Edge(Vertex(3),Vertex(5)))

    graph.set_adjacency(Edge(Vertex(4),Vertex(5)))

    graph.set_adjacency(Edge(Vertex(5),Vertex(1)))
    graph.bfs(Vertex(0))

    print('==========================================================================')
    print('================================= DFS ====================================')
    graph.clear()

    graph.set_adjacency(Edge(Vertex(0),Vertex(2)))
    graph.set_adjacency(Edge(Vertex(0),Vertex(4)))
    graph.set_adjacency(Edge(Vertex(0),Vertex(3)))

    graph.set_adjacency(Edge(Vertex(2),Vertex(1)))
    graph.set_adjacency(Edge(Vertex(2),Vertex(4)))

    graph.set_adjacency(Edge(Vertex(3),Vertex(4)))
    graph.set_adjacency(Edge(Vertex(3),Vertex(5)))


    graph.set_adjacency(Edge(Vertex(4),Vertex(1)))
    graph.set_adjacency(Edge(Vertex(4),Vertex(5)))
    
    graph.set_adjacency(Edge(Vertex(5),Vertex(1)))
    
    graph.dfs(Vertex(0).ID)

    print('==========================================================================')
    print('============================== DIJKSTRA ==================================')

    graph.clear(inital_val=-1)

    graph.set_adjacency(Edge(Vertex(0),Vertex(2)), 7)
    graph.set_adjacency(Edge(Vertex(0),Vertex(4)), 4)
    graph.set_adjacency(Edge(Vertex(0),Vertex(3)), 2)

    graph.set_adjacency(Edge(Vertex(1),Vertex(2)), 0)
    
    graph.set_adjacency(Edge(Vertex(2),Vertex(4)), 1)

    graph.set_adjacency(Edge(Vertex(3),Vertex(4)), 1)
    graph.set_adjacency(Edge(Vertex(3),Vertex(5)), 3)

    graph.set_adjacency(Edge(Vertex(4),Vertex(1)), 4)
    graph.set_adjacency(Edge(Vertex(4),Vertex(5)), 1)

    graph.set_adjacency(Edge(Vertex(5),Vertex(1)), 2)

    print(graph.dijkstra(Vertex(0)))
    
    print('==========================================================================')
