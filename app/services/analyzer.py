import re
from app.schemas.post import PostAnalyzeResponse


def count_hashtags(text: str) -> int:
    return len(re.findall(r"#\w+", text))


def extract_hashtags(text: str) -> list[str]:
    return re.findall(r"#\w+", text)


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


# NUEVA FUNCIÓN: analiza estructura narrativa
def analyze_story_structure(text: str) -> int:

    score = 0
    lines = [l for l in text.split("\n") if l.strip() != ""]

    # hook corto
    if lines and len(lines[0]) < 80:
        score += 25

    # varios párrafos (storytelling)
    if len(lines) >= 3:
        score += 25

    # insight
    if any(word in text.lower() for word in ["aprendí", "descubrí", "me di cuenta"]):
        score += 25

    # pregunta final
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
    improvement_tips=improvement_tips
)