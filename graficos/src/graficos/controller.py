from graficos.view import View
from graficos.model import Model

class Controller:
    def __init__(self):
        self.view = view = View()
        self.model = Model(view)

        # Subscrições de eventos da View
        self.view.importar_ficheiro_click_evt.add_handler(self.user_importa_ficheiro)

    def run(self):
        self.view.iniciar_interface()

    def user_importa_ficheiro(self) -> None:
        # TODO:
        print("Controller recebeu evento (da View) de que user seleccionou importar ficheiro")
        # Aqui vamos da instrução à View para mostrar o file selection dialog para o user selecionar um
        # ficheiro do file system para ser importado