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
            self._view._txtOut.controls.append(ft.Text(f"Inserire il campo mancante", color="red"))
            return

        annoInt= int(anno)
        self._model.buildGraph(colore,anno)
        self._view._txtOut.controls.append(ft.Text(f"Grafo correttamente creato."))
        self._view._txtOut.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} vertici e "
                                                   f"{self._model.getNumArchi()} archi."))

        self._view.update_page()




    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
