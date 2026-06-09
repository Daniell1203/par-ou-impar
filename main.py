import random

n = int(input("Digite um numero de 1 a 10: "))
p = random.randint(0, 10)
soma = n + p

resultado = "PAR" if soma % 2 == 0 else "IMPAR"
print(f"A opção vencedora foi {resultado}")