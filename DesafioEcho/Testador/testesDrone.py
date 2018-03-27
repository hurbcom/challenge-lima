# -*- coding: utf-8 -*-

import unittest
from Logica.drone import Drone


class TestDrone(unittest.TestCase):
    
    def test_MoverDrone(self):   
        
        #ao se movimentar para Oeste a Posicao X deve reduzir em 1, mas a Direcao e Posicao Y nao devem mudar  
        #portanto : (9,10,O)        
        droneTeste = Drone(10,10,"O","FFFF",15,15)      
        droneTeste.moverDrone()             
        self.assertEqual([droneTeste.getPosX(),droneTeste.getPosY(),droneTeste.getDirecao()] , [9,10,"O"])        
       
    
    def test_SairDaGrid(self):
        
        #ao tentar sair da Grid o Drone faz um giro de 180º
        #se esta virado para Leste ele permanece na mesma posicao, mas virado para Oeste
        #portanto: (14,14,O)
        droneTeste = Drone(14,14,"L","FFFF",15,15)
        droneTeste.moverDrone()
        self.assertEqual([droneTeste.getPosX(),droneTeste.getPosY(),droneTeste.getDirecao()] , [14,14,"O"])
    
    def test_GirarDrone(self):
        
        droneTeste = Drone(14,14,"L","DDDD",15,15)
        
        #se o Drone esta virado para Leste e recebe o comando para girar para Direita sua direcao entao muda para Sul
        droneTeste.girarDrone("D")
        self.assertEqual(droneTeste.getDirecao(),"S")
        
        #se o Drone esta virado para Sul e recebe o comando para girar para Direita sua direcao entao muda para Oeste
        droneTeste.girarDrone("D")
        self.assertEqual(droneTeste.getDirecao(),"O")
        
        #se o Drone esta virado para Oeste e recebe o comando para girar para Direita sua direcao entao muda para Norte
        droneTeste.girarDrone("D")
        self.assertEqual(droneTeste.getDirecao(),"N")
        
        #se o Drone esta virado para Norte e recebe o comando para girar para Direita sua direcao entao muda para Leste
        droneTeste.girarDrone("D")
        self.assertEqual(droneTeste.getDirecao(),"L")

    


if __name__ == "__main__":
    unittest.main() 