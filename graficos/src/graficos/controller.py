from graficos.view import View
from graficos.model import Model

class Controller:
    def __init__(self):
        self.view = view = View()
        self.model = Model(view)
        

    def run(self):
        self.view.iniciar_interface()