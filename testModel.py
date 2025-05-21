from model.model import Model

mymodel= Model()

mymodel.buildGraph("white",2018)

print(mymodel._graph.edges)
print(mymodel.getNumNodes())
print(mymodel.getNumArchi())
print(mymodel.top3Edges())