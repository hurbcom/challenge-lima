# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Posicoes com letras
class CmdIncompleto(Exception):
    
    def __init__(self):         
        self.mensagem = "A sequencia de comandos esta incompleta. Digite novamente."
