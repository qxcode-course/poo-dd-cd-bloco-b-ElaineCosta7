class Camisa:
    def __init__(self, tamanho: str):
        self.__tamanho = " "

    def set_tamanho(self, valor: str):
        if valor not in ["PP", "P", "M", "G", "GG", "XG"]:
            print("tamanho inválido")
            return False
        self.__tamanho = valor

    def get_tamanho(self) -> str:
        return self.__tamanho

    def __str__(self) -> str:
        return f"{self.__tamanho}"

camisa1 = Camisa("")
while True:
    if camisa1.get_tamanho() == " ":
        print("insira seu tamanho de camisa:")
        tamanho = input()
        if camisa1.set_tamanho(tamanho) != False:
            print("seu tamanho de camisa é", camisa1.get_tamanho())
            break