# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Comandos Invalidos no posicionamento dos Drones
class CmdInvalido(Exception):
    
    def __init__(self):         
        self.mensagem = "A sequencia de comandos possui caracteres invalidos. Comandos devem possuir apenas os caracteres E, D ou F"
