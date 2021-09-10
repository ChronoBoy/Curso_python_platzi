def run():

    palabra = input("Introduce una palabra: ")
    for letra in palabra:
        if letra == 'o':
            continue
        print (letra)
if __name__ == '__main__':
    run()        