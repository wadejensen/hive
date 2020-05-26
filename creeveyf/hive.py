#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import networkx as nx
from enum import Enum


# In[2]:


nodes = 6
G = nx.Graph()
G.add_node(0)
for node in range(nodes):
    G.add_node(node + 1)
    G.add_edge(0, node + 1)
G.add_edge(nodes, 0)

nx.set_node_attributes(G, '', 'colour')
nx.set_node_attributes(G, '', 'name')


# In[40]:


class Queen:
    
    def __init__(self, color):
        self.color = color
        self.range = 1
    
    def place(self, graph, position):
        graph.add_node(position, piece=self)
        addEmpties(graph, position)
            
            
#     def move(self, turn, graph, start, end):
#         if 
        
def addEmpties(graph, position):
    surroundingNodes = [(position[0], position[1] + 1, position[2] + 1),
                        (position[0] + 1, position[1] + 1, position[2]),
                        (position[0] + 1, position[1], position[2] - 1),
                        (position[0], position[1] - 1, position[2] - 1),
                        (position[0] - 1, position[1] - 1, position[2]),
                        (position[0] - 1, position[1], position[2] + 1)]
    for counter, node in enumerate(surroundingNodes):
        graph.add_node(node, piece=Empty())
        if counter > 0:
            graph.add_edge(position, node)
            graph.add_edge(node, surroundingNodes[counter - 1])
    graph.add_edge(position, surroundingNodes[0])
    graph.add_edge(surroundingNodes[5], surroundingNodes[0])
        
    

class Beetle:
    
    def __init__(self, color):
        self.color = color
        self.range = 1
        
class Spider:
    
    def __init__(self, color):
        self.color = color
        self.range = 3

class Ant:
    
    def __init__(self, color):
        self.color = color

class Grasshopper:
    
    def __init__(self, color):
        self.color = color

class Empty:
    
    def __init__(self):
        pass


# In[41]:


graph = nx.Graph()
wq = Queen('white')
wq.place(graph, (0, 0, 0))
nx.draw(graph)


# In[18]:


graph = nx.Graph()
one = Piece(Bug.queen, Color.white)
two = Piece(Bug.queen, Color.white)
three = Piece(Bug.queen, Color.white)
graph.add_node(one)
graph.add_node(two)
graph.add_node(three)
nx.draw(graph)


# In[6]:


one.color


# In[ ]:





# In[12]:


graph = nx.Graph()
graph.add_node((1,1,1), piece="wade")


# In[14]:


graph.nodes[(1,1,1)]['piece']


# In[9]:


graph.nodes.items()


# In[10]:


x = (0, 0, 0)
# y = (0, 1, 1)

distance = np.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2)


# In[11]:


distance


# In[ ]:




