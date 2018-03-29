# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Posicoes com letras
class PosInvalida(Exception):
    
    def __init__(self):         
        self.mensagem = "A posicao inficada possui caracteres invalidos ou está em um formato incorreto."
