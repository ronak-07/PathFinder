#AIzaSyCvH5ES6C4QtiM9mDWLGPjHVTqrw6AHKhA
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCvH5ES6C4QtiM9mDWLGPjHVTqrw6AHKhA')
from geopy.distance import vincenty

output = open("astar.txt","w+")
output2 = open("final_cords.txt","w+")
output3 = open("taken_path.txt","w+")

class Graph: 
    nodes = {}
    graphs = {}
    heuristic = {}
    
    def _init_(self):
        Graph.nodes = {}
        Graph.graphs = {}
       
    def add_vertex(self,l):
        Graph.nodes[int(l[0])]=[l[1],l[2]]

    def ini(self):    
        for i in range(0,int(n_nodes)):
            Graph.graphs[i] = []

    def add_edge(self,l):
        Graph.graphs[int(l[0])].append([int(l[1]),float(l[2])])
        Graph.graphs[int(l[1])].append([int(l[0]),float(l[2])])

    #above method run for all coordinates 
    #def find_heuristic(self,l):
       
graph_file = open("short_map.pypgr")
temp = graph_file.readlines()
graph_file.close
graph_file = open("short_map.pypgr","w+")
for i in range(0,len(temp)):
    if i >= 7:
        graph_file.write(temp[i])
graph_file.close()
graph_file = open("short_map.pypgr")
x = graph_file.read()
lines = x.split("\n")
n_nodes = lines[0]
n_edges= lines[1]
print(lines[0])
print(lines[1])
graph = Graph()
graph.ini()
for i in range(2,2+int(n_nodes)):
    graph.add_vertex(lines[i].split(" "))
    node=lines[i].split(" ")
    #graph.find_heuristic(lines[i].split(" "))
    

for i in range(2+int(n_nodes),2+int(n_nodes)+int(n_edges)):
	graph.add_edge(lines[i].split(" "))
print("Edges added")

start=2283 #isko change karna h.. start and goal
goal= 5466

origin = ((graph.nodes[start])[0],(graph.nodes[start][1]))
destination = ((graph.nodes[goal])[0],(graph.nodes[goal][1]))

for i in range(0,int(n_nodes)):
    #temp=line[i].split(" ")
    #print(temp[0])
    temp = ((graph.nodes[i])[0],(graph.nodes[i][1]))
    Graph.heuristic[i]= vincenty(temp,destination).meters #float(temp[1])
    print (Graph.heuristic[i])

def children(index):
    return Graph.graphs[index]

def aStar(start, goal):
    parent = {}
    g={}
    openset = set()
    closedset = set()   
    current = start
    openset.add(current)
    g[current]=0
    while openset:
        current= min(openset, key= lambda l: int(Graph.heuristic[l])+int(g[l]))
        output3.write((graph.nodes[int(current)])[0] + "," + (graph.nodes[int(current)])[1]+"\n")
        if current == goal:
            path=[]
            while current!=start: 
                path.append(current)
                current=parent[current]
            path.append(current)
            return path[: :-1]
        
        openset.remove(current)
        closedset.add(current)
        
        for l in children(current):
            if int(l[0]) in closedset:
                continue
            if int(l[0]) in openset:
                new_g = g[current] + l[1]
                if g[l[0]] > new_g: #initialize G[] properly
                    #If so, update the node to have a new parent
                    g[l[0]] = new_g
                    parent[l[0]] = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                g[l[0]] = g[current] + l[1]
                #Set the parent to our current item
                parent[l[0]] = current
                #Add it to the set
                openset.add(l[0])
    print (openset)
    raise ValueError('No Path Found')
    
for i in aStar(start,goal):
    output.write(str(i) + "\n")
    output2.write((graph.nodes[int(i)])[0] + "," + (graph.nodes[int(i)])[1]+"\n")