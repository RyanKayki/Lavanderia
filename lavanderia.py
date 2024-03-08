import os

custo_total = 0

while True:
    os.system('cls')
    print("-Bem vindo a lavanderia-")
    print("\n Tabela de Preços")
    print("\n 1 - Camiseta - R$ 2,00 (kg)\n 2 - Calça - R$ 3,50 (kg)\n 3 - Vestido - R$ 4,00 (kg)")

    try:
        tipo = int(input("Por favor, insira o que deseja lavar: "))
        peso = float(input("Agora, insira quantos (kg) de roupa deseja lavar: "))

        if tipo == 1:
            total = peso * 2.00
        elif tipo == 2:
            total = peso * 3.50
        else:
            total = peso * 4.00

        custo_total += total

        print("\n Roupas - Preço: R$ {:.2f}".format(custo_total))


        again = input("\nDeseja fazer outro cálculo? (s/n): ")
        if again.upper() == 'S':
            continue
        else:
            break

    except ValueError:
        print("Por favor, insira um número válido.")
        continue

