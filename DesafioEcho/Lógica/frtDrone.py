# -*- coding: utf-8 -*-

from ctrlDrone import CtrlDrone

def main():
    
    print("Digite a largura e a altura da área que os drones devem fotografar:")
    largura = input("Largura:"))
    altura  = input("Altura:"))
    
    controle = CtrlDrone(largura,altura)
         
    
    maisDrones = True
    while maisDrones:
        print("Deseja adicionar um novo Drone?")
        print("S para Sim e N para Não")
        addDrone = input("S / N ?")
        print(addDrone)
        if addDrone == "N":
            maisDrones = False
            continue
            
        print("batata")
    
    



if __name__ == "__main__":
    main()