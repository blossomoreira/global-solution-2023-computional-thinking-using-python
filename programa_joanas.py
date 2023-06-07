def cadastrar_cliente():

    # Solicita informações ao usuário para cadastrar o mesmo
    print("Olá, meu nome é JOANAs, sou sua assistente sustentavel. Antes de tudo, vamos te conhecer um pouquinho melhor!")
    print("Vamos realizar o seu cadastro.")
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    telefone = input("Digite o seu número de telefone: ")

    # Cria um dicionario com as informações do cliente
    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "plantios": []
    }

    return cliente

def cadastrar_plantio():
    # Solicita informações ao usuário para cadastrar um plantio
    print("\n Para você conhecer um poquinhos mais minhas funcionalidades, fale um pouco sobre o que você quer plantar!")
    tipo_planta = selecionar_opcao("Selecione o tipo de planta do plantio:", ["Trigo", "Milho", "Arroz", "Feijão"])
    tipo_solo = selecionar_opcao("Selecione o tipo de solo do plantio:", ["Argiloso", "Arenoso", "Mistura de Argila e Areia"])

    # Cria um dicionário com as informações do plantio
    plantio = {
        "tipo_planta": tipo_planta,
        "tipo_solo": tipo_solo,
        "possiveis_pragas": identificar_pragas(tipo_planta)
    }

    return plantio

def identificar_pragas(tipo_planta):
    # Dicionário com as pragas possíveis para cada tipo de planta
    pragas = {
        "Trigo": ["Lagarta do cartucho", "Ferrugem do trigo", "Pulgões"],
        "Milho": ["Lagarta do cartucho", "Lagarta elasmo", "Broca do colmo"],
        "Arroz": ["Bicho mineiro", "Lagarta do arroz", "Percevejo do colmo"],
        "Feijão": ["Mosca branca", "Lagarta da vagem", "Antracnose"]
    }

    # Verifica se o tipo de planta existe no dicionário de pragas
    if tipo_planta in pragas:
        return pragas[tipo_planta]
    else:
        return []

def selecionar_opcao(mensagem, opcoes):
    # Exibe a mensagem e as opções disponíveis para selecionar
    print(mensagem)
    for i in range(len(opcoes)):
        print(f"{i+1}. {opcoes[i]}")

    while True:
        # Pede para o usuário escolher uma opção
        escolha = input("Escolha uma opção: ")
        escolha = int(escolha)
        if escolha in range(1, len(opcoes) + 1):
                indice = escolha - 1
                return opcoes[indice]
        else:
                print("Opção inválida. Digite o número correspondente à opção.")

def main():
    # Cadastra um cliente
    cliente = cadastrar_cliente()

    while True:
        # Pergunta ao cliente se deseja cadastrar um plantio
        opcao = selecionar_opcao("\nVamos cadastrar um plantio? Digite uma das opções: ", ["Sim", "Não"])

        if opcao == "Sim":
            # Cadastra um plantio
            plantio = cadastrar_plantio()
            cliente["plantios"].append(plantio)
            print("\nPlantio cadastrado com sucesso!")
        elif opcao == "Não":
            break

    for plantio in cliente["plantios"]:
        tipo_solo = plantio["tipo_solo"]

        print(f"\nPara o plantio de {plantio['tipo_planta']} no solo {tipo_solo}, é recomendado cultivar as sementes:")

        # Verifica o tipo de solo e define as sementes recomendadas
        if tipo_solo == "Argiloso":
            sementes_recomendadas = ["Trigo", "Milho"]
        elif tipo_solo == "Arenoso":
            sementes_recomendadas = ["Feijão", "Arroz"]
        elif tipo_solo == "Mistura de Argila e Areia":
            sementes_recomendadas = ["Milho", "Feijão"]
        else:
            sementes_recomendadas = []

        if sementes_recomendadas:
            # Exibe as sementes recomendadas para o tipo de solo
            for semente in sementes_recomendadas:
                print(f"- {semente}")
        else:
            print("Não há sementes recomendadas para esse tipo de solo.")

        print("\nPossíveis pragas:")
        for praga in plantio["possiveis_pragas"]:
            print(f"- {praga}")

    print("Plantios:")
    for plantio in cliente["plantios"]:
        print(f" - Tipo de planta: {plantio['tipo_planta']}")
        print(f" - Tipo de solo: {plantio['tipo_solo']}")


if __name__ == "__main__":
    main()
