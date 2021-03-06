def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def path(G, v1, v2):
    distance_from_start={}
    open_list=[v1]
    distance_from_start[v1]=[v1]
    while len(open_list)>0:
        current=open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor]=distance_from_start[current]+[neighbor]
                if neighbor==v2:
                    return distance_from_start[v2]
                open_list.append(neighbor)
    return False

def centrality(G, v):
    distance_from_start={}
    open_list=[v]
    distance_from_start[v]=0
    while len(open_list)>0:
        current=open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor]=distance_from_start[current]+1
                open_list.append(neighbor)
    return (sum(distance_from_start.values())+0.0)/len(distance_from_start)

chain=((1, 2), (2, 3), (3, 4), (4, 5), (5, 6))
G={}
for n1, n2 in chain:
    make_link(G, n1, n2)
print path(G, 1, 6)
print centrality(G, 1)