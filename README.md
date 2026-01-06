# 🤖 Robô Garçom - Sistema de Pedidos

Um sistema de gerenciamento de pedidos para restaurantes que roda no terminal. O projeto simula o atendimento de um garçom, desde a coleta do pedido até o envio para a cozinha.

## 🚀 Sobre o Projeto
Este projeto foi desenvolvido como parte dos meus estudos em Lógica de Programação com Python. O foco foi aplicar estruturas de dados fundamentais para resolver um problema real.

**O que eu aprendi/pratiquei:**
* **Listas e Listas de Listas:** Para gerenciar a fila de pedidos.
* **Dicionários:** Para criar o cardápio e sistema de preços (em desenvolvimento).
* **Laços de Repetição (While/For):** Para manter o sistema rodando e processar a fila.
* **Funções:** Para organizar a lógica de serviço e evitar repetição de código.
* **Tratamento de Dados:** Conversão de inputs e manipulação de Strings.

## 🛠️ Como usar
1. Clone o repositório.
2. Execute o arquivo principal.
3. Siga as instruções no terminal para fazer os pedidos das mesas.

---
*Projeto desenvolvido com mentoria assistida por IA, focando em aprendizado ativo e lógica de programação.*
---

🧠 Metodologia de Estudo
Aprendizado Adaptativo: Identificação do perfil de aprendizado focado em narrativas e lógica antes da sintaxe.

Gamificação: Desenvolvimento guiado através de storytelling (o cenário do "Robô Garçom").

Desafio 10 Dias: Foco intensivo em lógica de programação (Dia 1/10 concluído).

⚙️ Funcionalidades Implementadas (Dia 1)
O sistema já é capaz de realizar o ciclo completo de atendimento:

Cardápio Digital: Uso de Dicionários (dict) para armazenar produtos e preços, permitindo busca rápida.

Interação com Usuário: Coleta dinâmica de pedidos e número da mesa via terminal.

Validação e Segurança: Implementação de try/except para prevenir falhas se o usuário digitar letras em vez de números, além de verificação se o item existe no menu.

Gestão de Pedidos: Armazenamento dos pedidos em uma Lista de Listas (Tickets), contendo nome, mesa e valor individual.

Automação do Serviço: Loop (while) para atendimento contínuo até que o operador decida encerrar.

Relatório Financeiro: Cálculo automático do faturamento total do dia ao fechar o caixa (iteração com for e acumuladores).

---

## 📅 Atualização: Dia 2 - A Memória do Robô (Persistência de Dados)

Nesta etapa, focamos em resolver o problema da "amnésia" do sistema. Anteriormente, os dados financeiros eram perdidos ao fechar o programa.

**Novas Funcionalidades:**
* **Persistência de Dados:** Implementação de escrita em arquivos (`.txt`) para salvar o relatório de fechamento de caixa no disco rígido.
* **Gerenciamento de Arquivos:** Uso da estrutura `with open()` para garantir que os arquivos sejam criados, escritos e fechados com segurança, evitando corromper dados.
* **Formatação de Texto:** Uso de caracteres de escape (`\n`) para estruturar o relatório final com quebras de linha adequadas.

**Tech Stack adicionada:**
* Manipulação de Arquivos (File I/O - Mode 'w').
* Context Managers (`with`).
* Formatação de Strings para Arquivos.
