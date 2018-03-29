# -*- coding: utf-8 -*-
import sys 
import os  
sys.path.append(os.getcwd() + "/Erros")  
sys.path.append(os.getcwd() + "/Logica")  

from Logica.ftrDrone import FtrDrone

def main():
    
    minhaFronteira = FtrDrone()
    
    minhaFronteira.inicializarControlador()
    minhaFronteira.inicializarDrones()
    minhaFronteira.imprimirRelatorio()           
    
if __name__ == "__main__":
    main()                