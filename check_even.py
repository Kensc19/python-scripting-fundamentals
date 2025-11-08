def is_even():
    num = input("Por favor, ingrese un número entero:")
    while not num.isdigit():
        print("Entrada inválida, por favor ingrese un número entero.")
        num = input("Por favor, ingrese un número entero:")
    if int(num) % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")
is_even()