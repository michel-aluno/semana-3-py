import utilidades


# Conversor de temperatura
temperatura = 30
resultado = utilidades.converter_temperatura(temperatura)

print("Temperatura em Fahrenheit:", resultado)


# Validador de senha
senha = "python123"

if utilidades.validar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")


# Caixa com *precos
total = utilidades.calcular_caixa(10, 20, 15, 5)

print("Total da compra:", total)


# Ficha do aluno com **dados
aluno = utilidades.ficha_aluno(
    nome="Michel",
    idade=18,
    curso="Engenharia de Software"
)

print("Ficha do aluno:", aluno)


# Lista segura
lista_original = ["Python", "HTML", "CSS"]

nova_lista = utilidades.adicionar_item(lista_original, "JavaScript")

print("Lista original:", lista_original)
print("Nova lista:", nova_lista)
