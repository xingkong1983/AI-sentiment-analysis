import pydot 

graph = pydot.Dot(graph_type='graph') 

for i in range(3):
 edge = pydot.Edge("Root", "Connection%d" % i)
 graph.add_edge(edge)

conn_num = 0
for i in range(3):
 for j in range(2):
  edge = pydot.Edge("Connection%d" % i, "Sub-connection%d" % conn_num)
  graph.add_edge(edge)
  conn_num  += 1

graph.write_png('./data/img/pydot-test-001.png')