class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def get_capacidade(self) -> int:
        return self.__capacidade
    def get_carga(self) -> int:
        return self.__carga

    def set_capacidade(self, valor: int) -> None:
        self.__capacidade = valor
        
    def set_carga(self, valor: int) -> None:
        if valor < 0:
            self.__carga = 0
        elif valor > self.__capacidade:
            self.__carga = self.__capacidade
        else:
            self.__carga = valor

    def consumir(self, tempo: int):
        self.set_carga(self.__carga - tempo)

    def carregar(self, potencia: int, tempo: int):
        self.set_carga(self.__carga + (potencia * tempo))

    def mostrar(self):
        print(f"{self.__carga}/{self.__capacidade}")

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia

    def get_potencia(self) -> int:
        return self.__potencia

    def set_potencia(self, valor: int) -> None:
        self.__potencia = valor

    def mostrar(self):
        print(f"(Potência {self.__potencia})")

class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def get_ligado(self) -> bool:
        return self.__ligado

    def get_bateria(self) -> Bateria | None:
        return self.__bateria

    def get_carregador(self)-> Carregador | None:
        return self.__carregador

    def set_ligado(self, valor: bool) -> None:
        self.__ligado = valor

    def set_bateria(self, bateria: Bateria) -> None:
        self.__bateria = bateria

    def rm_bateria(self) -> Bateria | None:
        if self.__bateria == None:
            print("erro: sem bateria para remover")
            return None
        b = self.__bateria
        self.__bateria = None
        print("bateria removida")
        return b

    def set_carregador(self, carregador: Carregador) -> None:
        self.__carregador = carregador
        print("carregador conectado")

    def rm_carregador(self) -> Carregador | None:
        if self.__carregador:
            print("carregador removido")
        self.__carregador = None
    
    def ligar(self):
        if self.__ligado:
            print("notebook ligado")
        if self.get_ligado() != True:
            self.set_ligado(True)
        if(self.__bateria and self.__bateria.get_carga() > 0) or (self.__carregador is not None):
            self.__ligado = True
            print("notebook ligado")
        else:
            print("não foi possível ligar")

    def desligar(self):
        if not self.__ligado:
            print('notebook ja está desligado')
            return
        self.__ligado = False
        print("notebook desligado")

    def mostrar(self):
        bat = "nenhuma" if self.__bateria is None else f"({self.__bateria.get_carga()}/{self.__bateria.get_capacidade()})"
        car = "desconectado" if self.__carregador is None else f"(Potência {self.__carregador.get_potencia()})"
        status = "ligado" if self.__ligado else "desligado"
        print(f"Status: {status}, Bateria: {bat}, Carregador: {car}")

        if self.get_ligado() == False:
            print("Status: Desligado")
            return

    def usar(self, tempo: int):
        if not self.__ligado:
            print("erro: ligue o notebook primeiro")
            return
        if self.__bateria is None and self.__carregador is None:
            print('erro: sem energia')
            self.__ligado = False
            return
        if self.__bateria is None and self.__carregador is not None:
            print("Notebook utilizado com sucesso")
            return
        if self.__bateria is not None and self.__carregador is None:
            carga_atual = self.__bateria.get_carga()
            if carga_atual ==0:
                print(f"bateria descarregada")
                self.desligar()
                return
            if carga_atual < tempo:
                print(f"Usando por {carga_atual} minutos, notebook descarregou")
                self.__bateria.consumir(carga_atual)
                self.desligar()
            else:
                print(f"Usando por {tempo} minutos, notebook descarregou")
                self.__bateria.consumir(tempo)
            return
        if self.__bateria is not None and self.__carregador is not None:
            print("Notebook utilizado com sucesso")
            potencia = self.__carregador.get_potencia()
            self.__bateria.carregar(potencia, tempo)
            return


notebook = Notebook() # criando notebook
notebook.mostrar()    # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado
notebook.ligar()      # msg: não foi possível ligar
notebook.usar(10)     # msg: notebook desligado

bateria = Bateria(50) # criando bateria que suporta 50 minutos e começa carregada
bateria.mostrar()     # (50/50)
notebook.set_bateria(bateria) # coloca a bateria no notebook

notebook.mostrar() # msg: Status: Desligado, Bateria: (50/50), Carregador: Desconectado
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: (50/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 30 minutos
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 20 minutos, notebook descarregou
notebook.mostrar() # msg: Status: Desligado, Bateria: (0/50), Carregador: Desconectado

bateria = notebook.rm_bateria() # msg: bateria removida
bateria.mostrar()  # (0/50)
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado

carregador = Carregador(2) # criando carregador com 2 de potencia
carregador.mostrar() # (Potência 2)

notebook.set_carregador(carregador) # adicionando carregador no notebook
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: (Potência 2)
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: Nenhuma, Carregador: (Potência 2)

notebook.set_bateria(bateria)
notebook.mostrar() # msg: Status: Ligado, Bateria: (0/50), Carregador: (Potência 2)
notebook.usar(10)  # msg: Notebook utilizado com sucesso
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: (Potência 2)