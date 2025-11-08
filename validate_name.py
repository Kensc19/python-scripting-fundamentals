def is_valid_name():
    name = input("Por favor, ingrese un nombre: ")
    for char in name:
        if not char.isalpha() and char != ' ':
            print("Entrada inválida. El nombre solo debe contener letras y espacios.")
            return False
    
    print("El nombre ingresado es", name)
is_valid_name()