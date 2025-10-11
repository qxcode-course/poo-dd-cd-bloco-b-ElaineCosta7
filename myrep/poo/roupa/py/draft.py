class Camisa:
    def __init__(self, tamanho: str):
        self.__tamanho = ""
        self.set_tamanho(tamanho)

    def set_tamanho(self, valor: str):
        if valor == "":
            return
        if valor not in ["PP", "P", "M", "G", "GG", "XG"]:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return False
        self.__tamanho = valor
        
    def get_tamanho(self) -> str:
        return self.__tamanho

    def __str__(self) -> str:
        return f"{self.__tamanho}"

def main():
    camisa = Camisa("")
    while True:
        line = input().strip()
        print(f"${line}")
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(f"size: ({camisa.get_tamanho()})")
        elif args[0] == "size":
            if len(args) == 1: # len descobre se existem args extras(eu acho)
                print(f"size: ({camisa.get_tamanho()})")
            else:
                camisa.set_tamanho(args[1])
        else:
            print("comando invalido")
    

main()