# ==========================
# CARDÁPIO
# ==========================

# Porções
batata_canoa = 35
batata_palito = 43
iscas_de_frango = 50
peixe_empanado = 60

# Bebidas
refrigerante = 15
suco_natural = 12
agua = 6

# ==========================
# COMANDAS
# ==========================

numeros = []
clientes = []
mesas = []
totais = []
status = []

pedidos = []

numero_comanda = 1

while True:

    print("\n=== RESTAURANTE ===")
    print("1 - Fazer pedido")
    print("2 - Abrir comanda")
    print("3 - Fechar comanda")
    print("4 - Visualizar comanda")
    print("5 - Aplicar desconto/gorjeta")
    print("6 - Relatório da noite")
    print("7 - Sair")

    try:
      restaurante = int(input("Escolha uma opção: "))
    except ValueError:
      print("Digite apenas números!")
      continue

    # ==========================
    # ABRIR COMANDA
    # ==========================

    if restaurante == 2:

        cliente = input("Nome do cliente: ")
        mesa = int(input("Número da mesa: "))

        numeros.append(numero_comanda)
        clientes.append(cliente)
        mesas.append(mesa)
        totais.append(0)
        status.append("Aberta")
        
        pedidos.append([]) 

        print(f"Comanda {numero_comanda} aberta!")

        numero_comanda += 1

    # ==========================
    # FAZER PEDIDO
    # ==========================

    elif restaurante == 1:

        numero = int(input("Número da comanda: "))

        if numero in numeros:

            indice = numeros.index(numero)

            if status[indice] == "Fechada":

                print("Comanda fechada!")

            else:

                print("=" * 40)
                print("CARDÁPIO")
                print("=" * 40)

                print("\nPORÇÕES")
                print("1 - Batata Canoa .......... R$ 35.00")
                print("2 - Batata Palito ......... R$ 43.00")
                print("3 - Iscas de Frango ....... R$ 50.00")
                print("4 - Peixe Empanado ........ R$ 60.00")

                porcao = int(input("Escolha uma porção: "))

                print("\nBEBIDAS")
                print("0 - Sem bebida")
                print("5 - Refrigerante .......... R$ 15.00")
                print("6 - Suco Natural .......... R$ 12.00")
                print("7 - Água .................. R$ 6.00")

                bebida = int(input("Escolha uma bebida: "))

                if porcao == 1:
                    valor_porcao = 35
                elif porcao == 2:
                    valor_porcao = 43
                elif porcao == 3:
                    valor_porcao = 50
                elif porcao == 4:
                    valor_porcao = 60
                else:
                    valor_porcao = 0

                if bebida == 0:
                    valor_bebida = 0
                elif bebida == 5:
                    valor_bebida = 15
                elif bebida == 6:
                    valor_bebida = 12
                elif bebida == 7:
                    valor_bebida = 6
                else:
                    valor_bebida = 0

                total_pedido = valor_porcao + valor_bebida

                descricao = ""

                if porcao == 1:
                   descricao += "Batata Canoa"

                elif porcao == 2:
                   descricao += "Batata Palito"

                elif porcao == 3:
                   descricao += "Iscas de Frango"

                elif porcao == 4:
                  descricao += "Peixe Empanado"


                if bebida == 5:
                  descricao += " + Refrigerante"

                elif bebida == 6:
                  descricao += " + Suco Natural"

                elif bebida == 7:
                  descricao += " + Água"

                pedidos[indice].append(descricao)

                totais[indice] += total_pedido

                print(f"Pedido adicionado!")
                print(f"Valor do pedido: R$ {total_pedido:.2f}")
                print(f"Total da comanda: R$ {totais[indice]:.2f}")

        else:
            print("Comanda não encontrada!")

    # ==========================
    # FECHAR COMANDA
    # ==========================

    elif restaurante == 3:

        numero = int(input("Número da comanda: "))

        if numero in numeros:

            indice = numeros.index(numero)

            print("\n===== RESUMO =====")
            print(f"Cliente: {clientes[indice]}")
            print(f"Mesa: {mesas[indice]}")
            print(f"Total: R$ {totais[indice]:.2f}")

            status[indice] = "Fechada"

            print("Comanda fechada!")
            print("\nPedidos:")

            for pedido in pedidos[indice]:
             print("-", pedido)
        else:
            print("Comanda não encontrada!")

    # ==========================
    # VISUALIZAR COMANDA
    # ==========================

    elif restaurante == 4:
        numero = int(input("Número da comanda: "))

        if numero in numeros:

           indice = numeros.index(numero)

           print(f"Cliente: {clientes[indice]}")
           print(f"Mesa: {mesas[indice]}")
           print(f"Status: {status[indice]}")

           print("\nPedidos:")

           for pedido in pedidos[indice]:
               print("-", pedido)

           print(f"\nTotal: R$ {totais[indice]:.2f}")
  
        else:
          print("Comanda não encontrada!")    


    # ==========================
    # DESCONTO OU GORJETA
    # ==========================

    elif restaurante == 5:

        numero = int(input("Número da comanda: "))

        if numero in numeros:

            indice = numeros.index(numero) 
            
            if status[indice] == "Fechada":
             print("Comanda já fechada!")
             continue

            print("1 - Desconto")
            print("2 - Gorjeta")

            escolha = int(input("Escolha: "))
            percentual = float(input("Percentual: "))

            valor_antigo = totais[indice]

            if escolha == 1:

                if percentual >= 100:
                    print("Desconto inválido!")

                else:

                    desconto = valor_antigo * percentual / 100
                    totais[indice] -= desconto

                    print(f"Valor antigo: R$ {valor_antigo:.2f}")
                    print(f"Novo valor: R$ {totais[indice]:.2f}")

            elif escolha == 2:

                gorjeta = valor_antigo * percentual / 100
                totais[indice] += gorjeta

                print(f"Valor antigo: R$ {valor_antigo:.2f}")
                print(f"Novo valor: R$ {totais[indice]:.2f}")

        else:
            print("Comanda não encontrada!")

    # ==========================
    # RELATÓRIO
    # ==========================

    elif restaurante == 6:

        faturamento = 0
        quantidade = 0

        print("\n===== RELATÓRIO =====")

        for i in range(len(numeros)):

            if status[i] == "Fechada":

                print(
                    f"Comanda {numeros[i]} - "
                    f"{clientes[i]} - "
                    f"R$ {totais[i]:.2f}"
                )

                faturamento += totais[i]
                quantidade += 1

        print(f"\nFaturamento total: R$ {faturamento:.2f}")

        if quantidade > 0:

            media = faturamento / quantidade

            print(f"Média por comanda: R$ {media:.2f}")

        else:

            print("Nenhuma comanda fechada.")

    # ==========================
    # SAIR
    # ==========================

    elif restaurante == 7:

        print("Sistema encerrado!")
        break

    else:

        print("Opção inválida!")