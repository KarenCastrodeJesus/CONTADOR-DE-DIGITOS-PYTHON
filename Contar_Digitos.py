def contar_digitos():
  print("--- MÉTODO: CONTAR DÍGITOS ---")
  try:
    numero = int(input("Introduce un numero entero: "))
  except ValueError:
    print("Por favor, introduce un número entero válido.")
    return

  contador = 0

  if numero == 0:
    contador = 1
  else:
    numero = abs(numero)
    while numero > 0:
      numero = numero // 10
      contador += 1

  print(f"El numero tiene {contador} digitos.\n")


if __name__ == "__main__":
  contar_digitos()