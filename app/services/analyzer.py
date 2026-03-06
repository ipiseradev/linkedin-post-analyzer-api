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
}

ROLE_KEYWORDS = {
    "Backend Developer": [
        "backend", "api", "fastapi", "django", "flask",
        "postgres", "postgresql", "mysql", "redis"
    ],
    "Frontend Developer": [
        "frontend", "react", "next", "nextjs", "vue", "angular", "ui", "ux"
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
    return re.findall(r"#\w+", text)


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

    if scores[best_role] == 0:
        return "General Software Developer"

    return best_role


def analyze_hook(first_line: str) -> int:
    length = len(first_line)

    if length < 60:
        return 90
    elif length < 100:
        return 75
    elif length < 140:
        return 60
    else:
        return 40


def analyze_readability(text: str) -> int:
    lines = text.split("\n")
    lines = [l for l in lines if l.strip() != ""]

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
    lines = [l for l in text.split("\n") if l.strip() != ""]

    if lines and len(lines[0]) < 80:
        score += 25

    if len(lines) >= 3:
        score += 25

    if any(word in text.lower() for word in ["aprendí", "descubrí", "me di cuenta"]):
        score += 25

    if "?" in text:
        score += 25

    return score


def analyze_post_text(text: str) -> PostAnalyzeResponse:
    text = text.strip()
    lines = [l for l in text.split("\n") if l.strip() != ""]

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
        improvement_tips.append(
            "Acorta la primera línea para hacer el hook más fuerte"
        )

    if readability_score < 80:
        improvement_tips.append(
            "Usa líneas más cortas para mejorar la lectura en LinkedIn"
        )

    if hashtags_count == 0:
        improvement_tips.append(
            "Añade entre 3 y 5 hashtags relevantes"
        )

    if len(text) < 80:
        improvement_tips.append(
            "Agrega más contexto o valor al contenido del post"
        )

    suggested_hashtags = [
        "#backend",
        "#python",
        "#fastapi",
        "#softwareengineering",
        "#buildinpublic",
    ]

    suggested_hashtags = [
        h for h in suggested_hashtags if h not in existing_hashtags
    ]

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