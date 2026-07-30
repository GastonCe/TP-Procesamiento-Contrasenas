# Sistema de Procesamiento y Análisis de Contraseñas 🔒

Proyecto modular desarrollado en **Python** para la validación, análisis de seguridad y generación de estadísticas avanzadas sobre cadenas de texto (contraseñas). 

Construido aplicando principios de programación modular, algoritmos de ordenamiento manuales y manejo directo de estructuras de datos.

---

## 🛠️ Características Principales

* **Validación de Seguridad:** Entrada interactiva con control de errores (longitud mínima, restricción de espacios y presencia de caracteres obligatorios).
* **Evaluación de Nivel de Complejidad:** Clasificación dinámica de la contraseña en niveles (*Débil*, *Medio*, *Fuerte*) según criterios de longitud y diversidad de caracteres.
* **Análisis Cuantitativo:** Conteo de tipos de caracteres (letras, números, espacios y símbolos) y cálculo de posiciones.
* **Reporte Estadístico:** Generación de métricas porcentuales y detección de caracteres repetidos consecutivos.
* **Utilidades Algorítmicas:** 
  * Inversión de cadenas y verificación de palíndromos.
  * Ordenamiento de caracteres mediante algoritmo de **Burbuja** (Ascendente / Descendente).
  * Conversión manual a minúsculas mediante manipulación ASCII.

---

## 🏗️ Estructura del Proyecto

````
TP-Procesamiento-Contrasenas/
│
├── main.py          # Punto de entrada principal
├── modulo.py        # Menú interactivo y orquestación del flujo de usuario
├── validaciones.py  # Lógica de validación y cálculo de nivel de seguridad
├── analisis.py      # Búsqueda y conteo de tipos de caracteres
├── estadisticas.py  # Muestreo estadístico y porcentajes
└── utilidades.py    # Algoritmo de burbuja, inversión y verificación de palíndromos
````

---
🚀 Cómo Ejecutarlo

1. Clonar el repositorio:
   git clone https://github.com/GastonCe/TP-Procesamiento-Contrasenas.git

2. Navegar a la carpeta del proyecto:
   cd TP-Procesamiento-Contrasenas

3. Ejecutar el script principal:
   python main.py

💻 Tecnologías Utilizadas

 * **Lenguaje:** Python 3.x
 * **Conceptos:** Modularización, Algoritmo de Ordenamiento por Burbuja, Código ASCII, Validaciones.
