# --- 1. Configurações e Dados ---

cardapio_bebidas = {
     1: "Água",
     2: "Refrigerante Coca-Cola",
     3: "Refrigerante Fanta Laranja",
     4: "Refrigerante Guaraná",
     5: "Suco de Laranja",
     6: "Suco de Maracujá",
     7: "Suco de Uva"
}

cardapio_preco = {
     1: 2.50,
     2: 3.50,
     3: 3.00,
     4: 3.00,
     5: 6.00,
     6: 7.00,
     7: 5.00
}

pedidos_pendentes = [] 
pedido_bebida = 0
mesa_solicitante = 0
faturamento_total = 0

# --- 2. O Manual do Robô (Funções) ---

def servico_bebida(pedido_bebida, mesa_solicitante):
        print(f"--- Processando pedido para a Mesa {mesa_solicitante} ---")

        if(pedido_bebida == "Água"):
            print("Colocando Água")
        elif("Refrigerante" in pedido_bebida):
            print(f"Colocando {pedido_bebida}")
        else:
            print(f"Colocando {pedido_bebida}")

        print(f"Levando o {pedido_bebida} para a mesa {mesa_solicitante}\n")

# --- 3. Abertura do Restaurante (Coleta) ---

print("Bem-vindo ao Sistema do Garçom Robô!")
print("As bebidas disponiveis são Água, Sucos e Refrigerantes.")
print(cardapio_bebidas)

while True:
    pedido = input("Deseja realizar um pedido? S (sim) ou N (não): ")
    if(pedido.upper() == "N"): # O .upper() garante que 'n' minúsculo também funcione
        print("Fim da coleta de pedidos! Enviando para a cozinha...\n")
        break
    else:
        # Pergunta o código
        try:
            # ⚠️ ZONA DE PERIGO
            # Aqui colocamos os inputs que podem dar erro
            pedido_bebida = int(input("Digite o código da bebebida desejada: "))
            mesa_solicitante = int(input("Digite o número da mesa: "))

            if pedido_bebida in cardapio_bebidas:
                # Traduz Código -> Nome e Preço
                nome_da_bebida = cardapio_bebidas[pedido_bebida]
                valor_da_bebida = cardapio_preco[pedido_bebida]

                # Cria o Ticket Completo
                ticket = [nome_da_bebida, mesa_solicitante, valor_da_bebida]
                pedidos_pendentes.append(ticket)
                print(f"Pedido de {nome_da_bebida} anotado! Valor: R$ {valor_da_bebida:.2f}")
            else:
                print("Ops! Bebida não encontrada.")   

        except ValueError:
            # 🛡️ ZONA DE SEGURANÇA (PLANO B)
            # O código cai aqui se o usuário digitar letras
            print("Ops! Você precisa digitar um número válido.")      
        
# --- 4. A Cozinha (Execução) ---

print("--- INICIANDO SERVIÇO ---")
for ticket in pedidos_pendentes:
    servico_bebida(ticket[0], ticket[1]) # ticket[0] = Nome, ticket[1] = Mesa

# --- 5. O Caixa (Fechamento) ---

print("--- FECHAMENTO DO CAIXA ---")
for ticket in pedidos_pendentes:
     faturamento_total += ticket[2]

print(f"Total faturado no serviço: R$ {faturamento_total:.2f}")
print("Todos os pedidos foram entregues. Bom trabalho, Robô!!")
