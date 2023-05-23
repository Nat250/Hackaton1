class Peca:
    def __init__(self,nome,quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def descricao(self):
        print("Restam %i da peça %s no estoque." % (self.quantidade, self.nome))

Parafuso      = Peca("Parafuso", 100)
Siglo_hp      = Peca("Siglo hp", 50)
Chassis       = Peca("Chassis", 15)
Roda          = Peca("Roda", 12)
Cart_Tinta_P  = Peca("Cartucho de Tinta Preto", 10)
Cart_Tinta_Am = Peca("Cartucho de Tinta Amarelo", 9)
Cart_Tinta_Az = Peca("Cartucho de Tinta Azul", 8)
Cart_Tinta_R  = Peca("Cartucho de Tinta Rosa", 7)