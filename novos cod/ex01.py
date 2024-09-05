# Solicita ao usuário a quantidade de números que ele deseja inserir
quantidade = int(input("Quantos números você deseja inserir? "))

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Usa um loop para receber os números do usuário e adicioná-los à lista
for i in range(quantidade):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Calcula a soma dos números na lista
soma = sum(numeros)

# Calcula a média dos números
media = soma / quantidade

# Exibe a média
print(f"A média dos números inseridos é: {media}")
