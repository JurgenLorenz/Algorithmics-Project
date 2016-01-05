from time import *
rows = raw_input('S:')
rows = rows.strip().split(" ")
nodes = []
keyboard = []
count = 2

#print starttime
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

def dijkstra(keyboard, nodes, distances, text):
    summa = 0
    if text[0] == nodes[0]:
        summa +=1
    else:
        text = nodes[0] + text
    text = text + '*'
    #print text
    for i in range(len(text)-1):
        
        unvisited = {node: None for node in nodes} #using None as +inf
        visited = {}
        current = text[i][0]
##        print "current"
##        print current
        currentDistance = 0
        unvisited[current] = currentDistance

        while True:
##            print "visited"
##            print visited
            for neighbour, distance in distances[current].items():
                if neighbour not in unvisited: continue
                newDistance = currentDistance + distance
                if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                    unvisited[neighbour] = newDistance
            visited[current] = currentDistance
            del unvisited[current]
            if not unvisited: break
            candidates = [node for node in unvisited.items() if node[1]]
##            print "kandidaadid"
##            print current
##            print candidates
            current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
        #print candidates
        kandidaadid = []
        nextletter = text[i+1][0]
        for key in visited.keys():
            if key[0] == nextletter:
                kandidaadid.append((key,visited[key]))
        kandidaadid = sorted(kandidaadid, key=lambda x: x[1])
        #print(kandidaadid)
        number = kandidaadid[0][1]
        
        summa += number + 1
        #print summa
    return summa

#print rows
#print keyboard
#print text
#print nodes
dist = check_neighbours(keyboard)
#print nodes
new = []
for i in range(20):
    starttime = time()
    dijkstra(keyboard,nodes, dist,text)
    endtime = time()
    elapsed = endtime-starttime
    new.append(elapsed)

    kesk = float(sum(new))/len(new)
    f = open('dijkstraCONTEST.txt', 'a')
    f.write(str(kesk)+'\n')
    f.close()


