class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self) -> str:
        return self.__nome
    def get_idade(self) -> int:
        return self.__idade

    def __str__(self) -> str:
        return f"{self.__nome}:{self.__idade}"

class Motoca:
    def __init__(self, cliente: Pessoa = None, potencia: int = 1, tempo: int = 0):
        self.__cliente: Pessoa | None = None
        self.__potencia: int = potencia
        self.__tempo: int = tempo

    def inserir(self, cliente: Pessoa) -> bool:
        if self.__cliente != None:
            print("fail: busy motorcycle")
            return False
        self.__cliente = cliente
        return True

    def remover(self) -> Pessoa | None:
        if self.__cliente != None:
            print(f"{self.get_Cliente()}")
        if self.__cliente == None:
            print("fail: empty motorcycle")
            return None
        aux: Pessoa = self.__cliente
        self.__cliente = None
        return aux

    def comprarTempo(self, tempo: int) -> None:
        self.__tempo += tempo

    def dirigir(self, tempo: int) -> None:
        if self.__tempo == 0:
            print("fail: buy time first")
            return
        if self.__cliente == None:
            print("fail: empty motorcycle")
            return
        if self.__cliente.get_idade() > 10:
            print("fail: too old to drive")
            return
        if tempo > self.__tempo:
            print(f"fail: time finished after {self.__tempo} minutes")
            self.__tempo = 0
        else:
            self.__tempo -= tempo

    def buzina(self) -> None:
        print("P" + "e" * self.__potencia + "m")

    def get_Cliente(self) -> Pessoa | None:
        return self.__cliente
    def get_Potencia(self) -> int:
        return self.__potencia
    def get_Tempo(self) -> int:
        return self.__tempo

    def __str__(self) -> str:
        if self.__cliente == None:
            cliente_str = "empty"
        else:
            cliente_str = self.__cliente
        return f"power:{self.__potencia}, time:{self.__tempo}, person:({cliente_str})"

def main():
    moto = Motoca(None, 1, 0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "init":
            potencia = int(args[1])
            moto = Motoca(None, potencia, 0)
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            cliente = Pessoa(nome, idade)
            moto.inserir(cliente)
        elif args[0] == "leave":
            moto.remover()
        elif args[0] == "buy":
            tempo: int = int(args[1])
            moto.comprarTempo(tempo)
        elif args[0] == "drive":
            tempo: int = int(args[1])
            moto.dirigir(tempo)
        elif args[0] == "honk":
            moto.buzina()
        else:
            print("fail: comando invalido")

main()