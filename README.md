# 🧠 Smart Resume Analyzer (Python + ML)

A practical Python project that analyzes resumes and matches them against job descriptions using machine learning.

This project is beginner-friendly, resume-worthy, and scalable to GenAI.

---

## 🚀 Features

- Extract text from PDF resumes
- Identify technical skills
- Match resume with job description
- Machine Learning based similarity score
- Clean and modular codebase

---

## 🛠 Tech Stack

- Python 3.9+
- PyPDF
- Scikit-learn (TF-IDF + Cosine Similarity)

---

## 📁 Project Structure

```
resume_analyzer/
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── matcher.py
├── requirements.txt
├── README.md
└── sample_resume.pdf
```

---

## ▶️ How to Run

1. Clone the repository
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Add your resume as `sample_resume.pdf`

4. Run the app
```bash
python app.py
```

5. Paste a job description when prompted

---

## 📈 Output Example

- Extracted Skills
- Resume Match Score (percentage)

---

## 🔮 Future Improvements

- Streamlit web interface
- Advanced NLP (spaCy)
- AI-based resume suggestions
- ATS optimization
```
