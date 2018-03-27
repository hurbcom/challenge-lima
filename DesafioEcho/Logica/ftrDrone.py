# -*- coding: utf-8 -*-
from ctrlDrone import CtrlDrone
from Erros.erroCmdInvalido     import CmdInvalido
from Erros.erroCmdIncompleto   import CmdIncompleto
from Erros.erroDirecaoInvalida import DirInvalida
from Erros.erroPosForaGrid     import PosForaGrid
from Erros.erroPosOcupada      import PosOcupada
from Erros.erroPosInvalida     import PosInvalida

def main():
    
    print("Digite a largura e a altura da área que os drones devem fotografar:")
    grid = False
    while not grid:
        
        largura = input("Largura:")
        altura  = input("Altura:")
        
        if largura.isdecimal() and altura.isdecimal():
            if int(largura) > 0 and int(altura) > 0:
                grid = True
        else:
            print("Altura ou Largura inválidas para a criação de uma área. Certifique-se de digitar apenas números maiores de 0.") 
    
    controle = CtrlDrone(largura,altura)
         
    
    maisDrones = True
    while maisDrones:
        
        print("Digite a sequencia de comandos para o Drone ",(controle.getQtdDrones() + 1), " ou deixe vazio para sair:")
        seqCmd = input("Sequencia de Comandos:")
        if seqCmd != "":            
            try:
                seqValidada = controle.interpretarSeqCmd(seqCmd)
                controle.posicionarDrone(seqValidada)
                print("\n O Drone ", controle.getQtdDrones() ," foi posicionado nas coordenadas [",seqValidada[0],",",seqValidada[1],"] . \n")
                
            except (CmdInvalido,CmdIncompleto,DirInvalida, PosForaGrid, PosOcupada,PosInvalida) as erro:
                print(erro.mensagem)          
            
            
        else:
            maisDrones = False    
   
    
    #Algum drone foi adicionado?
    if controle.getQtdDrones() > 0:
        
        dronesAdicionados = controle.getDrones()
    
        dronesAtv = True        
        while dronesAtv:  
            for drones in dronesAdicionados:
                if drones.atualizaStatus():
                    drones.executarProxCmd()                        
            dronesAtv = controle.verificarStatus()   
                    

        print("\n Relatorio:" )
        contador = 1
        for drones in dronesAdicionados:
            posFinal = [drones.getPosX(),drones.getPosY()]
            print("Drone ",contador, " :")
            print("     Posição Final:       ", posFinal)
            print("     Direção:             ", drones.getDirecao())
            print("     Quantidade de fotos  ", drones.getNumFotos()  )
            contador += 1
                
            
            
        



if __name__ == "__main__":
    main()