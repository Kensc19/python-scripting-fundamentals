def whileLoop():
    num = input("Ingresa un número entre 1 y 10: ")
    while not (num.isdigit() and 1 <= int(num) <= 10):
        print("Entrada inválida. Por favor, intenta de nuevo.")
        num = input("Ingresa un número entre 1 y 10: ")
    print("El número ingresado es ", num)

whileLoop()