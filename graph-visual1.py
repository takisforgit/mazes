####
## graph-visual1.py 
## Simple Graph Visualization
####

import networkx as nx
import matplotlib.pyplot as plt

graph = {
0: [1,5],
1: [0,2,3],
2: [1,4],
3: [1,4,5],
4: [2,3,5],
5: [0,3,4]
}


# extract nodes from graph
nodes = [v for v in graph] 
# print("Nodes:",nodes)

edges = [graph[node] for node in graph] 
# print("Per Node Edges List:",edges)

labels = {}

# create networkx graph
G=nx.Graph()
# # add nodes
for node in nodes:

	numOfNeigbors = len(graph[node])
	# print("Neighbors of node",node,":", end=" ")
	# print(edges[node])
	G.add_node(node)
	# Add label to each node
	labels[node] = node
	
## add edges
	for n in edges[node]:
		# print(node,"-->",n)
		G.add_edge(node,n)

# print(labels)
# print(G.nodes)
print(G.edges)

# positions for all nodes
pos = nx.shell_layout(G)
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
# edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=2)
# # labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

# show graph
plt.axis('off')
plt.title("Simple Graph Visualization")
plt.show()

########### DFS iteratively ##############
def dfs_iteratively(graph, root):

	visited = []
	stack = [root,]

	while stack:

		# Pop the LAST item in stack
		node = stack.pop()
		print("Popping:", node)

		if node not in visited:
			visited.append(node)
			print("Visited:",visited)
			
			# For all Neighbors of the node
			for x in graph[node]:
				if x not in visited:
					# Add NOT visited Neighbors to the stack
					stack.append(x)
				else:
					print("From", graph[node],"Already VISITED:",x)
			print("Stack:",stack)

	print("Stack is EMPTY. We have visited ALL nodes !")
	return visited


print("DFS iteratively: ",dfs_iteratively(graph,0))