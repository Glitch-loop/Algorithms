
class Dijkstra(object): 
  def shortest_path(self, graph, source):
    # Creating sets needed for the alghoritm
    dist = [float("inf")] * len(graph)
    sptSet = [0] * len(graph)

    # Initilizing data structure
    dist[source] = 0
    sptSet[source] = 1

    self.dijkstra(graph, dist, sptSet, source)
    print(dist)
    print(sptSet)


  def dijkstra(self, graph, dist, sptSet, CN):
    sptSet[CN] = 1 # Marking node was visited

    # Retriving the edges of the node
    for i in range(len(graph[CN])):
      if graph[CN][i] > 0:
        # There is an edge between the nodes
          """
            What is happening?
            1. It is being added the distance that has the current node so far (having its origin in 
            the original source) plus the wieght of the current edge of the current node. 
          """
          distance_edge =  dist[CN] + graph[CN][i]
          
          if distance_edge < dist[i]:
            """
            2. The result is compared with the previous distance stored in dist.
            It could be interpreted as: The current distance is lower than the stored distance
            for the node?
            """
            dist[i] = distance_edge
        
    node_to_visit = None
    # Visting the edges of the node (BFS)
    for i in range(len(dist)):
      if sptSet[i] == 1:
        # Node already visited
        continue
      else:
        if node_to_visit == None:
          # There is still not node chosen.
          node_to_visit = i
        else:
          if dist[i] <= dist[node_to_visit]:
            # Taking the node with lesser distance
            node_to_visit = i

    # If it is none, that means that there is not other node to visit.
    if node_to_visit != None:
      self.dijkstra(graph, dist, sptSet, node_to_visit)



def main():
  dijkstra = Dijkstra()
  graph = [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ],
            [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ],
            [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ],
            [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ],
            [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ],
            [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ],
            [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ],
            [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ],
            [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] ]

  dijkstra.shortest_path(graph, 0)


main()