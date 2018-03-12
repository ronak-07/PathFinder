
PathFinder
===========
Finding optimised path between source and destination using A-star algorithm. 

Usage
------

- Map (.osm) data has to be converted to a suitable format to create a graph

      python run.py -f short_map.osm -n p
		
- Now the obtained data has to be used to make graph and run A* on it. The output is three files. The final cordinates that are to be plotted on map, the nodes visited in order by A* search and also the node numbers of the final co-ordinates.

      python main.py 
		
- Now, to plot the co-ordinates on the map, we use selenium webdriver. This gives us the final path.

      python map.py

![alt text](https://github.com/ronak-07/PathFinder/blob/master/Secundrabad_RGIA.png)

General Description
-------------------
- Using OsmToRoadGraph repository by [AndGem](https://github.com/AndGem) osm file can be converted to graph with nodes and vertex, also the distance between them(g(x)).
- Using A* algorithm and the graph above, relevant nodes are stored.
- Using Selenium webdriver these coordinates are plotted on the map. 
- For the heuristic value (h(x)), geopy package was used.


Contributors
--------------

Aakanksha Mudgal  
Ronak Sisodia   
Yash Raj Jain
