# Generador de Resúmenes con IA

Aplicación web que permite generar resúmenes automáticos de textos usando inteligencia artificial.

## Tecnologías utilizadas

- Frontend: HTML, CSS, JavaScript
- Backend: Python + FastAPI
- IA: modelo de resumen de HuggingFace

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
2. Pegar un texto
3. Seleccionar tipo de resumen
4. Presionar "Generar resumen"