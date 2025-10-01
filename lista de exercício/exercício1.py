def devolvaResposta (seuNome, nomePai, nomeMae):
    print(f"Nome do usuário: {seuNome}")
    print(f"Nome dos pais: {nomePai} e {nomeMae}")


seuNome = str(input("Digite o seu nome: "))
nomePai = str(input("Digite o nome do seu pai: "))
nomeMae = str(input("Digite o nome da sua mae: "))

devolvaResposta(seuNome, nomePai, nomeMae)