def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        return True
    else: 
        return False    


def run():
    palabra = input("Introduce una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('SI es palindromo')
    else:
        print('NO es palindromo')    


if __name__ == '__main__':
    run()
   