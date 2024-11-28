import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    while True:
        try:
            adivinanza = int(input("Intenta adivinar: "))
            intentos += 1
            
            if adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

# Ejecutar el juego
adivina_el_numero()
