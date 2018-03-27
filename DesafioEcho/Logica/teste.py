
from ctrlDrone import CtrlDrone

def main():
    
    teste = CtrlDrone("10","10")
    
    seqValidada = teste.interpretarSeqCmd("0505NDEDEF")
    teste.posicionarDrone(seqValidada)
    
    status = teste.verificarStatus()
    drone = teste.getDrones()
    while status:
        for drones in drone:
            drones.executarProxCmd()
        status = teste.verificarStatus()
            
        
    print("acabou")


    
if __name__ == "__main__":
    main()