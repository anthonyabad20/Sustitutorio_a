import random
import datetime

def generar_numero_aleatorio():
    """Genera un número aleatorio entre 1 y 50."""
    return random.randint(1, 50)

def pedir_numero():

    while True:
        try:
            numero = int(input("Ingresa un número entre 1 y 100: "))
            if 1 <= numero <= 100:
                return numero
            else:
                print("El número debe estar entre 1 y 100.")
        except ValueError:
            print("Ingresa un valor numérico válido.")

def decorador_adivinado(funcion):

    def envoltura(*args, **kwargs):
        print("----- ¡Adivinando! -----")
        resultado = funcion(*args, **kwargs)
        print("----- ¡Número encontrado! -----")
        return resultado
    return envoltura


@decorador_adivinado
def adivina():
    print("Se ha creado un numero aleatorio de 1 a 100.Desafiate e intenta descubrirlo")
    numero_aleatorio = generar_numero_aleatorio()
    intentos = 0
    while True:
        numero_ingresado = pedir_numero()
        intentos += 1
        if numero_ingresado == numero_aleatorio:
            print("Felicidades.Has ganado ")
            ahora = datetime.datetime.now()
            print(f"Lo lograste en {intentos} intentos, el {ahora.day}/{ahora.month}/{ahora.year} a las {ahora.hour}:{ahora.minute}")
            break
        elif numero_ingresado < numero_aleatorio:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")

