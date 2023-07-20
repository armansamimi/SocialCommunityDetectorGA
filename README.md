# Detecting Communities in Social Networks Problem

To improve the performance of social networks in customer segmentation, targeting, and utilizing available information in social networks to achieve the maximum benefit from this information and complexity existing in these networks, advanced tools and techniques are required, and practically, it is impossible to do it manually.

One of these tools and approaches in extracting information from social networks is the concept of community detection. This concept has been used in various scientific fields such as physics, bioscience, computer science, economy, and social studies, and researchers in each of these fields have studied and expanded this concept from their own perspective.

A community within a network is a group of densely interconnected nodes that have more connections with each other than with nodes outside the community. In other words, it is a set of nodes that are more densely connected to each other within the community than to other nodes in the network.
Processes, methods, and algorithms used to identify and classify communities in social networks are called community detection. There are various types of algorithms for detecting communities in different types of graphs.

For example, special algorithms have been proposed for directed graphs, or algorithms proposed for undirected graphs are adapted to be used in directed graphs. Similarly, different algorithms have been proposed for weighted graphs or other types of graphs to be compatible with this type of graph. In addition to the type of graph, which determines the type of algorithm used, the communities themselves can be divided into two types: overlapping and non-overlapping. The graphs related to social networks are generally those graphs in which overlapping is allowed, which means that a node can be inside several communities.


# How to run:
For run this project you just need to run "GA-Main.py" file.
The dataset is automatically will be imported and the program try to find best community.

The input of the problem will be a list of graph edges and a txt file. In the first line, the number of nodes is specified. In the next lines, the first number will be the source node and the second number will be the destination node.

• Note that the input graphs are undirected.

