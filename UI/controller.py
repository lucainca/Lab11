import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):

        for c in self._model.getColori():
            self._view._ddcolor.options.append(ft.dropdown.Option(c))


        years= list(range(2015, 2018+1))
        for y in years:
            self._view._ddyear.options.append(ft.dropdown.Option(y))

        self._view.update_page()


    def handle_graph(self, e):


        anno = self._view._ddyear.value
        colore= self._view._ddcolor.value

        if anno == "" or colore == "":
            self._view.txtOut.controls.append(ft.Text(f"Inserire il campo mancante", color="red"))
            return


        self._model.buildGraph(colore,anno)
        self.fillDDProduct()
        self._view.txtOut.controls.append(ft.Text(f"Grafo correttamente creato."))
        self._view.txtOut.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} vertici e "
                                                   f"{self._model.getNumArchi()} archi."))


        for e in self._model.top3Edges():

            self._view.txtOut.controls.append(
                ft.Text(f"Arco da {e[0].Product_number} a {e[1].Product_number} con peso {e[2]["weight"]}"))
        daStampare = []
        for nodo in self._model.top3Ripetuti().items():
            chiave,valore= nodo
            if valore>1:
                daStampare.append(chiave)

        self._view.txtOut.controls.append(ft.Text(f"I nodi ripetuti sono: {daStampare}"))


        self._view.update_page()




    def fillDDProduct(self):
        for n in self._model._graph.nodes:
            self._view._ddnode.options.append(ft.dropdown.Option(n.Product_number))
        self._view.update_page()


    def handle_search(self, e):
        self._model.bestPath(int(self._view._ddnode.value))
        self._view.txtOut.controls.append(ft.Text(f"Numero archi percorso più lungo: {len(self._model._solOttima)}")
        )
        self._view.update_page()
