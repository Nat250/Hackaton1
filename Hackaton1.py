import numpy as np
from Corredor import Corredor
from Peca import *

"""
Arrays representam o Marketplace
Cada array é um corredor, cada posição é uma seção de array """

Corredor_1 = Corredor(1,np.array([[Parafuso, Siglo_hp],[Chassis, Roda]]))
Corredor_2 = Corredor(2,np.array([[Cart_Tinta_Am, Cart_Tinta_Az], [Cart_Tinta_P, Cart_Tinta_R]]))

" Para cada prateleria, uma matriz representa as peças "

