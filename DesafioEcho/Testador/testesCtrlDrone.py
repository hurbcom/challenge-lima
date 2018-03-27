# -*- coding: utf-8 -*-

from Logica.ctrlDrone import CtrlDrone
from Logica.ctrlDrone import validarSeqCmd
import unittest


class TestDrone(unittest.TestCase):
    
    def teste_PosOcupada(self):        
        controlador = CtrlDrone("10","10")
        controlador.posicionarDrone("0505NDEDEF")
        
        #a posicao 5,5 deve ser invalida ja que ha um drone la
        self.assertEqual("invalido",controlador.validarPosicao(5,5))      
    
    def teste_PosForaGrid(self):
        controlador = CtrlDrone("10","10")           
        
        #a posicao 15,15 deve ser invalida ja que esta fora da Grid
        self.assertEqual("invalido",controlador.validarPosicao(15,15))

    def teste_ValidarDirecao(self):       
        
        #validando os 4 pontos cardeais com a funcao Validar Sequencia de Comando
        self.assertEqual(validarSeqCmd("N","DDDD"),"valido")
        self.assertEqual(validarSeqCmd("S","DDDD"),"valido")
        self.assertEqual(validarSeqCmd("L","DDDD"),"valido")
        self.assertEqual(validarSeqCmd("O","DDDD"),"valido")       
        
        # ao passar uma direcao que NAO e um ponto cardeal, a funcao nao pode retornar "valido"
        self.assertIsNot(validarSeqCmd("D","DDDD"),"valido")
    
    # Comandos validos sao apenas cadeias feitas com D E F, qualquer outro caracter esta incorreto
    def teste_ValidarComandos(self):
        
        self.assertEqual(validarSeqCmd("O","DDDD"),"valido")
        self.assertEqual(validarSeqCmd("O","EEEE"),"valido")
        self.assertEqual(validarSeqCmd("O","FFFF"),"valido")
        self.assertEqual(validarSeqCmd("O","DEFE"),"valido")
        
        #qualquer outro caracter fora de D E F nao deve retornar "valido"
        self.assertIsNot(validarSeqCmd("O","ABCGHIJ"),"valido") 
  


    
    

if __name__ == "__main__":
    unittest.main()  
    