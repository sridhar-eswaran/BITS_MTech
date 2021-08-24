

# function to read input file and store each line as list
def readServerTransaction(filepath):
    with open(filepath) as file:   
        lines = file.readlines()  
    lines = [line.replace('\n','').split(',') for line in lines] 
    return lines

def getNodeList(input): 
    nodes = input[2]+input[3] 
    for node in range(3,len(input)): 
        nodes = nodes+input[node]
    nodes = ''.join(nodes) 
    nodes = ''.join(filter(lambda x: not x.isdigit(), nodes)) 
    nodes = list(set(nodes.replace(" ",""))) 
    return nodes 

def getEdgeList(input): 
    edges = {} 
    for node in range(2,len(input)): 
        edge = input[node][0].split(' ') 
        edges[(edge[0],edge[1])]=int(edge[2]) 
    return edges 

# function to find the shortest path using Dijkstra's algo
def dijktras(nodes,edges,source_index): 
    path_len = {v:float('inf') for v in nodes} 
    path_len[source_index] = 0 
    adjacent_nodes = {v:{} for v in nodes}  
    for (u,v), w_uv in edges.items(): 
        adjacent_nodes[u][v] = w_uv
    temp_node = [node for node in nodes] 
    while len(temp_node) > 0: 
        upper = {node: path_len[node] for node in temp_node} 
        u = min(upper,key=upper.get) 
        temp_node.remove(u) 
        for node,w_uv in adjacent_nodes[u].items(): 
            path_len[node] = min(path_len[node],path_len[u]+w_uv) 
    return path_len 



#read the file selected by user
input = readServerTransaction(txtfileLocation.name) # read the file selected by the user

# read info from the file selected
source_index = input[1][0][-1] 
nodes = getNodeList(input) 
edges = getEdgeList(input) 

# get the shortest path
path_lengths = dijktras(nodes,edges,source_index) 







