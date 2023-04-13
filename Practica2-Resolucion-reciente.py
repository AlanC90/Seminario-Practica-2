#Resolución de Practica 2.

#Inicio de Programa.
print('----------------------------------------\n')
print('Bienvenido/a.\n')
print()


print('Resolucion de ejercicios 1 y 2.\n')

print()

#Cargar contenido de README.md en variable.
texto ="""

NumPy is the fundamental package for scientific computing with Python.

Website: https://www.numpy.org
Documentation: https://numpy.org/doc
Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
Source code: https://github.com/numpy/numpy
Contributing: https://www.numpy.org/devdocs/dev/index.html
Bug reports: https://github.com/numpy/numpy/issues
Report a security vulnerability: https://tidelift.com/docs/security


It provides:
a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities

Testing:
NumPy requires pytest and hypothesis. Tests can then be run after installation with:

python -c "import numpy, sys; sys.exit(numpy.test() is False)"


Code of Conduct
NumPy is a community-driven open source project developed by a diverse group of contributors. The NumPy leadership has made a strong commitment to creating an open, inclusive, and positive community. Please read the NumPy Code of Conduct for guidance on how to interact with others in a way that makes our community thrive.

Call for Contributions
The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated. If you are considering larger contributions to the source code, please contact us through the mailing list first.

Writing code isn’t the only way to contribute to NumPy. You can also:

review pull requests
help us stay on top of new and old issues
develop tutorials, presentations, and other educational materials
maintain and improve our website
develop graphic design for our brand assets and promotional materials
translate website content
help with outreach and onboard new contributors
write grant proposals and help with other fundraising efforts
For more information about the ways you can contribute to NumPy, visit our website. If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invitation).

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved.

"""

print(" Texto de README.md cargado.\n")
print()


#----------#
#Ejercicio 1. 

def ejercicio_1():
  print(' Procesamiento de datos.\n')

  #Dividir texto por lineas.
  lineas = texto.split("\n")

  #Imprimir lineas que contienen "http" o "https".
  cantL = 0
  print('  Lineas que contienen "http" o "https": \n')
  for elem in lineas:
      if "http" in elem or "https" in elem:           #Revisar.
          print(f'   {elem}')
          cantL+=1

  if cantL == 0:           #Caso en que no haya lineas que cumplan criterio.
    print('   Ninguna\n')


  print()

  print()


#----------#
#Ejercicio 2.
def ejercicio_2():

    from collections import Counter
    import string

    #Dividir texto en palabras.
    palabras = texto.split()

    #Remover signos de puntuacion.
    caract_puntuacion = string.punctuation

    palabras = list(map(lambda x: x.strip(caract_puntuacion),palabras))


    #Pasar palabras a minusculas.
    palabras_en_minusc = list(map(lambda x: x.lower(), palabras))


    #Procesar texto e informar palabra que aparece mayor cantidad de veces.
    contador = Counter(palabras_en_minusc)

    palabraMayor = contador.most_common(1)

    print('  Palabra que aparece mayor cantidad de veces es: ')
    print(f'   "{palabraMayor[0][0]}" con {palabraMayor[0][1]} veces.\n')


    print()

    print(' ----------\n')


#----------#
#Ejercicio 3.
import string


def ejercicio_3():
    print(' Resolucion de ejercicio 3.\n')

    print()

    #Cargar datos.
    jupyter_info = """ JupyterLab is a web-based interactive development
    environment for Jupyter notebooks,
    code, and data. JupyterLab is flexible: configure and arrange the user
    interface to support a wide range
    of workflows in data science, scientific computing, and machine learning.
    JupyterLab is extensible and
    modular: write plugins that add new components and integrate with existing
    ones.
    """

    print('  Texto guardado en variable "jupyter_info".\n')


    print()


    #Procesar datos.
    print('   Procesamiento de datos.\n')

    #Leer letra desde teclado. 
    # Si es válida informar palabras que comienzan con dicha letra.
    letra = input('    Ingrese una letra: ')

    print()

    if letra in string.ascii_letters:

        #Convertir texto en lista de palabras.
        palabras_jupyter = jupyter_info.split()

        #Remover caracteres de puntuacion.
        palabras_jupyter = list(map(lambda x: x.strip(string.punctuation), palabras_jupyter)) 

        #Se almacena el conjunto de palabras que cumplen criterio.  
        print('    Palabras dentro del texto que empiezan con letra ingresada: ')
        palabras_jup_cumplen = set(filter(lambda x: x.startswith(letra), palabras_jupyter))

        #Se informa.
        if len(palabras_jup_cumplen) == 0:
            print('     0 (Ninguna)')
        else:
            for elem in palabras_jup_cumplen:
                print(f'     {elem}')  

    #En caso de que no se ingrese caracter valido, se informa.
    else:
        print('     No se ingreso una letra.\n')


    print()

    print()

    print(' ----------\n')


#----------#
#Ejercicio 4.

def ejercicio_4():
    print(' Resolucion de ejercicio 4.\n')

    print()

    evaluar = """ título: Experiences in Developing a Distributed Agent-based
    Modeling Toolkit with Python
    resumen: Distributed agent-based modeling (ABM) on high-performance
    computing resources provides the promise of capturing unprecedented details
    of large-scale complex systems. However, the specialized knowledge required
    for developing such ABMs creates barriers to wider adoption and utilization.
    Here we present our experiences in developing an initial implementation of
    Repast4Py, a Python-based distributed ABM toolkit. We build on our
    experiences in developing ABM toolkits, including Repast for High
    Performance Computing (Repast HPC), to identify the key elements of a useful
    distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
    and the Python C-API to create a scalable modeling system that can exploit
    the largest HPC resources and emerging computing architectures.
    """
 
    print("  Texto de articulo a analizar cargado.\n")

    print("   Procesar texto.\n")


    #Separar texto en lineas.
    lineas = evaluar.split('\n')



    #Almacenar y procesar titulo.
    titulo = (lineas[0] + lineas[1])

    titulo = titulo.strip(' título: ')

    titulo = titulo.split(' ')

    #Remover espacios en blanco que estan de mas.
    for numero in range(1, 4):
      titulo.pop(6)

    #Verificar e informar si cumple criterio.
    cant_palabras = len(titulo)
    if cant_palabras <= 10:
        print(f'    Título: ok ({cant_palabras} palabras)\n')
    else:
        print(f'    Título: not ok ({cant_palabras} palabras)\n')



    #Almacenar y procesar resumen.
    resumen = lineas[2:]

    #Remover lo innecesario.
    resumen = list(map(lambda x: x.strip("   "),resumen))
    resumen[0] = resumen[0].strip('resumen: ') #Preguntar por que se elimina la 'e' de 'performance'.

    #Pasar de lista a string.
    texto = ""
    for elem in resumen:
      texto = texto + ' ' + elem

    #Separar en oraciones.
    texto = texto.split(".")
    
    #Remover espacio vacio en ultima posicion.
    texto.pop(len(texto)-1)


    #Informar tipos de oracion segun criterios. #Preguntar si esta bien.
    
    #Inicializar contadores.
    lista = [0,0,0,0]

    for oracion in texto:
        #Separar la linea en palabras.
        oracion = oracion.split(' ')

        #Remover espacio vacío de oracion.
        oracion = oracion[1:]

        #Analizar e incrementar contadores.
        cant_palabras = len(oracion)

        if cant_palabras <= 12:       
            lista[0] += 1
            
        elif cant_palabras >= 13 and cant_palabras <= 17:
            lista[1] += 1
            
        elif cant_palabras >= 18 and cant_palabras <= 25:
            lista[2] += 1
            
        elif cant_palabras > 25:
            lista[3] += 1
                        

    #Informar.
    print(f'    Cantidad de oraciones faciles de leer: {lista[0]}, aceptables para leer: {lista[1]}, dificiles de leer: {lista[2]}, muy dificiles de leer: {lista[3]}')     


    print()

    print()

    print(' ----------\n')



#----------#
#Ejercicio 5.

def ejercicio_5():    

    print(' Resolucion de ejercicio 5.\n')

    print()

    
    from collections import Counter
    import string

    #Leer datos desde teclado.
    print("   Ingrese una frase: ")
    frase = input('    ')

    print()

    print("   Ingrese una palabra: ")
    cadena = (input("    ")).lower()

    print()


    #Dar formato a datos ingresados.
    lista_palabras = frase.split(" ")

    lista_palabras = list(map(lambda x: x.lower(), lista_palabras))

    lista_palabras = list(map(lambda x: x.strip(string.punctuation), lista_palabras))

    cadena = cadena.lower()

    
    #Procesar datos.
    #Contar veces que aparece cada palabra en texto.
    contador = Counter(lista_palabras)

    #Informar cantidad de veces que aparece palabra ingresada.
    if cadena in contador.keys():
        print('   Resultado: ')
        print(f'    la palabra ingresada aparece {contador[cadena]} veces.\n')


    print()

    print()

    print(' ----------\n')
    
   
    



#--------------------#
#Main.  

#ejercicio_1()
#ejercicio_2()
#ejercicio_3()
#ejercicio_4()
#ejercicio_5()


#Fin.
print()
print()
print("Fin del programa.\n")
print('----------------------------------------\n')

