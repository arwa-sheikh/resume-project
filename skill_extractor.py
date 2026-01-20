import re
from typing import List

SKILLS_DB = [
    "python", "java", "c++", "sql", "machine learning",
    "deep learning", "nlp", "data analysis",
    "django", "flask", "git", "linux"
]

# Precompile regex patterns for performance and correct word-boundary matching.
_SKILL_PATTERNS = [
    (skill, re.compile(rf"\b{re.escape(skill)}\b", flags=re.IGNORECASE))
    for skill in SKILLS_DB
]

def extract_skills(text: str) -> List[str]:
    """
    Extract known skills from text using word-boundary regex matching.
    Returns a list of matched skills (lowercased) in the order of SKILLS_DB.
    """
    if not text:
        return []

    found = []
    for skill, pattern in _SKILL_PATTERNS:
        if pattern.search(text):
            found.append(skill.lower())
    return found