# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Direcao Invalida
class DirInvalida(Exception):
    
    def __init__(self):         
        self.mensagem = "A direção indicada no comando não é um Ponto Cardeal. Indique um ponto cardeal."
