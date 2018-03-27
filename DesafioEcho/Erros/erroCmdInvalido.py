# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Comandos Invalidos no posicionamento dos Drones
class CmdInvalido(Exception):
    
    def __init__(self):         
        self.mensagem = "A sequencia de comendos é inválida. Comandos devem ser apenas E, D ou F"
