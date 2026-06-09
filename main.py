import random

v = 0

while True:
    while True:
        try:
            n = int(input("Digite um numero de 1 a 10: "))
            if 1 <= n <= 10:
                break
            print("Digite um numero entre 1 e 10.")
        except ValueError:
            print("Entrada invalida. Digite um numero.")

    while True:
        esc = input("par ou impar: ").upper()
        if esc in ("PAR", "IMPAR"):
            break
        print("Digite apenas 'par' ou 'impar'.")

    p = random.randint(0, 10)
    soma = n + p

    resultado = "PAR" if soma % 2 == 0 else "IMPAR"
    print(f"Soma: {soma} → A opção vencedora foi {resultado}")

    if esc == resultado:
        print("Voce venceu!")
        v += 1
    else:
        print("Perdeu!")
        break

print(f"Numero de vitorias: {v}")