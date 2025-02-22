import random  # Importamos la librería para generar números aleatorios

# Generamos un número aleatorio entre 1 y 10
secreto = random.randint(1, 10)
intentos = 0
max_intentos = 5

print("Adivina el número (entre 1 y 10). Tienes 5 intentos.")

# Bucle para intentar adivinar
while intentos < max_intentos:
    intento = int(input("Ingresa tu número: "))
    intentos += 1  # Contamos el intento

    if intento == secreto:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
        break  # Salimos del bucle si acierta
    elif intento < secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    # Si llega al último intento y no acertó
    if intentos == max_intentos:
        print("¡Se acabaron los intentos! El número era", secreto)
