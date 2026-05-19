
def longitud_total(contrasena:str):
    """
        Calcula la longitud total de la contraseña y lo muestra
    """
    print(f"La longitud total de la contrasena es: {len(contrasena)}")

def porcentaje_letras(contrasena:str):
    """
        Calcula el porcentaje de letras que contiene la contraseña y lo imprime
        Args:
            contrasena(str): Contraseña ingresada por teclado
    """
    cont=0
    largo=len(contrasena)
    for i in range(largo):
        caracter=contrasena[i]
        if "a"<=caracter<="z" or "A"<=caracter<="Z":
            cont+=1
    porcentaje=cont*100/largo
    print(f"Porcentaje de letras: {porcentaje} %")

def porcentaje_numeros(contrasena:str):
    """
        Calcula el porcentaje de numeros que contiene la contraseña y lo imprime
        Args:
            contrasena(str): Contraseña ingresada por teclado
    """
    cont=0
    largo=len(contrasena)
    for i in range(largo):
        caracter=contrasena[i]
        if "0"<=caracter<="9":
            cont+=1
    porcentaje=cont*100/largo
    print(f"Porcentaje de numeros: {porcentaje} %")

def porcentaje_simbolos(contrasena:str):
    """
        Calcula el porcentaje de simbolos que contiene la contraseña y lo imprime
        Args:
            contrasena(str): Contraseña ingresada por teclado
    """
    cont=0
    largo=len(contrasena)
    simbolos="""!"#$%&'()*+,-./"""
    for i in range(largo):
        caracter=contrasena[i]
        for j in range(len(simbolos)):
            if caracter==simbolos[j]:
                cont+=1
    porcentaje=cont*100/largo
    print(f"Porcentaje de simbolos: {porcentaje} %")

def caracteres_repetidos_consecutivos(contrasena:str):
    """
    Genera 2 listas en paralelo. Una guarda el caracter que se repite y la otra en el mismo indice 
    guarda la cantidad de veces que se repite dicho caracter. luego imprime ambas listas en simultaneo
    Args
        contrasena(str): Contraseña ingresada por teclado
    """
    cont_distintos=0
    largo=len(contrasena)
    #Esta variable lista guarda los caracteres repetidos
    lista_consecutivos=[" "]*largo 
    lista_cantidades=[0]*largo #guarda las cantidades de cada caracter que se repite
    #Guardo el caracter de las posicion 0 porque empieza a comparar con la posicion 1
    caracter_anterior=contrasena[0] 
    for i in range(1,largo):
        encontrado=False
        caracter=contrasena[i]

        if caracter==caracter_anterior:
            
            for j in range(cont_distintos):
              if lista_consecutivos[j] == caracter:
                    # Solo sumamos si el de atras no era igual al de hace dos vueltas.
                    # El i == 1 es por si pasa en el arranque.
                    if i == 1 or contrasena[i-1] != contrasena[i-2]:
                        lista_cantidades[j] += 1
                        encontrado = True
              
        # Lo agrego si es la primera vez que se repite consecutivamente este caracter
            if not encontrado:
                lista_consecutivos[cont_distintos] = caracter
                lista_cantidades[cont_distintos] = 1
                cont_distintos += 1

        caracter_anterior=caracter

    if cont_distintos==0:
        print("No se encontraron elementos repetidos consecutivos")
    else:
        print(f"Lista consecutiva: {lista_consecutivos}")
        for i in range(cont_distintos):
            print(f"El caracter {lista_consecutivos[i]} se repite {lista_cantidades[i]} veces")
                     
def generar_reporte_estadistico(contrasena:str):
    """"
        Recibe la contraseña ingresada e invoca las funciones para dar el reporte completo
        Args:
            contrasena(str): Contraseña ingresada por teclado
    """
    longitud_total(contrasena)
    porcentaje_letras(contrasena)
    porcentaje_numeros(contrasena)
    porcentaje_simbolos(contrasena)
    caracteres_repetidos_consecutivos(contrasena)
