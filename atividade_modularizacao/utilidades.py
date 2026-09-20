def converter_temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def validar_senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False


def calcular_caixa(*precos):
    total = sum(precos)
    return total


def ficha_aluno(**dados):
    return dados


def adicionar_item(lista, item):
    nova_lista = lista.copy()
    nova_lista.append(item)
    return nova_lista
