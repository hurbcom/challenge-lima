# -*- coding: utf-8 -*-

class Drone:      
    
    def __init__(self,sequComd,eixoX,eixoY,limtX,limtY,dirIni):
        
        self.comdSequ = sequComd   
        
        self.posicaoX = eixoX
        self.limiteX = limtX        
        self.posicaoY = eixoY
        self.limiteY = limtY 
        
        self.direcao = dirIni
        self.numFotos = 1
        self.posVisitada = [[eixoX,eixoY]]
        
        self.status = True
    
    def movimentarDrone(self):
        
        # seleciona o proximo comando a ser executado
        proxCmd = self.comdSequ[0]
        
        #deleta o comando selecionado        
        self.comdSequ = self.comdSequ[1:]
        
        if proxCmd == "E":
            ''' 
            Se o Drone esta virado para Norte e vira um angulo de 90º para a esquerda                
            entao ele ficaria virado para o Oeste                
            Mesma linha de pensamento  é aplicada aos outros pontos cardeais
            '''
            if self.direcao == "N":
                self.direcao = "O"                
            elif self.direcao == "O":
                self.direcao = "S"                
            elif self.direcao == "S":
                self.direcao = "L"                
            else:
                self.direcao = "N"
        
        elif proxCmd == "D":
            if self.direcao == "N":
                self.direcao = "L"                
            elif self.direcao == "O":
                self.direcao = "N"                
            elif self.direcao == "S":
                self.direcao = "O"
            else:
                self.direcao = "S"
        
        
       # Se o Drone for sair da Grid em vez disso ele faz um giro de 180º
        elif proxCmd == "F":
            if self.direcao == "N":
                self.posicaoY += 1     
                # o drone esta prestes a sair da grid?
                if self.posicaoY >= self.limiteY:
                    self.posicaoY -= 1
                    self.direcao = "S"
                
                # o drone ja esteve nessa posicao antes? se nao tiver, tira foto
                posDrone = [self.posicaoX,self.posicaoY]
                if posDrone not in self.posVisitada:
                    self.numFotos += 1
                    self.posVisitada.append(posDrone)
                    
            elif self.direcao == "S":
                self.posicaoY -= 1
                if self.posicaoY < 0:
                    self.posicaoY += 1
                    self.direcao = "N"
                posDrone = [self.posicaoX,self.posicaoY]
                if posDrone not in self.posVisitada:
                    self.numFotos += 1
                    self.posVisitada.append(posDrone)
                    
            elif self.direcao == "O":
                self.posicaoX -= 1
                if self.posicaoX < 0:
                    self.posicaoX += 1
                    self.direcao = "L"  
                posDrone = [self.posicaoX,self.posicaoY]
                if posDrone not in self.posVisitada:
                    self.numFotos += 1
                    self.posVisitada.append(posDrone)
                    
            else:
                self.posicaoX += 1
                if self.posicaoX >= self.limiteX:
                    self.posicaoX -= 1
                    self.direcao = "O"
                posDrone = [self.posicaoX,self.posicaoY]
                if posDrone not in self.posVisitada:
                    self.numFotos += 1  
                    self.posVisitada.append(posDrone)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
        
        