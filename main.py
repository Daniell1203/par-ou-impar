import random

n = int(input("Digite um numero de 1 a 10: "))
esc = input("par ou impar: ").upper()
p = random.randint(0, 10)
soma = n + p

resultado = "PAR" if soma % 2 == 0 else "IMPAR"
print(f"A opção vencedora foi {resultado}")

if esc == resultado:
    print("Voce venceu!")
else:
    print("Perdeu")