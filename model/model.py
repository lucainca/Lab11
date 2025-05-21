import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._allProd= DAO.getAllProducts()
        self._allEdges= []
        self._idMap = {}
        for v in self._allProd:
            self._idMap[v.Product_number]= v

        self._numArchiTot= 0
        self._solOttima= []
        self._numSol=0




    def buildGraph(self,color,year):
        allNodes = DAO.getAllNodes(color)
        self._graph.add_nodes_from(allNodes)
        self.addEdges(year,color)
        self._allEdges= [self._graph.edges]


    def addEdges(self,year,color):

        for u in self._graph.nodes:
            for v in self._graph.nodes:
                if u != v:
                    peso = DAO.getAllEdgesW(u,v,year)
                    if peso[0]>0 :
                        self._graph.add_edge(u, v,weight=peso[0])

    def top3Edges(self):

        listaSort= sorted(self._graph.edges(data=True),key=lambda x: x[2]["weight"], reverse =True)

        return listaSort[:3]

    def top3Ripetuti(self):
        l= self.top3Edges()
        diz={}
        for r1 in l:
            if r1[0].Product_number not in diz:
                diz[r1[0].Product_number]= 1
            else:
                diz[r1[0].Product_number]+=1

            if r1[1].Product_number not in diz:
                diz[r1[1].Product_number] = 1
            else:
                diz[r1[1].Product_number] += 1
        return diz


    def bestPath(self,sorgente):

        source = self._idMap[sorgente]
        parziale=[]
        self._ricorsione(parziale,source,0)
        elenco=[]
        for i in self._solOttima:
            elenco.append(i[2]["weight"])
        print(len(self._solOttima), elenco)



    def _ricorsione(self,parziale,nodo,liv):

        admissibleEdges= self._getAsmissibleEdges(nodo,parziale)

        if len(admissibleEdges)==0:
            if len(parziale)> len(self._solOttima):
                self._solOttima=copy.deepcopy(parziale)
                elenco = []
                for i in self._solOttima:
                    elenco.append(i[2]["weight"])
                print(len(self._solOttima), elenco)

        for e in admissibleEdges:
            parziale.append(e)
            self._ricorsione(parziale,e[1],liv+1)
            parziale.pop()


    def _getAsmissibleEdges(self,nodo,parziale):

        archiVicini= self._graph.edges(nodo,data=True)
        result= []
        for a in archiVicini:
            if self._cresecente(a,parziale) and self._isNew(a,parziale):
                result.append(a)
        return result


    def _cresecente(self,a,parziale):
        if len(parziale)==0:
            return True
        if a[2]["weight"]>= parziale[-1][2]["weight"]:
            return True

    def _isNew(self,a,parziale):
        if len(parziale) == 0:
            return True
        inverso= (a[1],a[0],a[2])
        if inverso not in parziale and a not in parziale:
            return True












    def getColori(self):
        colori = DAO.getAllColori()
        return colori

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumArchi(self):
        return len(self._graph.edges)
