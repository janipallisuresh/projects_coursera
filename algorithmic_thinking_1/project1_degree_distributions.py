'''
Construct Graphs and Compute Degree Distributions
'''
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])
             }
EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0, 4, 5, 6, 7, 3])
             }

# Function make_complete_graph
def make_complete_graph(num_nodes):
    "Constructs a Complete Graph with number of nodes as 'num_nodes'"
    
    ret_graph = {}
    for i_node in range (0, num_nodes):
        ret_graph[i_node] = set([])

    for i_node in range(0, num_nodes):
        for j_node in range (i_node+1, num_nodes):
            ret_graph[i_node].add(j_node);
            ret_graph[j_node].add(i_node);

    return ret_graph

#print( make_complete_graph(10))

# Function compute_in_degrees
# Returns indegrees of all nodes as a dictionary where
# keys: nodes
# values: in degress of correspoding nodes
def compute_in_degrees(digraph):
    "Calculates Indegrees of all nodes"
    
    ret_indegree = {}
    for each_node in digraph.keys():
        ret_indegree[each_node] = 0;

    for each_node in ret_indegree.keys():
        for each_value in digraph[each_node]:
            ret_indegree[each_value] = ret_indegree[each_value]+1
    return ret_indegree

#print compute_in_degrees(EX_GRAPH1)

# Function in_degree_distribution
# Returns in degree distibution of a graph as dictionary where
# keys : indegrees
# values : No.of nodes with corresponding in degree.
def in_degree_distribution(digraph):
    "calculate In degree distribution for all in degrees"
    
    ret_indeg_dist = {}
    in_degrees = compute_in_degrees(digraph)

    for each_key in in_degrees:
        if in_degrees[each_key] not in ret_indeg_dist.keys():
            ret_indeg_dist[in_degrees[each_key]] = 0   
        ret_indeg_dist[in_degrees[each_key]] = ret_indeg_dist[in_degrees[each_key]] + 1;

    return ret_indeg_dist;

#print in_degree_distribution(EX_GRAPH1)
