def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def linha(tam=42):
    return '=' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for c, item in enumerate(lista):
        print(f'\033[33m{c+1}\033[m - \033[34m{item}\033[m')
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc
