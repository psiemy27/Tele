canales = ["TV1", "TV2s", "A3", "Cuatro", "Tele5", "Sexta"]

while True:
    
    SELECCION_CANAL = int(input("Choose a channel number (1-6): "))

    if 1 <= SELECCION_CANAL <= len(canales):
        print("Selected channel:", canales[SELECCION_CANAL - 1])
    else:
        print("Invalid channel!")

    respuesta = input("Do you want to try another channel? (yes/no): ").strip().lower()
    if respuesta != "yes":
        print("Program closed. Goodbye!")
        break