from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from matcher import calculate_similarity

def main():
    resume_path = "sample_resume.pdf"

    print("\n📄 Reading resume...")
    resume_text = extract_text_from_pdf(resume_path)

    print("\n🛠 Extracting skills...")
    skills = extract_skills(resume_text)
    print("Skills found:", skills)

    print("\n📊 Resume Matcher")
    job_description = input("\nPaste job description here:\n")

    score = calculate_similarity(resume_text, job_description)
    print(f"\n Resume Match Score: {score}%")

if __name__ == "__main__":
    main()
