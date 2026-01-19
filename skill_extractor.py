SKILLS_DB = [
    "python", "java", "c++", "sql", "machine learning",
    "deep learning", "nlp", "data analysis",
    "django", "flask", "git", "linux"
]

def extract_skills(text: str) -> list:
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return found_skills
