
# will alays be dijkstra for this question
question_type = 'dijkstra'

# result_values states which value(s) of the table will be replaced with an input field.  
# List of tuples (row, iteration) 
result_values = []

# graph_values states which edge weights will be replaced when the template is generated. None values will be replaced with a text field.  
# List of tuples ((Vertex1, Vertex2), weight)
# If you wanted to change the edge weight between vertex 'A' and 'B' to 2 with a display value of None. The tuple would be (('A', 'B'), (2, None))
# Edges with a weight of none will show up as a textbox in the graph html.
graph_values = [
                [(('A','B'), (2, None)), (('B', 'C'), (9, 9))],
                [(('A','B'), (1, None)), (('B', 'C'), (7, None))],
                ]


# graph states the weight of each edge on the graph
# Dictionary within a dictionary [key=node] : {[key=node attached to main key] : [value=distance]}  

graph = {

         'A': {'B': 2, 'E': 2},
         'B': {'A': 2, 'C': 9, 'F': 5},
         'C': {'B': 9, 'G': 1},
         'D': {'E': 1, 'H': 3},
         'E': {'A': 2, 'D': 1, 'I': 9, 'F': 9},
         'F': {'B': 5, 'E': 9, 'J': 1, 'G': 1},
         'G': {'C': 1, 'F': 1},
         'H': {'I': 1, 'D': 3},
         'I': {'E': 9, 'H': 9, 'J': 1},
         'J': {'F': 1, 'I': 1},
}  

#the starting point for the algorithm
start_node = "H"
end_node = "C"
