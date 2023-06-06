def cadastrar_cliente():
    print("\nOlá, meu nome é JOANAs, sou sua assistente. Antes de tudo, vamos te conhecer um pouquinho melhor!")
    print("\nVamos realizar o seu cadastro.")
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    telefone = input("Digite o seu número de telefone: ")

    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "plantios": []
    }

    return cliente


def cadastrar_plantio():
    print("\nMe fale um pouco sobre o que você quer plantar: ")
    tipo_planta = selecionar_opcao("Selecione o tipo de planta do plantio:", ["Trigo", "Milho", "Arroz", "Feijão"])
    tipo_solo = selecionar_opcao("Selecione o tipo de solo do plantio:", ["Argiloso", "Arenoso", "Mistura de Argila e Areia"])

    plantio = {
        "tipo_planta": tipo_planta,
        "tipo_solo": tipo_solo,
        "possiveis_pragas": identificar_pragas(tipo_planta)
    }

    return plantio


def identificar_pragas(tipo_planta):
    pragas = {
        "Trigo": ["Lagarta-do-cartucho", "Ferrugem-do-trigo", "Pulgões"],
        "Milho": ["Lagarta-do-cartucho", "Lagarta-elasmo", "Broca-do-colmo"],
        "Arroz": ["Bicho-mineiro", "Lagarta-do-arroz", "Percevejo-do-colmo"],
        "Feijão": ["Mosca-branca", "Lagarta-da-vagem", "Antracnose"]
    }

    if tipo_planta in pragas:
        return pragas[tipo_planta]
    else:
        return []


def selecionar_opcao(mensagem, opcoes):
    print(mensagem)
    for i in range(len(opcoes)):
        print(f"{i+1}. {opcoes[i]}")

    while True:
        escolha = input("Escolha uma opção: ")
        try:
            escolha = int(escolha)
            if escolha in range(1, len(opcoes) + 1):
                indice = escolha - 1
                return opcoes[indice]
            else:
                print("Opção inválida. Digite o número correspondente à opção.")
        except ValueError:
            print("Opção inválida. Digite o número correspondente à opção.")


def main():
    cliente = cadastrar_cliente()

    while True:
        opcao = selecionar_opcao("\nVamos cadastrar um plantio? Digite", ["Sim", "Não"])

        if opcao == "Sim":
            plantio = cadastrar_plantio()
            cliente["plantios"].append(plantio)
            print("\nPlantio cadastrado com sucesso!")
        elif opcao == "Não":
            break

    for plantio in cliente["plantios"]:
        tipo_solo = plantio["tipo_solo"]

        print(f"\nPara o plantio de {plantio['tipo_planta']} no solo {tipo_solo}, é recomendado cultivar as seguintes sementes:")

        if tipo_solo == "Argiloso":
            sementes_recomendadas = ["Semente 1", "Semente 2"]
        elif tipo_solo == "Arenoso":
            sementes_recomendadas = ["Semente 3", "Semente 4"]
        elif tipo_solo == "Mistura de Argila e Areia":
            sementes_recomendadas = ["Semente 5", "Semente 6"]
        else:
            sementes_recomendadas = []

        if sementes_recomendadas:
            for semente in sementes_recomendadas:
                print(f"- {semente}")
        else:
            print("Não há sementes recomendadas para esse tipo de solo.")

        print("\nPossíveis pragas:")
        for praga in plantio["possiveis_pragas"]:
            print(f"- {praga}")

    print("\nCliente:")
    print(f"Nome: {cliente['nome']}")
    print("Plantios:")
    for plantio in cliente["plantios"]:
        print(f" - Tipo de planta: {plantio['tipo_planta']}")
        print(f" - Tipo de solo: {plantio['tipo_solo']}")

if __name__ == "__main__":
    main()
