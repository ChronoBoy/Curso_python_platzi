
def dolares_a_pesos():
    try:
        dolares = float(input("Introduce el numero de dolares que deseas convertir a pesos: "))
        valor_dolar = 19.5
        pesos = round(float(dolares * valor_dolar))
        print ("Tus pesos son: $" + str(pesos))
           
    except:
        print("Debe de introducir una cantidad que sea numero")    


def pesos_a_dolares():
    pesos = float(input("Introduce el numero de pesos que deseas convertir a dolares: "))
    valor_dolar = 19.5
    dolares = round(float(pesos/valor_dolar),2)
    print("Tus dolares son: $" + str(dolares))

def run():
    while True: 
        try:
            respuesta = int(input("Introduce el numero de la accion que quieras hacer: \n"
            "1. Convertir dolares a pesos \n"
            "2. Convertir pesos a dolares \n"
            "3. salir \n"))

            if respuesta == 1:
                dolares_a_pesos()
                while True:
                    try:
                        salir = int(input("Quieres seguir convirtiendo dolares a pesos? \n"
                        "1. Si \n"
                        "2. Volver \n"))
                        if salir == 1:
                            dolares_a_pesos()
                        elif salir == 2:    
                            break
                    except:
                        print("Debe de introducir un numero")    
                            
            elif respuesta == 2:
                pesos_a_dolares()
                while True:
                    try:
                        salir = int(input("Quieres seguir convirtiendo pesos a dolares? \n"
                        "1. Si \n"
                        "2. Volver \n"))
                        if salir == 1:
                            pesos_a_dolares()
                        elif salir == 2:    
                            break
                    except:
                        print("Debe de introducir un numero")    
            
            elif respuesta >= 3:
                break
        except:
            print("Debe de introducir un numero")


if __name__ == '__main__':
    run()

        

    
    


   



   
