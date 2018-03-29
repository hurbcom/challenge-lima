# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Posicoes Ocupadas
class PosOcupada(Exception):
    
    def __init__(self):         
        self.mensagem = "A coordenada indicada ja está ocupada. Informe outra coordenada."