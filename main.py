# Sempre que suspeitar de uma vaga, adcione aqui
lista_negra = ["empresa123", "vaga urgente", "curso pago"]


# 2. A Função de Análise
# Ela recebe o nome e os dados, e devolve uma pontuação
def analisar_vaga(nome_empresa, site, cobrou_dinheiro):
    score = 0

    # verifica a lista negra
    if nome_empresa in lista_negra:
        score += 20  # Pontuação altíssima se já estiver na lista

    # verifica se houve cobrança
    if cobrou_dinheiro == "sim":
        score += 10

    # verifica se há site oficial
    if site == "nao":
        score += 3

    return score

# O loop verifica outras empresas sem rodar o programa várias vezes
estatistica_golpes = 0

while True:
    print("\n--- NOVO FILTRO DE VAGA (Digite 'sair' no nome para encerrar) ---")

    nome = input("Nome da empresa: ")
    if nome.lower() == "sair":
        break

    tem_site = input("Possui site oficial? (sim/nao): ").lower()
    pediu_pagamento = input("Exigiram pagamento de curso/taxa? (sim/nao): ").lower()


    resultado_risco = analisar_vaga(nome, tem_site, pediu_pagamento)

    # Exibe o relatório da consulta
    print(f"\nRelatório para: {nome}")
    if resultado_risco >= 10:
        print("❌ ALERTA VERMELHO: Altíssima probabilidade de golpe!")
        estatistica_golpes += 1
    elif resultado_risco >= 3:
        print("⚠️ ATENÇÃO: Verifique melhor as informações antes de prosseguir.")
    else:
        print("✅ PARECE SEGURO: Mas lembre-se, nunca pague para trabalhar!")

print(f"\nPrograma encerrado. Você identificou {estatistica_golpes} possíveis golpes hoje.")

