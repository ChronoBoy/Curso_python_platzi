import random
import time
import keyboard

def volver_jugar():
    contador = 10
    while contador > 0:
        contador -= 1 
        print (contador)
        time.sleep(1)


def run():
    pc_numero = random.randint(1,100)
    numero_usr = int(input("Introduce un numero del 1 al 100: "))
    contador_vidas = 5

    while numero_usr != pc_numero:
        if numero_usr < pc_numero:
            print('Mi numero es MAYOR')
        else:
            print('Mi numero es MENOR')
        contador_vidas -=1
        print("Te quedan: {} vidas".format(contador_vidas))    

        numero_usr = int(input("Introduce otro numero: "))
        
        if contador_vidas == 1:
            print('HAZ PERDIDO!')
            break 
    if numero_usr == pc_numero:
        print('GANASTE!') 

    print("CONTINUAR???: \n")    
    volver_jugar()


if __name__ == '__main__':
    run();