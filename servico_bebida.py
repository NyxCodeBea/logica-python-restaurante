def servico_bebida(pedido_bebida, mesa_solicitante):
        print(f"--- Processando pedido para a Mesa {mesa_solicitante} ---")

        if(pedido_bebida == "Água"):
            print("Colocando Água")
        elif("Refrigerante" in pedido_bebida):
            print(f"Colocando {pedido_bebida}")
        else:
            print(f"Colocando {pedido_bebida}")
        print(f"Levando o {pedido_bebida} para a mesa {mesa_solicitante}\n")

cardapio = {
     1: "Água",
     2: "Refrigerante Coca-Cola",
     3: "Refrigerante Fanta Laranja",
     4: "Refrigerante Guaraná",
     5: "Suco de Laranja",
     6: "Suco de Maracujá",
     7: "Suco de Uva"
}

pedidos_pendentes = [] 
pedido_bebida = 0
mesa_solicitante = 0

print("Bem-vindo ao Sistema do Garçom Robô!")
print("As bebidas disponiveis são Água, Sucos e Refrigerantes.")
print(cardapio)

while True:
    pedido = input("Deseja realizar um pedido? S (sim) ou N (não): ")
    if(pedido == "N"):
        print("Fim da coleta de pedidos! Enviando para a cozinha...\n")
        break
    else:
        pedido_bebida = int(input("Digite o código da bebebida desejada: "))
        mesa_solicitante = int(input("Digite o número da mesa: "))

        nome_da_bebida = cardapio[pedido_bebida]

        ticket = [nome_da_bebida, mesa_solicitante]
        pedidos_pendentes.append(ticket)
        print("Pedido anotado!")

print("--- INICIANDO SERVIÇO ---")
for ticket in pedidos_pendentes:
    servico_bebida(ticket[0], ticket[1])

print("Todos os pedidos foram entregues. Bom trabalho!")
