# -*- coding: utf-8 -*-

class Drone:      

    def __init__(self,eixoX,eixoY,dirIni,sequComd,limtX,limtY):
        
        self.__comdSequ = sequComd   
        
        self.__posicaoX = eixoX
        self.__limiteX = limtX        
        self.__posicaoY = eixoY
        self.__limiteY = limtY 
        
        self.__direcao = dirIni
        self.__numFotos = 1
        self.__posVisitada = [[eixoX,eixoY]]
        
        self.__status = True
    
    #executa proxima sequComd 
    def executarProxCmd(self):
        
        # seleciona o proximo comando a ser executado
        proxCmd = self.__comdSequ[0]
        
        #deleta o comando selecionado        
        self.__comdSequ = self.__comdSequ[1:]
        
        
        if proxCmd == "E" or proxCmd == "D":
            self.girarDrone(proxCmd)
        else:
            self.moverDrone()
            posAtual = [self.__posicaoX,self.__posicaoY]            
            if posAtual not in self.__posVisitada:
                self.__posVisitada.append(posAtual)
                self.__numFotos += 1            
   
    ''' 
    Se o Drone esta virado para Norte e vira um angulo de 90º para a esquerda                
    entao ele ficaria virado para o Oeste
    Se o Drone esta virado para Norte e vira um angulo de 90º para a direita
    entao ele ficaria virado para Leste               
    Mesma linha de pensamento  é aplicada aos outros pontos cardeais
    '''
    #Gira o Drone dependendo se recebeu comando E ou D
    def girarDrone(self,comando):
              
        if comando == "E":                
                if self.__direcao == "N":
                    self.__direcao = "O"  
                    
                elif self.__direcao == "O":
                    self.__direcao = "S"      
                    
                elif self.__direcao == "S":
                    self.__direcao = "L"   
                    
                else:
                    self.__direcao = "N"
            
        elif comando == "D":
            if self.__direcao == "N":
                self.__direcao = "L" 
                    
            elif self.__direcao == "O":
                self.__direcao = "N" 
                    
            elif self.__direcao == "S":
                self.__direcao = "O"
                    
            else:
                self.__direcao = "S"        
      
            
    # dada a Posicao XY do Drone e sua Direcao Atual retorna a nova Posicao
    # caso o Drone tente sair da Grid ele ira fazer um giro de 180º
    def moverDrone(self):       
        
        if self.__direcao == "N":
            if(self.__posicaoY + 1) >= self.__limiteY:
                self.__direcao = "S"
            else:
                self.__posicaoY += 1
                
        elif self.__direcao == "S":
            if(self.__posicaoY - 1) < 0:
                self.__direcao = "N"
            else:
                self.__posicaoY -= 1
                
        elif self.__direcao == "L":
            if(self.__posicaoX + 1) >= self.__limiteX:
                self.__direcao = "O"
            else:
                self.__posicaoX += 1
                
        else:
            if(self.__posicaoX - 1) < 0:
                self.__direcao = "L"
            else:
                self.__posicaoX -= 1
        
        
        
                
    
    # diz se ainda ha comandos a serem executados pelo drone
    def atualizaStatus(self):
        if len(self.__comdSequ) > 0:
            return self.__status
        else:
            self.__status = False
            return self.__status
    
    
    '''
    Metodos "Getters" para serem usados nos testes
    '''
    def getDirecao(self):
        return self.__direcao
        
    def getPosX(self):
        return self.__posicaoX
        
    def getPosY(self):
        return self.__posicaoY        
        
    def getNumFotos(self):
        return self.__numFotos   
    
    
    
    

         
    
        