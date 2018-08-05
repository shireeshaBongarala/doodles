from graphviz import Digraph

g = Digraph(comment='The Round Table')
g.edge('Hello', 'World')
g.view()
