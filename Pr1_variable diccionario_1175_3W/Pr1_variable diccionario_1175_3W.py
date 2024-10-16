print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Definimos un diccionario que contiene las divisas y sus símbolos.
divisas = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}

# Pedimos al usuario que ingrese una divisa.
divisa_input = input("Introduce una divisa (Euro, Dollar, Yen): ")

# Buscamos la divisa en el diccionario y mostramos el símbolo correspondiente.
if divisa_input in divisas:
    # Si la divisa está en el diccionario, mostramos su símbolo.
    print(f"El símbolo de {divisa_input} es: {divisas[divisa_input]}")
else:
    # Si la divisa no está en el diccionario, mostramos un mensaje de error.
    print("La divisa no está en el diccionario.")
