#Ejercicio 6.

def ejercicio_6():
  palabra = input("Ingresá una palabra: ").lower()

  if "a" in palabra and "n" in palabra:
      print("Hay letras a y n.")
  else:
      if "a" in palabra and not "n" in palabra:
      #if "a" in palabra:
          print("Solo hay letras a")
      elif "n" in palabra and not "a" in palabra:
      #if "n" in palabra:
          print("Solo hay letras n")
      else:
          print("No se encontro ninguna")



#ejercicio_6()



#---------------------#
#Ejercicio 7.

# import string


# texto = """El salario promedio de un hombre en Argentina es de $60.000, mientras que el de una mujer es de $45.000. Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas."""

# #print(string.ascii_uppercase)

# #mayusculas = list(map(lambda x: x in string.ascii_uppercase, texto))

# mayusculas = set(filter(lambda x: x in string.ascii_uppercase, texto)) #Incluir repetidos?

# print(mayusculas)


# minusculas = set(filter(lambda x: x in string.ascii_lowercase, texto))
# print(minusculas)

# caracteres_no_letras = set(filter(lambda x: x not in string.ascii_letters, texto))
# print(caracteres_no_letras)


# texto_en_palabras = texto.split(" ")
# print(texto_en_palabras)
# print(f"Cantidad de palabras en texto: {len(texto_en_palabras)}")



#------------------#
#Ejercicio 8.
# from collections import Counter

# print("Ingrese una palabra o frase: ")
# cadena = input()


# contador = Counter(cadena)

# if " " in cadena:
#   contador.pop(" ")

# print(contador)


# mas_ocurrencias = contador.most_common(1)[0][1]
# print(mas_ocurrencias)

# if mas_ocurrencias == 1:
#     print("Es heterograma.\n")
# elif mas_ocurrencias > 1:
#     print("No es heterograma.\n")



#Ejercicio 9.

print("Ingrese una palabra: \n")
palabra = input()

#dicc = {"A, E, I, O, U, L, N, R, S, T":1}
dicc = {("A", "E", "I","O", "U"):1}



print(dicc.keys())

suma = 0
for elem in palabra:
  if elem in dicc[0]:
     suma += 1

print(suma)

   














