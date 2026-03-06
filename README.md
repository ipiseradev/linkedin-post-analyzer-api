LinkedIn Post Analyzer API

API construida con FastAPI que analiza publicaciones de LinkedIn y estima su potencial de engagement.

El objetivo del proyecto es analizar automáticamente distintos aspectos de un post técnico y devolver scores, insights y sugerencias para mejorarlo.

Este proyecto surge de experimentar con cómo funciona el engagement en contenido técnico dentro de LinkedIn.

Features

La API analiza automáticamente:

Fuerza del hook (primera línea)

Legibilidad del contenido

Estructura narrativa del post

Uso de hashtags

Tecnologías detectadas dentro del contenido

Rol técnico estimado del post (Backend, Frontend, DevOps, etc)

Sugerencias automáticas de mejora

Scores que devuelve

La API calcula los siguientes indicadores:

Score	Descripción
hook_score	Fuerza de la primera línea
readability_score	Facilidad de lectura
story_score	Calidad de la estructura narrativa
viral_score	Score general estimado de engagement

También devuelve:

suggested_hashtags

improvement_tips

technologies

role_detected

API Endpoint
POST /posts/analyze

Analiza un post de LinkedIn y devuelve métricas estimadas de engagement.

Ejemplo de request
{
  "text": "Estoy construyendo una API con Python y FastAPI. El backend también usa Docker y PostgreSQL. ¿Qué les parece?"
}
Ejemplo de respuesta
{
  "viral_score": 46,
  "hook_score": 60,
  "readability_score": 55,
  "story_score": 25,
  "suggested_hashtags": [
    "#backend",
    "#python",
    "#fastapi",
    "#softwareengineering",
    "#buildinpublic"
  ],
  "improvement_tips": [
    "Acorta la primera línea para hacer el hook más fuerte",
    "Usa líneas más cortas para mejorar la lectura en LinkedIn",
    "Añade entre 3 y 5 hashtags relevantes"
  ],
  "technologies": [
    "Python",
    "FastAPI",
    "Docker",
    "PostgreSQL"
  ],
  "role_detected": "Backend Developer"
}
Demo
<img width="1919" height="1033" src="https://github.com/user-attachments/assets/968bd136-6172-4868-8066-ee727aaacb87" />
Tech Stack

Python

FastAPI

Regex (text analysis)

Postman (API testing)

Cómo correr el proyecto
1️⃣ Clonar el repositorio
git clone https://github.com/ipiseradev/linkedin-post-analyzer-api
2️⃣ Instalar dependencias
pip install -r requirements.txt
3️⃣ Levantar el servidor
uvicorn app.main:app --reload
4️⃣ Abrir documentación automática
http://127.0.0.1:8000/docs
Ideas futuras

Mejor análisis de estructura narrativa

Detección más precisa de storytelling

Optimización automática de hashtags

Score más avanzado de potencial viral

Reescritura automática de posts para mejorar engagement

Autor

Ignacio Pisera

Full Stack Developer

Python • FastAPI • Docker • Linux
