import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()




    def buildGraph(self,colore,year):

        self._nodes = DAO.getAllNodes(colore)
        self._idMap= {}
        for v in self._nodes:
            self._idMap[v.Product_number] = v

        self._graph.add_nodes_from(self._nodes)
        self.addEdges(year)



    def addEdges(self,year):
        edges = DAO.getAllArchi(self._idMap, year)
        for edge in edges:
            self._graph.add_edge(edge.p1,edge.p2, weight=edge.peso)


    def getColori(self):
        colori = DAO.getAllColori()
        return colori

    def getNumNodes(self):
        return len(self._nodes)

    def getNumArchi(self):
        return len(self._graph.edges)
