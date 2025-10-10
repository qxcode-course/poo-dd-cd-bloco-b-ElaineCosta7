class Chinela:
    def __init__(self, tamanho: int = 0):
        self.__tamanho: int = 0

    def set_tamanho(self, valor: int) -> None:
        if valor < 20 or valor > 50 or valor % 2 != 0:
            print("tamanho inválido")
            return True
        self.__tamanho = valor

    def get_tamanho(self) -> int: #leitura
        return self.__tamanho

    def __str__(self):
        return f"{self.__tamanho}"

chinela = Chinela()
while True:
    if chinela.get_tamanho() == 0:
        print("insira seu número de calçado:")
        tamanho = int(input())
        if chinela.set_tamanho(tamanho) != True:.
            print("seu número de calçado é", chinela.get_tamanho())
            break
