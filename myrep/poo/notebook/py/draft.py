class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

class Carregador:
    def __init__(self, potencia):
        self.__potencia: int = potencia

class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None

    def ligar(self):

    def desligar(self):

    def mostrar(self) -> bool:
        print(f"status: {self.__ligado}")

    def usar(self, tempo):


notebook = Notebook() # criando notebook
notebook.mostrar()    # msg: Status: Desligado
notebook.usar(10)     # msg: erro: ligue o notebook primeiro
notebook.ligar()      # msg: notebook ligado
notebook.mostrar()    # msg: Status: Ligado
notebook.usar(10)     # msg: Usando por 10 minutos
notebook.desligar()   # msg: notebook desligado