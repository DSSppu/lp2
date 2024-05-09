import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent  
        self.g = g 
        self.h = h   

    def f(self):
        return self.g + self.h

class AStar:
    def __init__(self, start_state, goal_state, neighbors_func, heuristic_func):
        self.start_node = Node(start_state)
        self.goal_node = Node(goal_state)
        self.neighbors_func = neighbors_func
        self.heuristic_func = heuristic_func

    def search(self):
        open_set = []   
        closed_set = set()   

       
        heapq.heappush(open_set, (self.start_node.f(), id(self.start_node), self.start_node))

        while open_set:
            _, _, current_node = heapq.heappop(open_set)

             
            if current_node.state == self.goal_node.state:
                return self._reconstruct_path(current_node)

            closed_set.add(current_node.state)

             
            for neighbor_state in self.neighbors_func(current_node.state):
                if neighbor_state in closed_set:
                    continue
                
                
                tentative_g = current_node.g + 1   

                
                neighbor_node = None
                for _, _, node in open_set:
                    if node.state == neighbor_state:
                        neighbor_node = node
                        break

                if neighbor_node is None or tentative_g < neighbor_node.g:
                    neighbor_node = Node(neighbor_state, parent=current_node, g=tentative_g, h=self.heuristic_func(neighbor_state, self.goal_node.state))
                    heapq.heappush(open_set, (neighbor_node.f(), id(neighbor_node), neighbor_node))

         
        return None

    def _reconstruct_path(self, node):
        path = []
        while node is not None:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))

 
def manhattan_distance(state, goal_state):
     
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

def get_neighbors(state):
     
    x, y = state
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]   
    
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < 10 and 0 <= ny < 10]   

start_state = (0, 1 )
goal_state = (5, 9)
astar = AStar(start_state, goal_state, get_neighbors, manhattan_distance)
path = astar.search()

if path:
    print("Path found: ", path )
else:
    print("No path found")
