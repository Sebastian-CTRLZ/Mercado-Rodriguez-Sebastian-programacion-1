# Mercado-Rodriguez-Sebastian-programacion-1.
# Repositorio de Evidencias de Clase

Este repositorio tiene como propósito principal almacenar, estructurar y documentar los trabajos, prácticas y proyectos desarrollados durante el ciclo académico como evidencia de aprendizaje.

---

## 📁 Estructura del Repositorio

A continuación se detalla la organización de las carpetas dentro de este proyecto:

* **`practicas/`**: Contiene los ejercicios prácticos, actividades guiadas, pruebas de código y pequeñas entregas semanales realizadas en clase o en casa.
* **`proyectos/`**: Destinada a almacenar proyectos integradores de mayor escala, trabajos finales o desarrollos en equipo.
* **`README.md`**: Archivo de presentación principal que describe el contenido del repositorio, las guías de uso y la bitácora del entorno de desarrollo.

---

## 🛠️ Bitácora de Instalación del IDE

* **Entorno / Editor Instalado:** Visual Studio Code (VS Code)
* **Versión:** 1.93+ (o la versión actual que tengas instalada)
* **Sistema Operativo:** Windows / macOS / Linux

### Configuración e Instalación
1. Se descargó el instalador ejecutable desde el sitio web oficial ([code.visualstudio.com](https://code.visualstudio.com/)).
2. Se ejecutó el asistente de instalación activando las opciones de integración con el Explorador de archivos (*"Agregar la acción 'Abrir con Code' al menú contextual"*).
3. Se instalaron extensiones base según las necesidades del curso (ej. complementos para formateo de código, lenguaje de programación en uso y soporte para Git).

### Dificultades / Problemas Presentados y Soluciones

* **Problema:** Al intentar ejecutar el comando `code .` desde la terminal o consola de comandos, el sistema no reconocía el comando como un ejecutable válido.
  * **Solución:** Se abrió la paleta de comandos en VS Code con `Ctrl + Shift + P` (o `Cmd + Shift + P`), se buscó `Shell Command: Install 'code' command in PATH` y se seleccionó la opción para agregar el comando a las variables de entorno del sistema. Tras reiniciar la terminal, el comando funcionó correctamente.

* **Problema:** Git Bash o la terminal integrada no detectaba correctamente los comandos de Git instalados en el sistema.
  * **Solución:** Se verificó que Git estuviera instalado independientemente desde su sitio oficial y se reinició la sesión del editor para que tomara la ruta de instalación global.
