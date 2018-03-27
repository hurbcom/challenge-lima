# -*- coding: utf-8 -*-

from drone import Drone
from Erros.erroCmdInvalido     import CmdInvalido
from Erros.erroDirecaoInvalida import DirInvalida
from Erros.erroPosForaGrid     import PosForaGrid
from Erros.erroPosOcupada      import PosOcupada
from Erros.erroPosInvalida     import PosInvalida
from Erros.erroCmdIncompleto   import CmdIncompleto

class CtrlDrone:
    
    def __init__(self,largura,altura):
        self.__alturaGrid = altura
        self.__larguraGrid = largura
        self.__dronesAtuais = []
        self.__posIniDrones = []    
   
    
    #dada uma Sequencia de Comandos posiciona um Drone
    def posicionarDrone(self,seqCmd):         
             
        posNovoDrone = [int(seqCmd[0]),int(seqCmd[1])]  
        
        novoDrone = Drone(int(seqCmd[0]),int(seqCmd[1]),seqCmd[2],seqCmd[3],int(self.__larguraGrid),int(self.__alturaGrid))  
        
        self.__posIniDrones.append(posNovoDrone)
        self.__dronesAtuais.append(novoDrone)  
      
    
    #metodo utilizado para interpretar uma sequencia de comandos recebida
    #ela recebe a sequencia e retorna uma lista com os campos separados em:
    #Posicao Eixo X, Posicao Eixo Y, Direcao do Drone, Comandos a serem executados
    def interpretarSeqCmd(self,sequenciaComd):
            
            ''' 
            Dependendo da altura e largura da Grid a quantidade de digitos para representar
            a posicaoX e posicaoY do drone pode variar
            '''
            
            posicaoX = sequenciaComd[0:len(self.__larguraGrid)]
            #deletando os digitos já utilizados
            sequenciaComd = sequenciaComd[len(self.__larguraGrid):]
            
            if len(sequenciaComd) == 0:
                raise CmdIncompleto
            
            posicaoY = sequenciaComd[0:len(self.__alturaGrid)]
            sequenciaComd = sequenciaComd[len(self.__alturaGrid):]
            
            self.validarPosicao(posicaoX,posicaoY)
            
            if len(sequenciaComd) == 0:
                raise CmdIncompleto
                
            #uma vez removida as coordenadas do Drone o primeiro digito da String sera a Direcao do drone
            direcao = sequenciaComd[0]
            sequenciaComd = sequenciaComd[1:]
            
            if len(sequenciaComd) == 0:
                raise CmdIncompleto
                
            sequenciaComd = sequenciaComd[0:]            
            
            self.validarSeqCmd(direcao,sequenciaComd)            
           
            return [posicaoX,posicaoY,direcao,sequenciaComd]
            
                
    
    
    #testa uma Sequencia de Comandos ja interpretada para saber se todos caracteres estão corretos
    def validarSeqCmd(self,direcao,sequenciaComd):
        
        if direcao != "N" and direcao != "S" and direcao != "L" and direcao != "O":
            raise DirInvalida
           
        for caracter in sequenciaComd:
            if caracter != "D" and caracter != "F" and caracter != "E":
                raise CmdInvalido
        
        return "valido"
    
    #verifica se uma Posicao XY ja esta com um Drone ou se esta fora da Grid
    def validarPosicao(self,posX,posY):
        
        if posX.isdecimal() and posY.isdecimal():            
            posicao = [int(posX),int(posY)]
            
            if int(posX) >= int(self.__larguraGrid) or int(posY) >= int(self.__alturaGrid):
                raise PosForaGrid
                  
            if posicao not in self.__posIniDrones:
                return "valido"
            else:
                raise PosOcupada
        else:
            raise PosInvalida
    
    # verifica se ainda ha algum Drone com Status True
    def verificarStatus(self):
        
        statusGeral = False
        for drone in self.__dronesAtuais:
            statusGeral = drone.atualizaStatus()
        
        return statusGeral
            
            
    '''
    Metodos "Getters" para serem usados nos testes
    '''
    def getAlturaGrid(self):
        return self.__alturaGrid
    
    def getLarguraGrid(self):
        return self.__larguraGrid
    
    def getDrones(self):
        return self.__dronesAtuais
    
    def getQtdDrones(self):
        return len(self.__dronesAtuais)
    
     
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        