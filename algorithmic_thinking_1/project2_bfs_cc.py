'''
Implementation of BFS and Connected Componenets.
'''

# Queue class
class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """ 
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)
    
    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def enqueue(self, item):
        """
        Add item to the queue.
        """        
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []


# Function bfs_visited
# Returns list of all nodes that are visited
def bfs_visited(ugraph, start_node):
    "Implementation of Breadth-First-Search Algorithm"

    q_bfs = Queue()
    visited = set([]);
    visited.add(start_node);
    q_bfs.enqueue(start_node)

    while (len(q_bfs) > 0):
        j_node = q_bfs.dequeue()
        # for all the neighbours of j_node
        for h_node in ugraph[j_node]:
            if h_node not in visited:
                visited.add(h_node)
                q_bfs.enqueue(h_node);

    return visited;

# Function cc_visited
# print bfs_visited(GRAPH1, 0);
def cc_visited(ugraph):
    "compute list of connected componenet sets in the Graph"

    rem_nodes = ugraph.keys()
    conn_comps = []

    while(rem_nodes):
        start_node  = rem_nodes[0]
        visited = bfs_visited(ugraph, start_node)

        if (visited):
            conn_comps.append(visited)
        for visited_node in visited:
            try:
                rem_nodes.remove(visited_node);
            except ValueError:
                pass

    return conn_comps;

# print cc_visited(GRAPH1)

def largest_cc_size(ugraph):
    "Find the size of largest connected componenent in the graph"

    conn_comps = cc_visited(ugraph);
    max_size = 0;

    for one_set in conn_comps:
        size = len(one_set)
        if(max_size < size):
            max_size = size;

    return max_size

# print largest_cc_size(GRAPH1)

# Function compute_resilience
def compute_resilience(ugraph, attack_order):
    "Removes the nodes as in 'attack_order' then computes largest connected component size"

    temp_ugraph = ugraph;
    ret_list = []
    ret_list.append(largest_cc_size(ugraph))
    
    for attack_node in attack_order:
        # Delete the node
        del temp_ugraph[attack_node]
        for each_node in temp_ugraph.keys():
            # delete the edges
            if (attack_node in temp_ugraph[each_node]):
                temp_ugraph[each_node].remove(attack_node)
        ret_list.append(largest_cc_size(temp_ugraph))

    return ret_list;

# print compute_resilience(GRAPH1, [1, 2, 3, 4])
