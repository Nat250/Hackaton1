class Corredor:
    def __init__(self,numero,posicao):
        self.numero = numero
        self.posicao = posicao

    def Pos_Prat(self):
        print("Restam %i da peça %s no estoque." % (self.quantidade, self.nome))