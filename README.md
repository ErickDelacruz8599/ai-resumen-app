# Generador de Resúmenes con IA

Aplicación web que permite generar resúmenes automáticos de textos usando inteligencia artificial.  
El sistema incluye autenticación de usuarios mediante reconocimiento facial (Face ID), almacenamiento de datos en una base de datos y registro del historial de resúmenes generados.

## Funcionalidades

- Generación automática de resúmenes usando inteligencia artificial
- Inicio de sesión seguro mediante reconocimiento facial (Face ID)
- Registro y autenticación de usuarios
- Guardado automático del historial de resúmenes
- Interfaz web simple e intuitiva
- Posibilidad de seleccionar diferentes tipos de resumen (corto, medio o detallado)

## Tecnologías utilizadas

- Frontend: HTML, CSS, JavaScript
- Backend: Python + FastAPI
- Inteligencia Artificial: modelo de resumen de HuggingFace
- Autenticación: reconocimiento facial (Face ID)
- Base de datos: SQLite o PostgreSQL para almacenar usuarios y resúmenes
- API: comunicación entre frontend y backend mediante REST API

## Arquitectura del sistema

El sistema sigue una arquitectura cliente-servidor:

- El frontend permite que el usuario ingrese el texto.
- El backend procesa la solicitud y envía el texto al modelo de IA.
- El modelo de IA genera el resumen automáticamente.
- La base de datos guarda la información del usuario y el historial de resúmenes.

## Instalación

1. Clonar el repositorio

git clone URL_DEL_REPOSITORIO

2. Entrar al backend

cd backend

3. Crear entorno virtual

python -m venv venv

4. Activar entorno

Windows:  
venv\Scripts\activate

5. Instalar dependencias

pip install -r requirements.txt

6. Ejecutar servidor

uvicorn main:app --reload

## Uso

1. Abrir el archivo frontend/index.html
2. Registrarse o iniciar sesión usando reconocimiento facial
3. Ingresar el texto que se desea resumir
4. Seleccionar el tipo de resumen
5. Presionar "Generar resumen"
6. El sistema mostrará el resumen generado por la IA
7. El resumen quedará almacenado en la base de datos para consultas futuras

## Estructura del proyecto

frontend/ → interfaz gráfica del usuario  
backend/ → API y lógica del sistema  
database/ → gestión de base de datos  
models/ → modelo de inteligencia artificial  
auth/ → sistema de autenticación facial

## Posibles mejoras futuras

- Exportar resúmenes en PDF
- Traducción automática del texto
- Integración con aplicaciones educativas
- Historial avanzado de documentos resumidos

## Autor

Proyecto desarrollado con fines académicos.