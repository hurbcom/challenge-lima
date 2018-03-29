# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Posicoes fora da Grid
class PosForaGrid(Exception):
    
    def __init__(self):         
        self.mensagem = "A coordenada que foi indicada esta fora da area delimitada."
