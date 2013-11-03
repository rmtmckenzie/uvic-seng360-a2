
# will alays be dijkstra for this question
question_type = 'dijkstra'

# result_values states which value(s) of the table will be replaced with an input field.  
# List of tuples (row, iteration) 
result_values = [
                 [('C', 5),('F', 3),('I', 6)],
                 [('C', 4),('F', 4),('I', 5)]
                 ]

# graph_values states which edge weights will be replaced when the template is generated. 
# List of tuples ((Vertex1, Vertex2), weight)
# If you wanted to change the edge weight between vertex 'A' and 'B' to 2 the tuple would be (('A', 'B'), 2)
graph_values = []


# graph states the weight of each edge on the graph
# Dictionary within a dictionary [key=node] : {[key=node attached to main key] : [value=distance]}  

graph = {

         'A': {'B': 1, 'E': 2},
         'B': {'A': 1, 'C': 8, 'F': 5},
         'C': {'B': 8, 'G': 1},
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
