def cadastrar_cliente():
    print("Olá, meu nome é JOANAs, sou sua assistente sustentável. Antes de tudo, vamos te conhecer um pouquinho melhor!")
    print("Vamos realizar o seu cadastro.")
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
    print("\nPara você conhecer um pouquinho mais sobre minhas funcionalidades, fale um pouco sobre o que você quer plantar!")
    tipo_planta = input("Selecione o tipo de planta do plantio:\n1. Trigo\n2. Milho\n3. Arroz\n4. Feijão\n")
    tipo_solo = input("Selecione o tipo de solo do plantio:\n1. Argiloso\n2. Arenoso\n3. Mistura de Argila e Areia\n")

    if tipo_planta == "1":
        tipo_planta = "Trigo"
    elif tipo_planta == "2":
        tipo_planta = "Milho"
    elif tipo_planta == "3":
        tipo_planta = "Arroz"
    elif tipo_planta == "4":
        tipo_planta = "Feijão"

    if tipo_solo == "1":
        tipo_solo = "Argiloso"
    elif tipo_solo == "2":
        tipo_solo = "Arenoso"
    elif tipo_solo == "3":
        tipo_solo = "Mistura de Argila e Areia"

    plantio = {
        "tipo_planta": tipo_planta,
        "tipo_solo": tipo_solo,
        "possiveis_pragas": identificar_pragas(tipo_planta)
    }

    return plantio

def identificar_pragas(tipo_planta):

    pragas = {

        "Trigo": ["Lagarta do cartucho", "Ferrugem do trigo", "Pulgões"],
        "Milho": ["Lagarta do cartucho", "Lagarta elasmo", "Broca do colmo"],
        "Arroz": ["Bicho mineiro", "Lagarta do arroz", "Percevejo do colmo"],
        "Feijão": ["Mosca branca", "Lagarta da vagem", "Antracnose"]
    }

    if tipo_planta in pragas:
        return pragas[tipo_planta]
    else:
        return []

def main():
    cliente = cadastrar_cliente()
    while True:
        opcao = input("\nVamos cadastrar um plantio? Digite '1' para continuar ou '2' para encerrar: ")

        if opcao == "1":
            plantio = cadastrar_plantio()
            cliente["plantios"].append(plantio)
            print("\nPlantio cadastrado com sucesso!")
        elif opcao == "2":
            break

    for plantio in cliente["plantios"]:
        tipo_solo = plantio["tipo_solo"]

        print(f"\nVi que você quer fazer um plantio de {plantio['tipo_planta']} no solo {tipo_solo}. É recomendado também para esse solo recomendado cultivar as sementes:")

        if tipo_solo == "Argiloso":
            sementes_recomendadas = ["Trigo", "Milho"]
        elif tipo_solo == "Arenoso":
            sementes_recomendadas = ["Feijão", "Arroz"]
        elif tipo_solo == "Mistura de Argila e Areia":
            sementes_recomendadas = ["Milho", "Feijão"]
        else:
            sementes_recomendadas = []

        if sementes_recomendadas:
            for semente in sementes_recomendadas:
                print(f"- {semente}")

        print("\nPossíveis pragas:")
        for praga in plantio["possiveis_pragas"]:
            print(f"- {praga}")

    print("\nPlantios realizados:")
    for plantio in cliente["plantios"]:
        print(f" - Tipo de planta: {plantio['tipo_planta']}")
        print(f" - Tipo de solo: {plantio['tipo_solo']}")


if __name__ == "__main__":
    main()
