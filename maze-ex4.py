import networkx as nx
import matplotlib.pyplot as plt

##############################################################
"""
Maze to Graph

First I would like to change the representation of the maze. 
This part is not necessary and we can detect "neighbours" while we search for a path. 
But for newbies it will be simpler to decompose the problem and first convert a maze into a 2D array 
and into a graph as a dictionary.

Our graph will be represented as a dictionary, where keys are node coordinates, 
values are neighbour node coordinates and directions are how to get to it. 
Node coordinates are represented as a tuple with two numbers. 
This way each cell has unique name. Directions will be useful to write the route
when we search for a path inside the maze.

First we collect all of the empty cells and write them as a keys. 
Then gather information about the neighbours.
We could do this in one iteration through a matrix with defaultdict, 
but I want to try a simpler method better suited for Python newbies. 
For each cell we only look at the "south" and "east" neighbours and add them as "connections". 
And with these directions we add the reverse "N" and "W" connection for neighbouring cells.
This way we skip duplicate operations.
Don't forget to check for edge cases. Below you can see the simple code for it. 

"""

def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    # print(height, width)
    # First we collect all of the empty cells and write them as a keys. 
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    print("Empty Cells:", graph)

    # # extract nodes from graph
    # # nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
    # # create networkx graph
    # G=nx.Graph()
    # # add nodes
    # for node in graph :
    #     G.add_node(node)
    # # add edges
    # for edge in graph:
    #     G.add_edge(edge[0], edge[1])
    # # draw graph
    # pos = nx.random_layout(G)
    # nx.draw(G, pos, Labels=True)
    # # show graph
    # plt.show()


    # For each cell we only look at the "south" and "east" neighbours and add them as "connections".
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph


#### Main #####

maze1  = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

graph2= maze2graph(maze1)
# print(graph2)

# for key in graph2.keys():
#     # print(key, graph2[key])
#     print(key,"-->", end="")
#     for i in range(len(graph2[key])):
#         print(graph2[key][i],  end="")
#     print()

# print("\n\n",graph2[(1,1)])


# for key in graph2.keys():
#     print(key)

##############################################################
""" Breadth(Depth)-First Search

Breadth-first_search and Depth-first_search are similar to each other.
DFS visits the child nodes before visiting the sibling nodes; 
that is, it traverses the depth of any particular path before exploring its breadth.
BFS visits the parent nodes before visiting the child nodes. 
A stack is used for DFS and a queue for BFS. So you can easily "switch" DFS to BFS.
@spoty's solution "BFS + deque" is a classical BFS realisation, using a double ended queue.

It's faster than using a list and also we can easily switch BFS to DFS by simply
replacing "q.popleft()" => "q.popright()".
"""

# from collections import deque
# ​​
# def checkio(maze_map, start=(1, 1), goal=(10, 10)):
#     def get_adjacent(n):
#         x, y = n
#         n = [(x - 1, y, "N"), (x, y - 1, "W"),
#              (x + 1, y, "S"), (x, y + 1, "E")]
#         return [((x, y), c) for x, y, c in n if maze_map[x][y] != 1]
# ​
#     q, v = deque([(start, "")]), set()
# ​
#     while q:
#         cords, path = q.popleft()
#         if cords == goal:
#             return path + mark
#         if cords in v:
#             continue
#         v.add(cords)
#         for pos, mark in get_adjacent(cords):
#             if pos in v:
#                 continue
#             else:
#                 q.append((pos, path + mark))


##############################################################
"""
A* search algorithm
As A* traverses the graph, it follows a path of the lowest expected total cost or distance, keeping a sorted priority queue of alternate path segments along the way. You can read more on Wikipedia.
For priority queuing, Python has the heapq module and @PositronicLlama's solution "First" takes advantage of it combined with namedtuples to add readabilty here.
"""

"""
Navigate a maze and return a route from the start to the finish.
Use A* to find a path in an efficient manner.
"""

# import heapq
# import collections
# ​
# # The cardinal directions
# DIRECTIONS = [
#         (0, -1, 'N'),
#         (0, 1, 'S'),
#         (-1, 0, 'W'),
#         (1, 0, 'E'),
#     ]
# ​
# Node = collections.namedtuple('Node', ['hist', 'ix', 'dist', 'pt', 'prev', 'direction'])
# ​
# def heuristic(point, goal):
#     """
#     Return an admissible heuristic for the distance from point to goal.
#     For the case of a grid with orthogonal movement, use the Manhattan distance.
#     """
#     return abs(point[0] - goal[0]) + abs(point[1] - goal[1])
# ​
# def checkio(labyrinth):
#     """
#     Return a string of the characters [NSEW] describing a path through labyrinth.
#     labyrinth: A list of lists.  '0' indicates a passable cell.
#     """
#     height, width = len(labyrinth), len(labyrinth[0])
#     start = (1, 1)
#     goal = (height - 2, width - 2)

#     # Each node consists of (estimated path distance, ix, dist, (x, y), previous node, direction)
#     # The ix field is a serial number to ensure that subsequent fields are
#     # not compared.
#     open = [Node(heuristic(start, goal), 0, 0, start, None, None)]

#     # A set of all visited coordinates.
#     explored = set()

#     ix = 1
#     while open:
#         node = heapq.heappop(open)
#         _, _, dist, point, prev, prev_d = node
#         if point in explored:
#             continue
#         if point == goal:
#             break
#         explored.add(point)

#         # Now consider moves in each direction.
#         for dx, dy, d in DIRECTIONS:
#             new_point = point[0] + dx, point[1] + dy
#             if new_point not in explored and \
#             not labyrinth[new_point[1]][new_point[0]]:
#                 h = dist + 1 + heuristic(new_point, goal)
#                 tie_break = 4 if prev_d != d else 0 # Prefer moving straight
#                 new_node = Node(h, ix + tie_break, dist + 1, new_point, node, d)
#                 heapq.heappush(open, new_node)
#                 ix = ix + 1
# ​
#     # Return a path to node
#     result = ''
#     while node.prev is not None:
#         result = node.direction + result
#         node = node.prev
#     return result
    