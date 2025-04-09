import copy
import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allTeams=[]
        self._grafo = nx.Graph()
        #creo una mappa con id Teams e gli oggetti Teams
        self._idMap ={}

    def getTeams(self, year):
        return DAO.getTeams(year)


    def creaGrafo(self,year):
        self._grafo.clear()
        teams= DAO.getTeams(year)
        self._grafo.add_nodes_from(teams)
        # in questo momento creo la mappa id-oggetto Teams
        for t in teams:
            self._idMap[t.ID] = t


        #metto gli archi facendo tutte le combinazioni possibili. Essendo grafico semplice l'arco inverso lo sovrascrive (a,b) (b,a)
        for t1 in self._grafo.nodes:
            for t2 in self._grafo.nodes:
                #essendo grafico semplice sovrascrive le coppie inverse qundi basta togliere le coppie (a,a) (b,b)...
                #cosi però non sbaglio di sicuro
                if t1.ID<t2.ID:
                    if self._grafo.has_edge(t1,t2):
                        self._grafo.edges[t1,t2]["weight"] += (t1.totSalary + t2.totSalary)
                    else:
                        self._grafo.add_edge(t1,t2, weight = t1.totSalary + t2.totSalary)


        #in alternativa uso la libreria itertool
        #in myedges ho una lista di tuple
        #myedges = list(itertools.combinations(self._allTeams, 2))
        #essendo lista di tuple posso usare add_adges_from
        #self._grafo.add_edges_from(myedges)

        # #aggiungo i pesi che sono i salari
        # salaryOfTeams = DAO.getSalaryOfTeams(year, self._idMap)
        #
        # #ciclo sugli archi e aggiungo la somma dei pesi
        # for e in self._grafo.edges:
        #     #in e c'è una tupla con i due nodi dell'arco
        #     self._grafo[e[0]][e[1]]["weight"] = salaryOfTeams[e[0]] + salaryOfTeams[e[1]]




    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)



    #ottengo i vicini di un nodo
    def getSortedNeighbors(self,v0):
        vicini = self._grafo.neighbors(v0)
        #archi
        viciniTuples=[]
        for v in vicini:
            #appendo la tupla composta dal nodo vicino e dal suo peso rispetto al nodo sorgente
            viciniTuples.append((v,self._grafo[v0][v]["weight"]))
        #ordino la lista di tuple per peso che è il secondo elemento della tupla
        viciniTuples.sort(key = lambda x: x[1], reverse=True)
        return viciniTuples





    def getYears(self):
        return DAO.getAllYears()



