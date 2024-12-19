import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = []
    estadisticas = {
        "intentos_totales": 0,
        "mejor_intento": None
    }
    
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    while True:
        try:
            adivinanza = int(input("Intenta adivinar: "))
            intentos.append(adivinanza)
            estadisticas["intentos_totales"] += 1
            
            if adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {estadisticas['intentos_totales']} intentos.")
                
                # Actualizar mejor intento
                if estadisticas["mejor_intento"] is None or estadisticas["intentos_totales"] < estadisticas["mejor_intento"]:
                    estadisticas["mejor_intento"] = estadisticas["intentos_totales"]
                    print("¡Este es tu mejor intento hasta ahora!")
                
                print(f"Tus intentos: {intentos}")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

# Ejecutar el juego
adivina_el_numero()
