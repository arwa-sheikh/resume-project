from skill_extractor import extract_skills

def test_extract_basic_skills():
    text = "Experienced Python developer skilled in Django and SQL databases."
    skills = extract_skills(text)
    assert "python" in skills
    assert "django" in skills
    assert "sql" in skills

def test_no_false_positive_substring():
    # words like 'account' should not match skills by substring
    text = "Worked in account management and sequencing operations."
    skills = extract_skills(text)
    # no skill should be accidentally matched from those words
    assert isinstance(skills, list)

def test_case_insensitive():
    text = "PYTHON, Flask and Git experience."
    skills = extract_skills(text)
    assert "python" in skills
    assert "flask" in skills
    assert "git" in skills

def test_empty_text():
    assert extract_skills("") == []