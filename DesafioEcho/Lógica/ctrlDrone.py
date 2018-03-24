# -*- coding: utf-8 -*-

from drone import Drone

class CtrlDrone:
    
    def __init__(self,largura,altura):
        self.alturaGrid = altura
        self.larguraGrid = largura
        self.dronesAtuais = []
        self.posIniDrones = []
        
    def posicionarDrone(self,sequenciaComd):    
        
        ''' 
        Dependendo da altura e largura da Grid a quantidade de digitos para representar
        a posicaoX e posicaoY do drone pode variar
        '''
        
        posicaoX = sequenciaComd[0:len(self.larguraGrid)]
        #deletando os digitos já utilizados
        sequenciaComd = sequenciaComd[len(self.larguraGrid):]
        
        posicaoY = sequenciaComd[0:len(self.alturaGrid)]
        sequenciaComd = sequenciaComd[len(self.alturaGrid):]
        
        #uma vez removida as coordenadas do Drone o primeiro digito da String sera a Direcao do drone
        direcao = sequenciaComd[0]
        sequenciaComd = sequenciaComd[1:]
     
        posNovoDrone = [int(posicaoX),int(posicaoY)]       
        novoDrone = Drone(sequenciaComd,int(posicaoX),int(posicaoY),int(self.larguraGrid),int(self.alturaGrid),direcao)  
        
        self.posIniDrones.append(posNovoDrone)
        self.dronesAtuais.append(novoDrone)
        
    
        
        
        
        
        
        
        
        
        
        
        