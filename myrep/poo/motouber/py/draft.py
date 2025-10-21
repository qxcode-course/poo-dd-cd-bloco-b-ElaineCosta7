class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome: str = nome
        self.__dinheiro: int = dinheiro

    def get_nome(self) -> str:
        return self.__nome
    def get_dinheiro(self) -> int:
        return self.__dinheiro

    def set_dinheiro(self, valor: int) -> int:
        self.__dinheiro = valor

    def __str__(self) -> str:
        return f"{self.__nome}:{self.__dinheiro}"

class Moto:
    def __init__(self, motorista: Pessoa | None, passageiro: Pessoa | None, custo: int):
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None
        self.__custo: int = custo

    def adicionar_motorista(self, motorista: Pessoa) -> bool:
        if self.__motorista != None:
            return False
        self.__motorista = motorista
        return True

    def adicionar_passageiro(self, passageiro: Pessoa) -> bool:
        if self.__passageiro != None:
            return False
        self.__passageiro = passageiro
        return True

    def remover_passageiro(self) -> Pessoa | None:
        if self.__passageiro == None:
            print("fail: sem passageiro")
            return
        aux: Pessoa = self.__passageiro
        if self.__passageiro.get_dinheiro() < self.__custo:
            print("fail: Passenger does not have enough money")
            self.__passageiro.set_dinheiro(0)
            self.__motorista.set_dinheiro(self.__motorista.get_dinheiro() + self.__custo)
            self.__custo = 0
            self.__passageiro = None
            print(F"{aux} left")
            return
        if self.__passageiro.get_dinheiro() > self.__custo:
            self.__passageiro.set_dinheiro(self.__passageiro.get_dinheiro() - self.__custo) 
            self.__motorista.set_dinheiro(self.__motorista.get_dinheiro() + self.__custo)
            self.__custo = 0
            self.__passageiro = None
            print(F"{aux} left")
            return

    def dirigir(self, custo = int) -> None:
        self.__custo += custo

    def get_motorista(self) -> Pessoa | None:
        return self.__motorista
    def get_passageiro(self) -> Pessoa | None:
        return self.__passageiro
    def get_custo(self) -> int:
        return self.__custo

    def __str__(self) -> str:
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"
    
def main():
    moto = Moto(None, None, 0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            motorista = Pessoa(nome, dinheiro)
            moto.adicionar_motorista(motorista)
        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            passageiro = Pessoa(nome, dinheiro)
            moto.adicionar_passageiro(passageiro)
        elif args[0] == "drive":
            custo: int = int(args[1])
            moto.dirigir(custo)
        elif args[0] == "leavePass":
            moto.remover_passageiro()
        else:
            print("fail: comando invalido")

main()