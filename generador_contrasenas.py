import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D','E','F','G']
    minusculas = ['a','b','c','d','e','f','g']
    caracteres = ['!','@','#','$','%','&','*']
    numeros = ['1','2','3','4','5','6','7','8','9','0'] 

    lista_caracteres = mayusculas + minusculas + caracteres + numeros

    contrasena = []
 
    for i in range(15):
        caracter_random = random.choice(lista_caracteres)
        contrasena.append(caracter_random)
    contrasena = ''.join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("tu contrasena es: " + contrasena)

if __name__ == '__main__':
    run()