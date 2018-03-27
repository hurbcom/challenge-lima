# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Posicoes fora da Grid
class PosForaGrid(Exception):
    
    def __init__(self):         
        self.mensagem = "A posição que foi indicada está fora da área delimitada."
