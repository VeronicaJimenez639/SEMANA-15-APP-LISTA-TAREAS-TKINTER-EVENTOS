# Semana 15 - App Lista de Tareas Tkinter con Eventos

Aplicación de escritorio desarrollada en Python con Tkinter para gestionar tareas mediante una interfaz gráfica, aplicando manejo de eventos de teclado y ratón.

## Funcionalidades

- Añadir tareas
- Marcar tareas como completadas
- Desmarcar tareas
- Eliminar tareas
- Agregar tareas con la tecla Enter
- Marcar tareas con doble clic
- Feedback visual con colores para estado pendiente y completado

## Estructura del proyecto

- `modelos/`: clase `Tarea`
- `servicios/`: lógica de negocio
- `ui/`: interfaz gráfica
- `main.py`: punto de arranque
- `dist/`: contiene el archivo ejecutable generado

## Ejecutar el proyecto

Para ejecutar la aplicación desde Python:

`python main.py`

## Generar el ejecutable

Para generar el archivo ejecutable se utilizó PyInstaller con el siguiente comando:

`pyinstaller --noconsole --onefile --name ListaTareas main.py`

## Archivo ejecutable

El archivo ejecutable generado es:

`dist/ListaTareas.exe`

Este archivo permite abrir la aplicación sin necesidad de ejecutar manualmente el código Python.

## Archivo .gitignore

Se configuró el archivo `.gitignore` para excluir archivos innecesarios generados durante la compilación, como `build/` y `*.spec`.
