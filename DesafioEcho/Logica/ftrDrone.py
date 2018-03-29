# -*- coding: utf-8 -*-

from Logica.ctrlDrone import CtrlDrone
from Erros.erroCmdInvalido     import CmdInvalido
from Erros.erroCmdIncompleto   import CmdIncompleto
from Erros.erroDirecaoInvalida import DirInvalida
from Erros.erroPosForaGrid     import PosForaGrid
from Erros.erroPosOcupada      import PosOcupada
from Erros.erroPosInvalida     import PosInvalida


class FtrDrone():
    
    def __init__(self):
        
        self.meuControlador = None
        self.ptsCardeais = {"N":"Norte","S":"Sul","L":"Leste","O":"Oeste"}
        
    def inicializarControlador(self):
        
        print("Digite a largura e a altura da área que os drones devem fotografar: \n")
        grid = False
        while not grid:        
            largura = input("Largura:")
            altura  = input("Altura:")
            
            if largura.isdecimal() and altura.isdecimal():
                if int(largura) > 0 and int(altura) > 0:
                    grid = True
                    print(" \nFoi gerada uma area de ",int(largura)," x ", int(altura)," . \n")
            else:
                print("\n Altura ou Largura invalida para a criação de uma area. " + 
                      "Certifique-se de digitar apenas numeros maiores que 0. \n") 
        
        self.meuControlador = CtrlDrone(largura,altura)
        
    
    def inicializarDrones(self):
        
        maisDrones = True
        while maisDrones:
            
            print("Digite a sequencia de comandos para o Drone "
                  ,(self.meuControlador.getQtdDrones() + 1), " ou deixe vazio para sair:")
            
            seqCmd = input("Sequencia de Comandos:")
            if seqCmd != "":            
                try:
                    seqValidada = self.meuControlador.interpretarSeqCmd(seqCmd)
                    self.meuControlador.posicionarDrone(seqValidada)
                    print("\n O Drone ", self.meuControlador.getQtdDrones() ,
                          " foi posicionado nas coordenadas [",int(seqValidada[0]),",",int(seqValidada[1]),
                          "] virado para ", self.ptsCardeais.get(seqValidada[2]),
                          " com a sequencia de comandos \"", seqValidada[3],"\". \n")
                    
                except (CmdInvalido,CmdIncompleto,DirInvalida, PosForaGrid, PosOcupada,PosInvalida) as erro:
                    print("\n ",erro.mensagem, "\n")         
            else:
                maisDrones = False  
                
    
    def imprimirRelatorio(self):
        
        #Algum drone foi adicionado?
        if self.meuControlador.getQtdDrones() > 0:
            
            dronesAdicionados = self.meuControlador.getDrones()
        
            dronesAtv = True        
            while dronesAtv:  
                for drones in dronesAdicionados:
                    if drones.atualizaStatus():
                        drones.executarProxCmd()                        
                dronesAtv = self.meuControlador.verificarStatus()   
                        
    
            print("\n Relatorio:" )
            contador = 1
            for drones in dronesAdicionados:
                posFinal = [drones.getPosX(),drones.getPosY()]
                print("Drone ",contador, " :")
                print("     Posicao Final:       ", posFinal)
                print("     Direcao:             ", self.ptsCardeais.get(drones.getDirecao()))
                print("     Quantidade de fotos  ", drones.getNumFotos()  )
                contador += 1
        else:
            print(" \n Nenhum drone foi adicionado. Nao ha relatorio de atividades. \n")
           

   
            
    
