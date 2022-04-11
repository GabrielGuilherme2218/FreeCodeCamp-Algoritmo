import numbers

def pesquisa_linear(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
    

def verificar(index):
    if index is not None:
        print("O número do Índice: ", index)
    else:
        print("O número do índice não existe")

numeros = [0,1,2,3,4,5,6,7,8,9,10]

resultado = pesquisa_linear(numeros, 8)

verificar(resultado)