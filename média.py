while True:
    print("\n---Média---")
    nome = input("\nDigite o seu nome: ")
    n1 = float(input("\nDigite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    media = (n1 + n2 + n3) / 3

    if media >= 7:
        print(f"\nAprovado! Média: {media:.1f}")
    elif media >= 5 and media < 7:
        print(f"\nRecuperação. Média: {media:.1f}")
    elif media < 5:
        print(f"\nReprovado. Média: {media:.1f}")