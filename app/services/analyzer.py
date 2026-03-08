import re
from app.schemas.post import PostAnalyzeResponse

TECH_KEYWORDS = {
    "python": "Python",
    "fastapi": "FastAPI",
    "django": "Django",
    "flask": "Flask",
    "react": "React",
    "node": "Node.js",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "mysql": "MySQL",
    "redis": "Redis",
    "aws": "AWS",
    "gcp": "GCP",
    "azure": "Azure",
    "spring": "Spring Boot",
    "spring boot": "Spring Boot",
    "java": "Java",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "html": "HTML",
    "css": "CSS",
}

ROLE_KEYWORDS = {
    "Backend Developer": [
        "backend", "api", "fastapi", "django", "flask",
        "postgres", "postgresql", "mysql", "redis", "spring", "java"
    ],
    "Frontend Developer": [
        "frontend", "react", "next", "nextjs", "vue", "angular",
        "ui", "ux", "html", "css", "javascript", "typescript"
    ],
    "DevOps Engineer": [
        "docker", "kubernetes", "ci/cd", "devops", "aws", "gcp", "azure", "terraform"
    ],
    "Data Engineer": [
        "etl", "pipeline", "data engineer", "spark", "airflow", "warehouse", "bigquery"
    ],
    "AI Engineer": [
        "ai", "ml", "machine learning", "llm", "genai", "rag", "nlp"
    ],
}


def count_hashtags(text: str) -> int:
    return len(re.findall(r"#\w+", text))


def extract_hashtags(text: str) -> list[str]:
    return re.findall(r"#\w+", text.lower())


def detect_technologies(text: str) -> list[str]:
    text_lower = text.lower()
    detected = []

    for keyword, name in TECH_KEYWORDS.items():
        if keyword in text_lower:
            detected.append(name)

    return sorted(list(set(detected)))


def detect_role_from_post(text: str) -> str:
    text_lower = text.lower()
    scores: dict[str, int] = {}

    for role, keywords in ROLE_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            if keyword in text_lower:
                score += 1
        scores[role] = score

    best_role = max(scores, key=scores.get)
    best_score = scores[best_role]

    if best_score == 0:
        return "General Software Developer"

    tied_roles = [role for role, score in scores.items() if score == best_score]
    if len(tied_roles) > 1:
        return "General Software Developer"

    return best_role


def analyze_hook(first_line: str) -> int:
    score = 40
    first_line_lower = first_line.lower()
    length = len(first_line)

    if length < 80:
        score += 20
    elif length < 120:
        score += 10

    if "?" in first_line:
        score += 10

    if re.search(r"\b\d+\b", first_line):
        score += 10

    if any(word in first_line_lower for word in ["hoy", "aprendí", "descubrí", "construí", "lancé"]):
        score += 10

    return min(score, 100)


def analyze_readability(text: str) -> int:
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    if not lines:
        return 20

    avg = sum(len(l) for l in lines) / len(lines)

    if avg < 60:
        return 90
    elif avg < 100:
        return 75
    elif avg < 140:
        return 55
    else:
        return 35


def analyze_story_structure(text: str) -> int:
    score = 0
    text_lower = text.lower()
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    if lines and len(lines[0]) < 80:
        score += 20

    if len(lines) >= 3:
        score += 20

    if any(word in text_lower for word in ["aprendí", "descubrí", "me di cuenta", "empecé", "hoy", "finalmente"]):
        score += 30

    if "?" in text:
        score += 15

    if any(word in text_lower for word in ["problema", "solución", "resultado", "proceso"]):
        score += 15

    return min(score, 100)


def build_suggested_hashtags(technologies: list[str], role_detected: str) -> list[str]:
    tags = set()

    role_map = {
        "Backend Developer": ["#backend", "#apidevelopment"],
        "Frontend Developer": ["#frontend", "#webdevelopment"],
        "DevOps Engineer": ["#devops", "#cloud"],
        "Data Engineer": ["#dataengineering", "#bigdata"],
        "AI Engineer": ["#ai", "#machinelearning"],
        "General Software Developer": ["#softwareengineering", "#programming"],
    }

    tech_map = {
        "Python": "#python",
        "FastAPI": "#fastapi",
        "Django": "#django",
        "Flask": "#flask",
        "React": "#reactjs",
        "Node.js": "#nodejs",
        "Docker": "#docker",
        "Kubernetes": "#kubernetes",
        "PostgreSQL": "#postgresql",
        "MySQL": "#mysql",
        "Redis": "#redis",
        "AWS": "#aws",
        "GCP": "#gcp",
        "Azure": "#azure",
        "Spring Boot": "#springboot",
        "Java": "#java",
        "JavaScript": "#javascript",
        "TypeScript": "#typescript",
        "HTML": "#html",
        "CSS": "#css",
    }

    for tag in role_map.get(role_detected, []):
        tags.add(tag)

    for tech in technologies:
        if tech in tech_map:
            tags.add(tech_map[tech])

    tags.add("#buildinpublic")

    return list(tags)[:5]


def analyze_post_text(text: str) -> PostAnalyzeResponse:
    text = text.strip()
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    first_line = lines[0] if lines else text

    hook_score = analyze_hook(first_line)
    readability_score = analyze_readability(text)
    story_score = analyze_story_structure(text)

    hashtags_count = count_hashtags(text)
    existing_hashtags = extract_hashtags(text)
    technologies = detect_technologies(text)
    role_detected = detect_role_from_post(text)

    viral_score = int((hook_score + readability_score + story_score) / 3)

    improvement_tips = []

    if len(first_line) > 60:
        improvement_tips.append("Acorta la primera línea para hacer el hook más fuerte")

    if readability_score < 80:
        improvement_tips.append("Usa líneas más cortas para mejorar la lectura en LinkedIn")

    if hashtags_count == 0:
        improvement_tips.append("Añade entre 3 y 5 hashtags relevantes")

    if len(text) < 80:
        improvement_tips.append("Agrega más contexto o valor al contenido del post")

    if "?" not in text:
        improvement_tips.append("Agregar una pregunta al final puede aumentar la interacción")

    if len(lines) < 3:
        improvement_tips.append("Divide el post en más bloques para mejorar la estructura visual")

    improvement_tips = list(dict.fromkeys(improvement_tips))

    suggested_hashtags = build_suggested_hashtags(technologies, role_detected)
    suggested_hashtags = [h for h in suggested_hashtags if h.lower() not in existing_hashtags]

    return PostAnalyzeResponse(
        viral_score=viral_score,
        hook_score=hook_score,
        readability_score=readability_score,
        story_score=story_score,
        suggested_hashtags=suggested_hashtags,
        improvement_tips=improvement_tips,
        technologies=technologies,
        role_detected=role_detected,
    )