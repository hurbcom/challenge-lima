# -*- coding: utf-8 -*-

#Essa Exception foi criada para tratar os problemas de Direcao Invalida
class DirInvalida(Exception):
    
    def __init__(self):         
        self.mensagem = "A direcao indicada para o drone nao e um Ponto Cardeal. As direcoes validas sao N, S, L e O"
