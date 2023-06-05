def cadastrar_cliente():
    print("\nCadastro do Cliente")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "plantios": []
    }

    return cliente

def cadastrar_plantio():
    print("\nCadastro do Plantio")
    tipo_planta = selecionar_opcao("Selecione o tipo de planta do plantio:", ["Trigo", "Milho", "Arroz", "Feijão"])
    tamanho_hectare = float(input("Digite o tamanho do plantio em hectares: "))
    tipo_solo = selecionar_opcao("Selecione o tipo de solo do plantio:", ["Argiloso", "Arenoso", "Mistura de Argila e Areia"])
    modelo_cultivo = selecionar_opcao("Selecione o modelo de cultivo utilizado:", ["Convencional", "Orgânico", "Hidropônico"])

    plantio = {
        "tipo_planta": tipo_planta,
        "tamanho_hectare": tamanho_hectare,
        "tipo_solo": tipo_solo,
        "modelo_cultivo": modelo_cultivo
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
    for index, opcao in enumerate(opcoes, 1):
        print(f"{index}. {opcao}")

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
        opcao = selecionar_opcao("\nDeseja cadastrar um novo plantio? (Digite o número da opção)", ["Sim", "Não"])

        match opcao:
            case "Sim":
                plantio = cadastrar_plantio()
                plantio["possiveis_pragas"] = identificar_pragas(plantio["tipo_planta"])
                cliente["plantios"].append(plantio)
                print("\nPlantio cadastrado com sucesso!")
            case "Não":
                break

    for plantio in cliente["plantios"]:
        match plantio["modelo_cultivo"]:
            case "Convencional":
                print(f"\nPara o plantio de {plantio['tipo_planta']} no solo {plantio['tipo_solo']}, é recomendado cultivar os seguintes vegetais:")
                match plantio["tipo_solo"]:
                    case "Argiloso":
                        print("- Alface")
                        print("- Cenoura")
                    case "Arenoso":
                        print("- Tomate")
                        print("- Pimentão")
                    case "Mistura de Argila e Areia":
                        print("- Tomate")
                        print("- Pimentão")
                    case _:
                        print("Tipo de solo inválido.")

                print("\nPossíveis pragas:")
                for praga in plantio["possiveis_pragas"]:
                    print(f"- {praga}")

            case "Orgânico":
                print(f"\nPara o plantio de {plantio['tipo_planta']} no solo {plantio['tipo_solo']}, é recomendado cultivar os seguintes vegetais:")
                match plantio["tipo_solo"]:
                    case "Argiloso":
                        print("- Alface")
                        print("- Brócolis")
                    case "Arenoso":
                        print("- Pimentão")
                        print("- Abobrinha")
                    case "Mistura de Argila e Areia":
                        print("- Tomate")
                        print("- Pimentão")
                    case _:
                        print("Tipo de solo inválido.")

                print("\nPossíveis pragas:")
                for praga in plantio["possiveis_pragas"]:
                    print(f"- {praga}")

            case "Hidropônico":
                print(f"\nPara o plantio de {plantio['tipo_planta']} no solo {plantio['tipo_solo']}, é recomendado cultivar os seguintes vegetais:")
                match plantio["tipo_solo"]:
                    case "Argiloso":
                        print("- Alface")
                        print("- Rúcula")
                    case "Arenoso":
                        print("- Alface")
                        print("- Espinafre")
                    case "Mistura de Argila e Areia":
                        print("- Alface")
                        print("- Couve")
                    case _:
                        print("Tipo de solo inválido.")

                print("\nPossíveis pragas:")
                for praga in plantio["possiveis_pragas"]:
                    print(f"- {praga}")

    print("\nCliente:")
    print(f"Nome: {cliente['nome']}")
    print("Plantios:")
    for plantio in cliente["plantios"]:
        print(f" - Tipo de planta: {plantio['tipo_planta']}")
        print(f" - Tamanho do hectare: {plantio['tamanho_hectare']} hectares")
        print(f" - Tipo de solo: {plantio['tipo_solo']}")
        print(f" - Modelo de cultivo: {plantio['modelo_cultivo']}")
        print()

if __name__ == "__main__":
    main()
