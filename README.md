# LinkedIn Post Analyzer API

API construida con **FastAPI** que analiza publicaciones de LinkedIn y estima su potencial de engagement.

El objetivo es analizar automáticamente distintos aspectos de un post técnico y devolver **scores, insights y sugerencias para mejorarlo**.

Este proyecto surge de experimentar con cómo funciona el engagement en contenido técnico dentro de LinkedIn.

---

## Features

La API analiza automáticamente:

- Fuerza del **hook** (primera línea)
- **Legibilidad** del contenido
- **Estructura narrativa** del post
- Uso de **hashtags**
- **Tecnologías detectadas** dentro del contenido
- **Rol técnico estimado** del post (Backend, Frontend, DevOps, etc.)
- **Sugerencias automáticas de mejora**

---

## Scores que devuelve

La API calcula los siguientes indicadores:

- `hook_score` → fuerza de la primera línea
- `readability_score` → facilidad de lectura
- `story_score` → calidad de la estructura narrativa
- `viral_score` → score general estimado de engagement

También devuelve:

- `suggested_hashtags`
- `improvement_tips`
- `technologies`
- `role_detected`

---

## API Endpoint

```bash
POST /posts/analyze

Demo
<img width="1918" height="1017" alt="descarga" src="https://github.com/user-attachments/assets/04e37ce1-8bcb-4a20-a4ba-eb1213a7b915" />


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
    "Docker",
    "FastAPI",
    "PostgreSQL",
    "Python"
  ],
  "role_detected": "Backend Developer"
}


Tech Stack
- Python
- FasAPI
- Regex(análisis de texto)
- Postman(API testing)

Cómo correr el proyecto
1. Instalar dependencias
pip install -r requirements.txt

2. Levantar el servidor
uvicorn app.main:app --reload

3. Abrir documentación
http://127.0.0.1:8000/docs

Ideas futuras
- Mejor análisis de estructura narrativa

- Detección más precisa de storytelling

- Optimización automática de hashtags

- Score más avanzado de potencial viral

- Reescritura automática de posts para mejorar engagement

Autor

Ignacio Pisera

Full Stack Developer
Python • FastAPI • Docker • Linux