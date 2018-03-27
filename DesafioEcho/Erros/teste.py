# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 18:34:48 2018

@author: Thiago
"""
from Erros.erroCmdInvalido import CmdInvalido

def main():
    '''
    a = 12
    b = 13
    try:        
        
        if a != b:
            raise CmdInvalido
        else:
            print("ok")
    except CmdInvalido as erro:
        print(erro.mensagem)
    '''
    
    a = input("oi")
    
    if a ==  "":
        print("vazzio")
    else:
        print(a)
                
            
    
if __name__ == "__main__":
    main()