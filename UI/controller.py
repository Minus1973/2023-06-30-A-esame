import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model


    def fillDDYear(self):
        years = self._model.getYears()
        for y in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(
                                                        text=y
                                                    ))
        self._view.update_page()


    # il metodo scrive le quadre di quell'anno
    def handleDDYearSelection(self, e):
        teams = self._model.getTeams(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text(f"ho trovato {len(teams)} squadre"))
        #popolo il DD con l'oggetto squadra
        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{t}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(
                                                    data=t,
                                                    text=t,
                                                    on_click=self.readDDTeams
                                                ))
        self._view.update_page()


    # legge dal DD quando seeziono un campo
    def readDDTeams(self, e):
        if e.control.data is None:
            self._selectedTeam = None
        else:
            self._selectedTeam = e.control.data
            # questo serve per debug
        print(f" medoto chiamato  {self._selectedTeam}")



    def handleCreaGrafo(self, e):
        if self._view._ddAnno.value is None:
            self._view._txt_result.controls.append(ft.Text("Seleziona un anno"))
            return
        #altrimenti
        self._model.creaGrafo(self._view._ddAnno.value)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        n,a = self._model.getGraphDetails()
        self._view._txt_result.controls.append(ft.Text(f"con {n} nodi e {a} archi"))
        self._view.update_page()

    def handleDettagli(self, e):
        v0 = self._selectedTeam
        vicini = self._model.getSortedNeighbors(self._selectedTeam)

        self._view._txt_result.controls.append(ft.Text("Stampo i vicini"))
        for t in vicini:
            self._view._txt_result.controls.append(ft.Text(f"{t[1]}  {t[0]}"))
        self._view.update_page()



    def handlePercorso(self, e):
        pass






