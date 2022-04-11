def pesquisa_binaria(list, target):
    primeiro = 0
    ultimo = len(list) - 1

    while primeiro <= ultimo:
        ponto_do_meio = (primeiro + ultimo)// 2
        if list[ponto_do_meio] == target:
            return ponto_do_meio
        elif list[ponto_do_meio] < primeiro:
            ultimo = ponto_do_meio + 1
        else:
            primeiro = ponto_do_meio - 1
    return None 


def verificar(index):
    if index is not None:
        print("O número do índice é: ", index)
    else:
        print("O número do índice não existe")
        
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = pesquisa_binaria(numeros, 8)

verificar(resultado)