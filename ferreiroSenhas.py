import secrets

# Conjuntos de caracteres possíveis
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*"

# ----------------------------------------------------------------------------

print("=== BEM VINDO AO FERREIRO DE SENHAS ===")

while True:
    # Tratamento para garantir um tamanho de senha válido
    while True:
        tamanho = int(input("\nQual o tamanho da senha que você quer? "))

        if tamanho > 0:
            break  # Valor válido, sai do loop do tamanho
        else:
            print("Por favor, digite um número maior que zero!")

    # Pergunta se quer caracteres especiais
    usar_simbolos = input("Quer incluir símbolos? (s/n): ")

    # Monta a lista de caracteres permitidos
    caracteres = letras + numeros

    if usar_simbolos == "s":
        caracteres = caracteres + simbolos

    # Gera a senha sorteando caractere por caractere
    senha = ""
    for i in range(tamanho):
        caractere_sorteado = secrets.choice(caracteres)
        senha = senha + caractere_sorteado

    print("Sua nova senha é:", senha)

    # Pergunta se o usuário quer continuar
    resposta = input("\nQuer gerar outra senha? (s/n): ")
    if resposta != "s":
        print("Programa encerrado. Até mais!")
        break  # Sai do loop principal e finaliza o programa
