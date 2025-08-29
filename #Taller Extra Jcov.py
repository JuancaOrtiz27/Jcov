#Taller Extra Jcov
import random

numero_secreto = random.randint(1, 20)
intentos = 0

print("Adivina el número entre 1 y 20")

while True:
    intento = int(input("Tu número: "))
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo")
    elif intento > numero_secreto:
        print("Demasiado alto")
    else:
        print("¡Correcto! Lo lograste en", intentos, "intentos")
        break