import pdb
from time import *
"""
The Bellman-Ford algorithm
Graph API:
    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
"""

new = []

def check_neighbours(matrix):
    dictionary = {}
    suund = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            distances = {}
            node = matrix[i][j]
##            if node[0] in dictionary:
##                continue
            lisai = i
            lisaj = j
            if i < len(matrix)-1:
                value = matrix[lisai+1][j]
##                while value == node:
##                    lisa += 1
##                    if i+lisa < len(matrix):
##                        value = matrix[i+lisa][j]
                while value[0] == node[0] and lisai+1 < len(matrix)-1:
                    lisai += 1
                    value = matrix[lisai][j]
                else:
                    distances[value] = 1
##                lisa = 1
                lisai = i
            if j < len(matrix[i])-1:
                value = matrix[i][lisaj+1]
##                while value == node:f
##                    lisa += 1
##                    if j+lisa < len(matrix[0]):
##                        value = matrix[i][j+lisa]
##                print 'konn'
##                print value
##                print lisaj
                while value[0] == node[0] and lisaj+1 < len(matrix[0])-1:
                    lisaj += 1
                    value = matrix[i][lisaj+1]                    
                else:
                    distances[value] = 1
                lisaj = j
            if i > 0:
                value = matrix[lisai-1][j]
                while value[0] == node[0] and lisai-1 >= 0:
                    lisai -= 1
                    value = matrix[lisai][j]
                else:
                    distances[value] = 1
            if j > 0:
                value = matrix[i][lisaj-1]
##                print value
                while value[0] == node[0] and lisaj >= 0:
                    lisaj -= 1
                    value = matrix[i][lisaj-1]
                else:
                    distances[value] = 1
            dictionary[node] = distances
    return dictionary

# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p


def test(keyboard,letter):
    graph = check_neighbours(keyboard)

    d, p = bellman_ford(graph, letter)
    return d, p


if __name__ == '__main__':
    rows = raw_input('S:')
    rows = rows.strip().split(" ")
    nodes = []
    keyboard = []
    count = 2
    summa = 0
    
    for i in range(int(rows[0])):
        keys = raw_input()
        for key in keys:
            #print key
            if key in nodes:
                uus = key + str(count)
                nodes.append(uus)
                count = count +1
    ##            print count
            if key not in nodes:
                nodes.append(key)
    for i in range(int(rows[0])):
        rida = []
        for j in range(int(rows[1])):
            rida.append(nodes[i*int(rows[1])+j])
        keyboard.append(rida)
    
    ##print keyboard
    text = raw_input('Type: ')
    for i in range(1):
        starttime = time()
        text = text + '*'
        if text[0] == nodes[0]:
            summa +=1
        else:
            text = nodes[0]+text
        current = text[0]
        for i in range(len(text)-1):
            d,p = test(keyboard, current)
            nextletter = text[i+1]
            #print current
            kandidaadid = []
            for key in d.keys():
                if key[0] == nextletter:
                    kandidaadid.append((key,d[key]))
    ##        print "visited"
    ##        print visited
            kandidaadid = sorted(kandidaadid, key=lambda x: x[1])
            current = kandidaadid[0][0]
            number = kandidaadid[0][1]

            summa +=number+1
        #print summa
        endtime = time()
        new.append(endtime-starttime)


kesk = float(sum(new))/len(new)
f = open('bellmannACM.txt', 'a')
f.write(str(kesk)+'\n')
f.close()
