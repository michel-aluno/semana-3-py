
from operacoes import somar, subtrair, multiplicar, dividir

def menu():
    print("\n=== CALCULADORA PYTHON ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

def executar():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando a calculadora. Até logo!")
            break

        if opcao in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == "1":
                    resultado = somar(num1, num2)
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                elif opcao == "2":
                    resultado = subtrair(num1, num2)
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                elif opcao == "3":
                    resultado = multiplicar(num1, num2)
                    print(f"Resultado: {num1} * {num2} = {resultado}")
                elif opcao == "4":
                    resultado = dividir(num1, num2)
                    print(f"Resultado: {num1} / {num2} = {resultado}")

            except ValueError as erro:
                # Captura tanto entrada de texto inválida quanto a divisão por zero lançada pela função
                print(f"\n[ATENÇÃO] {erro}")
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    executar()