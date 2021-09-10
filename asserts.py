def son_palabras(lista):
    
    palabras_en_lista = []
    for palabra in lista:
        try:
            assert type(palabra) == str,f'{palabra} no es una palabra'
            palabras_en_lista.append(palabra) 
        except AssertionError as e:
            print(e)
    return palabras_en_lista

def run():
    lista = ['Alvaro', 'Astrid', 4,0.5,True]
    print('Los elementos dentro de la lista que son palabras son: ',son_palabras(lista))             
               


if __name__ == '__main__':
    run()
