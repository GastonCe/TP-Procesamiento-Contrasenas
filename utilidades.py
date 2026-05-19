
def transformar_minuscula(texto: str) -> str:
    """
    Convierte los caracteres que sean letras marusculas a minusculas y 
    devuelve esa nueva cadena
    Args:
        texto(str): Cadena a revisar
    Returns:
        str: Cadena convertida todo a mayusculas, si es posible
    """
    largo = len(texto)
    texto_minúscula = ""
    
    for i in range(largo):
        caracter = texto[i]
        
        # Si el caracter esta en el rango de las mayusculas
        if caracter >= "A" and caracter <= "Z":
            # Le sumamos 32 para transformarlo en minuscula
            numero_ascii = ord(caracter)
            nueva_letra = chr(numero_ascii + 32)
            texto_minúscula += nueva_letra
        else:
            # Si no es mayuscula lo dejamos igual
            texto_minúscula += caracter
            
    return texto_minúscula

def burbuja(lista:list, ascendente:bool)->list:
    """
    Odena la contraseña en forma ascendente o descendente segun eligio el usuario
    utilizando metodo de burbujeo
    Args:
        lista(list): lista que contiene los caractedes de la contraseña
        ascendente(bool): Recibe true si se desea ordenar ascendente o false si se desea descendente
    Returs:
        list: Devuelve la lista ordenada
    """
    n = len(lista)
    # ASCENDENTE
    if ascendente:
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    auxiliar = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = auxiliar
    # DESCENDENTE
    else:
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] < lista[j + 1]:
                    auxiliar = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = auxiliar

    return lista

def ordenar_contrasena(contrasena:str):
    """
    Ordena una contraseña ingresada por teclado utlizando el metodo Burbuja,
    donde el usuario elige si desea ascendente o descendente
    Args:
        contrasema(str): Contraseña ingresada por teclado
    """
    eleccion=input("Elija manera de ordenar (asc/desc): ")
    #Con los caracteres de la contraseña armo una lista
    largo=len(contrasena)
    lista=[" "]*largo

    for i in range(largo):
        lista[i]=contrasena[i]

    if eleccion=="asc":
        lista_ordenada=burbuja(lista,True)
        print(f"Lista ordenada ascendente: {lista_ordenada}")
    elif eleccion=="desc":
        lista_ordenada=burbuja(lista,False)
        print(f"Lista ordenada descendente: {lista_ordenada}")
    else:
        print("Opcion invalida!!!")
    
def mostrar_contrasena_invetida(contrasena:str)->str:
    """
        Invierte la contraseña ingresada y la imprime
        Args:
            contrasena(str): la contraseña ingresada por teclado
        Returns
            str: Devuelve un string que es usado mas adelante para veirificar si la contraseña 
                 es palindromo
    """
    largo=len(contrasena)
    #Guardo espacio fijo en memoria para la longitud de la lista
    lista=[0]*largo 
    for i in range(largo):
        lista[largo-i-1]=contrasena[i]

    contra_invertida=""
    for i in range(largo):
        contra_invertida+=lista[i]
    print(f"Contrasena invertida: {contra_invertida}")
    return contra_invertida

def verificar_palindromo(contrasena:str):
    """
    Reutiliza la funcion mostrar_contraseña_invertida. Verifica si es palindromo y lo muestra por pantalla
    Args:
        contrasema(str): Contraseña ingresada por teclado 
    """
    contrasena_invertida=mostrar_contrasena_invetida(contrasena)
    contrasena_minuscula=transformar_minuscula(contrasena_invertida)     
    #compara ambas textos (la contrasena original y la invertida)
    if contrasena==contrasena_minuscula:
        print(f"La contasena '{contrasena}' es un palindromo.")
    else:
        print(f"La contasena '{contrasena}' no es un palindromo.")
