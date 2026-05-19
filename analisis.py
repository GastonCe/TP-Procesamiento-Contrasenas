def contar_tipos_caracteres(contrasena:str):
    """
    Cuenta la cantidad de letras, numeros, espacios y simbolos que tiene la contraseña ingresada
    Args:
        contrasena(str): contraseña ingresada
    """
    cant_letras=0
    cant_numeros=0
    cant_simbolos=0
    cant_espacios=0
    largo=len(contrasena)
    simbolos="""!"#$%&'()*+,-./"""

    for i in range(largo):
        caracter=contrasena[i]
        if "a"<=caracter<="z" or "A"<=caracter<="Z":
            cant_letras+=1
        elif "0"<=caracter<="9":
            cant_numeros+=1
        elif caracter==" ":
            cant_espacios+=1
        else:
            for j in range(len(simbolos)):
                if caracter==simbolos[j]:
                    cant_simbolos+=1
    print(f"La contrasena ingresa contiene:")
    print(f"Cantidad de numeros: {cant_numeros}")
    print(f"Cantidad de letras: {cant_letras}")
    print(f"Cantidad de espacios: {cant_espacios}")
    print(f"Cantidad de simbolos: {cant_simbolos}")
  
def buscar_caracter(contrasena:list,caracter:chr):
    """
    Busca cuantas veces aparece un caracter ingresado por teclado dentro de la contraseña ingresada
    y en que posiciones se encuentra
    Args:
        contrasena(str): contraseña ingresada por teclado
        caracter(char): El caracter a buscar
    """
    cant_aparicion=0
    largo=len(contrasena)
    lista_posiciones=[0]*largo
    for i in range(largo):
        if contrasena[i]==caracter:
            lista_posiciones[cant_aparicion]=i
            cant_aparicion+=1
    lista_final=lista_posiciones[0:cant_aparicion]
    print(f"El caracter buscado aparece {cant_aparicion} veces")
    print(f"En las posiciones: {lista_final}")




