graph = {
    1: [2, 3],
    2: [4],
    3: [2, 4],
    4: []
}


def  depth_first_search(visited_nodes, stack):
  while(len(stack) > 0):
    node = stack.pop()


    if node in visited_nodes:
      return
    
    print("node: ", node)
    visited_nodes.append(node)

    edges = graph[node]
    
    while (len(edges) > 0):
      stack.append(edges.pop())
  
    depth_first_search(visited_nodes, stack)
    

  


def main():
  depth_first_search([], [1])

main()