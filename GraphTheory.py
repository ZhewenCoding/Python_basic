#测试MAAS 图论 未报错 但不出图 Colab可出图
#原理：使用networkx模块draw()函数构造graph，使用matplotlib把图显示出来
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from graphviz import Digraph
import scipy as sp
# G=nx.Graph()
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_edge(1,2)
# G.add_edge(1,3)
# nx.draw(G,with_labels=True)
# nx.draw(G,with_labels=True,node_color="r",edge_color="g")
# plt.show()         #要出图 必须导入matplotlib中的pyplot并调用show函数

# G=nx.Graph()
# G.add_edges_from([("Sensor","Controller"),
#                   ("Controller","Actuator"),
#                   ("Actuator","Plant"),
#                   ("Plant","Sensor")])
# nx.draw(G,with_labels=True,node_shape="s",node_size=4000)
# plt.show()

# G=nx.Graph()    #degree正常显示  indegree/outdegree报错 不存在这两个函数
# G.add_edges_from([(2,1),(2,3),(2,4),(3,1),(4,3),(5,2)])
# nx.draw(G,with_labels=True)
# print('Degree:',G.degree())
# print('InDegree:',G.in_degree())
# print('OutDegree:',G.out_degree())


#测试GraphViz工具包   不能出图
# from graphviz import Digraph
# G=Digraph('G')
# G.edges([('1','2'),('1','3'),('1','1'),('1','2')])
# plt.show()

#知乎测试：
# import networkx as nx
#
# oo = float('inf')
#
# # 创建无向图
# G = nx.Graph()
# G.add_node(1) # 添加节点１
# G.add_edge(2,3) #　添加节点２，３并链接２３节点
# print(G.nodes, G.edges, G.number_of_nodes(), G.number_of_edges())
# # 创建有向图
# G = nx.DiGraph()
# G.add_edge(2, 3)
# G.add_edge(3, 2)
# G.to_undirected()  # 转换成无向图
# print(G.edges)

#测试Numpy 已成功出图

#
# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y)
# plt.show()

# G = Digraph('G')
# G.edges([('1','2'),('1','3'),('1','1'),('1','2')])
# # G
# plt.show()

# G = nx.DiGraph()
# G.add_nodes_from([1,2,3,4,5])
# G.add_edges_from([(2,1),(2,3),(2,4),(3,1),(4,3),(5,2)])
# nx.draw(G,with_labels = True,node_size = 2000)
# print(nx.adjacency_matrix(G))

#Weighted matrices
# G = nx.Graph()
# G.add_edge(1,1,weight = 2)
# G.add_edge(1,2,weight = 11)
# G.add_edge(1,3,weight = 10)
# G.add_edge(2,3,weight = 15)
# pos = nx.spring_layout(G)
# nx.draw_networkx(G,pos)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#不出图

#DFS/BFS
G = nx.DiGraph()
G.add_edges_from([('A','B'),
                  ('B','D'),
                  ('A','C'),
                  ('C','E'),
                  ('C','F')])
nx.draw(G,with_labels=True,node_size=2000)
print('BFS:',list(nx.bfs_edges(G,'A')))
print('DFS:',list(nx.dfs_edges(G,'A')))
#不出图 打印正常

