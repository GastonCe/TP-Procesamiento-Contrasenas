def validar_contrasena()->str:
    """
        Solicita ingreso de contraseña al usuario y verifica que:
          -no este vacia
          -no comience con espacios
          -no tenga menos de 8 caracteres
        Return: 
            str: Contraseña validada
    """
    contraInvalida=True
    while contraInvalida:
        contrasena=input("ingrese contrasena: ")
        if contrasena== "":
            print("La contrasena no puede estar vacia")
        elif contrasena[0]==" ":
            print("La contrasena no puede comenzar con espacios")
        elif len(contrasena)<8:
            print("La contrasena debe tener al menos 8 caracteres")
        else:
            contador=0
            for i in range (len(contrasena)):
               # print(f'{contrasena[i]}')
                if (contrasena[i]>="a" and contrasena[i]<="z") or (contrasena[i]>="A" and contrasena[i]<="Z"):
                    contador=1
            if contador==1: 
                contraInvalida=False
            else:
                print("La contrasena debe tener al menos 1 letra")
    return contrasena

def validar_nivel_seguridad(contrasena:str)->str:
    """ 
        Verifica si la contraseña de ingresa tiene nivel de seguridad debil, medio o fuerte

        Args:
            contraseña(str): La contraseña ingresada
        Returns:
            str: Un cadena con el valor debil, medio o fuerte 
    """
    contiene_letras=False
    contiene_numeros=False
    contiene_simbolos=False
    simbolos="""!"#$%&'()*+,-./"""
    largo=len(contrasena)
    
    for i in range(largo):
        caracter=contrasena[i]
        if (caracter >= "a" and caracter <= "z") or (caracter >= "A" and caracter <= "Z"):
            contiene_letras = True
        elif caracter >= "0" and caracter <= "9":
            contiene_numeros = True
        else:
            for j in range(len(simbolos)):
                if caracter==simbolos[j]:
                    contiene_simbolos=True

    if largo>=12 and contiene_letras and contiene_numeros and contiene_simbolos:
        return "Fuerte"
    elif 8<=largo<=9 and not contiene_numeros and not contiene_simbolos and contiene_letras:
        return "Debil"
    elif contiene_letras and contiene_numeros and not contiene_simbolos:
        return "Media"
    else:
        return "Sin categoria"    

   

    