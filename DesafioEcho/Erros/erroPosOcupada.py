# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Posicoes Ocupadas
class PosOcupada(Exception):
    
    def __init__(self,tipoErro):         
        self.mensagem = "A posição que foi indicada já está ocupada. Teste outra."