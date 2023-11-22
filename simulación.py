"""
Actividad 1 - 25 puntos
Por consola se piden como máximo 5 números hasta que pulsas q
muestra la suma de los números introducidos.
algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
"""

def suma_numeros(*numeros):
    try:
        numeros = [float(numero) for numero in numeros if float(numero) >= 0]
        resultado = sum(numeros)
        return resultado
    except ValueError:
        return "Error: Por favor, ingresa números válidos y no negativos."


# Solicitar números al usuario
entrada = input("Introduce hasta 5 números no negativos separados por espacios (o 'q' para salir): ").split()

# Verificar si se ingresó 'q' para salir
if 'q' in entrada:
    print("Saliendo del programa.")
else:
    # Limitar la cantidad de números a 5
    entrada = entrada[:5]

    # Llamar a la función con los números ingresados
    resultado = suma_numeros(*entrada)

    # Mostrar el resultado
    print(f"La suma de los números no negativos introducidos es: {resultado}")

""" en un principio he utilizado un try para hacer una validación para que si pone algun argumento no valido 
este le salte como ingresar un argumento valido, y despues he usado el if para poder hacer un comando de salida, 
ya que si por ejemplo utilizo un while este tendria que seguir hasta que sea 5 sin poder escoger que sean menos números"""

"""
Actividad 2
En consola se piden las unidades y el precio.
Estos datos permiten calcular el subtotal.
Si el día de hoy es anterior al 15 de cada mes, se aplica
un descuento del 5%
Muestra el resultado el total de la factura.
algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
"""

def tienda(*precio):
    try:

    dia=input(int("dime un dia numéricamente ej:7"))
    precio=input(int("dime el precio de la compra"))




"""
Actividad 3
En consola pides número inicial.
En consola pides número final.
Muestra una lista con todos los números pares que hay entre 
estos dos números.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
"""

"""
Actividad 4
Crea un módulo con las siguientes clases
Mesa
Silla
Lampara
las tres clases tiene como atributo color y precio.
En otro módulo importa únicamente la clase Silla y crea dos sillas. Una de color azul y otra roja con precios de 9.95

algoritmo funciona:5 puntos
algoritmo utiliza características de POO : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica enumeradores o similar para Color : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
"""