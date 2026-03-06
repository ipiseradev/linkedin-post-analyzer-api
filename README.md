# LinkedIn Post Analyzer API

API construida con **FastAPI** que analiza publicaciones de LinkedIn y estima su potencial de engagement.

El objetivo es evaluar automáticamente distintos aspectos de un post y devolver sugerencias para mejorarlo.

---

# Qué analiza la API

La API evalúa:

• Fuerza del **hook** (primera línea)  
• **Legibilidad** del contenido  
• Uso de **hashtags**  
• **Estructura narrativa** del post  
• **Sugerencias de mejora**

---

# Scores que devuelve

La API calcula:

- `hook_score` → fuerza de la primera línea
- `readability_score` → facilidad de lectura
- `story_score` → estructura narrativa del contenido
- `viral_score` → score general estimado

---

# Ejemplo de uso

POST request:
## API Endpoint

POST /posts/analyze
Analiza un post de LinkedIn y devuelve un score estimado de engagement.

## DEMO
<img width="1918" height="1017" alt="descarga" src="https://github.com/user-attachments/assets/04e37ce1-8bcb-4a20-a4ba-eb1213a7b915" />


Body:

```json
{
  "text": "Construyendo una API con FastAPI para analizar posts de LinkedIn.\n\nEstoy probando cómo mejorar el engagement de mis publicaciones.\n\n#backend #python"
}

Respueta:
{
  "viral_score": 71,
  "hook_score": 75,
  "readability_score": 90,
  "story_score": 50,
  "suggested_hashtags": [
    "#fastapi",
    "#softwareengineering",
    "#buildinpublic"
  ],
  "improvement_tips": [
    "Acorta la primera línea para hacer el hook más fuerte"
  ]
}

  Stack

  -Python
  -FastAPI
  -Regex (análisis de texto)
  -Postman para testear el endpoint

  Cómo correr el proyecto:
  

  2️⃣ Levantar el servidor
   uvicorn app.main:app --reload

  
   3️⃣ Abrir documentación
   http://127.0.0.1:8000/docs

   Ideas futuras

   -Mejor análisis de estructura narrativa

   -Detección de storytelling

   -Optimización automática de hashtags

   - Score más preciso de potencial viral

    Autor

   Ignacio Pisera

   Full Stack Developer
   Python • FastAPI • Docker • Linux
