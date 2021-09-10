def aplicar_operaciones(num):
    operaciones = [abs,float]

    resultado = []

    for operacion in operaciones:
        resultado.append(operacion(num))
    return print(resultado)


def run():
    num = int(input("Introduce un numero: "))
    aplicar_operaciones(num)    

if __name__ == '__main__':
    run()