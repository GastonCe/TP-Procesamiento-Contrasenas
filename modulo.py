import validaciones
import analisis
import utilidades
import estadisticas

def bienvenido():
    print("Bienvenido al sistema de procesamiento de contrasenas")

def salir():   
    print("FINALIZO EL PROCESAMIENTO DE CONTRASEÑAS.")
    print("Buena Suerte Y Hasta Luego")

def mostrar_menu():
    opcion=""
    contrasena_verificada=False
    while opcion!="9":
#        print("Bienvenido al sistema de procesamiento de contrasenas")
        print("          ===================Menu======================")
        print("                   1.Ingresar contrasena")
        print("                   2.Validar nivel de seguridad")
        print("                   3.Contar tipos de caracteres")
        print("                   4.Buscar caracter especifico")
        print("                   5.Mostrar contrasena invertida")
        print("                   6.Generar reporte estadistico")
        print("                   7.Verificar si es palindromo")
        print("                   8.Ordenar caracteres de la contrasena")
        print("                   9.Salir")
        opcion=(input("Elija un opcion: "))

        match opcion:
            case "1":    
                contrasena_validada=validaciones.validar_contrasena()
                print(f"La contraseña {contrasena_validada} fue validada")
                contrasena_verficada=True
            case "2":
                if contrasena_verficada:
                    nivel_seguridad=validaciones.validar_nivel_seguridad(contrasena_validada)
                    print(f"Nivel de seguridad: {nivel_seguridad}")
            case "3":
                if contrasena_verficada:
                    analisis.contar_tipos_caracteres(contrasena_validada)
            case "4":
                if contrasena_verficada:
                    caracter=input("ingresar caracter a buscar: ")
                    analisis.buscar_caracter(contrasena_validada,caracter)
            case "5":
                if contrasena_verficada:
                    utilidades.mostrar_contrasena_invetida(contrasena_validada)
            case "6":
                if contrasena_verficada:
                    estadisticas.generar_reporte_estadistico(contrasena_validada)
            case "7":
                if contrasena_verficada:
                    utilidades.verificar_palindromo(contrasena_validada)
            case "8":
                if contrasena_verficada:
                    utilidades.ordenar_contrasena(contrasena_validada)
            case "9":
                salir()
            case _:
                print("opcion no valida")    