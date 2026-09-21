# agent.py

import json
import re
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_FILE = BASE_DIR / "knowledge" / "interview_knowledge.json"


# ============================================================
# LOAD INTERVIEW KNOWLEDGE
# ============================================================

def load_interview_knowledge():
    try:
        with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"ERROR: File not found: {KNOWLEDGE_FILE}")
        return {}

    except json.JSONDecodeError as error:
        print(f"ERROR: Invalid JSON: {error}")
        return {}


INTERVIEW_KNOWLEDGE = load_interview_knowledge()


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):
    text = text.lower().strip()

    # Remove punctuation
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text


# ============================================================
# INTENT DETECTION
# ============================================================

def detect_intent(question):

    q = normalize_text(question)

    # --------------------------------------------------------
    # GREETING
    # --------------------------------------------------------

    if q in [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return "greeting"


    # --------------------------------------------------------
    # INTRODUCTION / PROFESSIONAL SUMMARY
    # --------------------------------------------------------

    if any(phrase in q for phrase in [
        "tell me about yourself",
        "introduce yourself",
        "give me your introduction",
        "walk me through your background",
        "tell me about your background",
        "who is srija",
        "tell me about srija",
        "professional summary",
        "summarize your profile",
        "summary of your profile"
    ]):
        return "introduction"


    # --------------------------------------------------------
    # EDUCATION
    # --------------------------------------------------------

    if any(phrase in q for phrase in [
        "educational background",
        "academic background",
        "tell me about your education",
        "what is your education",
        "what did you study",
        "what is your degree",
        "where did you study",
        "which college",
        "academic qualifications",
        "what is your cgpa",
        "what is your btech",
        "when will you graduate",
        "graduation"
    ]):
        return "education"


    # --------------------------------------------------------
    # EXPERIENCE OVERVIEW
    # --------------------------------------------------------

    if any(phrase in q for phrase in [
        "work experience",
        "professional experience",
        "tell me about your experience",
        "what experience do you have",
        "walk me through your experience",
        "what internships have you done",
        "tell me about your internships"
    ]):
        return "experience_overview"


    # ========================================================
    # TAYANA / AI INTERNSHIP
    # ========================================================

    # Generative AI internship questions
    if any(phrase in q for phrase in [
        "did you work with generative ai",
        "what did you do with generative ai",
        "generative ai experience",
        "how is generative ai related to your internship"
    ]):
        return "generative_ai_internship"


    # NLP internship questions
    if any(phrase in q for phrase in [
        "did you work with nlp",
        "what did you do with nlp",
        "nlp experience",
        "how did you use nlp during your internship"
    ]):
        return "nlp_internship"


    # Teamwork questions
    if any(phrase in q for phrase in [
        "did you work in a team",
        "did you collaborate with a team",
        "how did you work with your team",
        "cross functional teams",
        "team during your internship"
    ]):
        return "internship_teamwork"


    # Internship responsibilities
    if any(phrase in q for phrase in [
        "responsibilities during your internship",
        "what responsibilities did you have",
        "what did you do as an ai intern",
        "main responsibilities at tayana",
        "tasks did you perform during your internship"
    ]):
        return "ai_internship_responsibilities"


    # Internship technologies
    if any(phrase in q for phrase in [
        "technologies did you use during your ai internship",
        "tools did you use at tayana",
        "technologies did you work with at tayana",
        "which programming language did you use during your internship",
        "how did you use python during your internship"
    ]):
        return "ai_internship_technologies"


    # General Tayana internship
    if any(phrase in q for phrase in [
        "ai internship",
        "internship at tayana",
        "what did you do at tayana",
        "what did you work on during your ai internship",
        "role at tayana",
        "tayana solutions",
        "describe your ai internship",
        "kind of work did you do at tayana"
    ]):
        return "ai_internship"


    # Specific AI internship role/contribution
    if any(phrase in q for phrase in [
        "role as an ai intern",
        "contribution at tayana",
        "contribute during your ai internship",
        "responsibility at tayana solutions"
    ]):
        return "ai_internship_role"


    # ========================================================
    # SALESFORCE INTERNSHIP
    # ========================================================

    if any(phrase in q for phrase in [
        "salesforce internship",
        "salesforce experience",
        "agentblazer experience",
        "agentblazer program",
        "what did you do with apex",
        "what did you do with lwc"
    ]):
        return "salesforce_internship"


    if any(phrase in q for phrase in [
        "technologies did you use in your salesforce",
        "what is apex",
        "how did you use apex",
        "what are lightning web components",
        "what are lwc",
        "how did you use lwc",
        "what did you develop using salesforce"
    ]):
        return "salesforce_technologies"


    if any(phrase in q for phrase in [
        "what did you achieve in salesforce",
        "what superbadges",
        "salesforce achievements",
        "what did you accomplish in the agentblazer"
    ]):
        return "salesforce_achievements"


    # ========================================================
    # PROJECTS
    # ========================================================

    # Career Recommender
    if any(phrase in q for phrase in [
        "career recommender",
        "career recommendation project",
        "roadmap generator",
        "career roadmap",
        "career recommendation system"
    ]):

        # Purpose
        if any(phrase in q for phrase in [
            "why did you build",
            "purpose",
            "problem does",
            "why is",
            "objective"
        ]):
            return "career_project_purpose"


        # Role / contribution
        if any(phrase in q for phrase in [
            "what did you do",
            "your role",
            "your contribution",
            "what did you implement"
        ]):
            return "career_project_work"


        # Technologies
        if any(phrase in q for phrase in [
            "technologies",
            "techniques",
            "algorithms",
            "machine learning",
            "nlp"
        ]):
            return "career_project_technologies"


        # Challenges
        if any(phrase in q for phrase in [
            "challenge",
            "problem",
            "difficult",
            "overcome"
        ]):
            return "career_project_challenges"


        return "career_project"


    # --------------------------------------------------------
    # Fraud Detection
    # --------------------------------------------------------

    if any(phrase in q for phrase in [
        "fraud detection",
        "credit card fraud",
        "fraud detection system",
        "fraud project",
        "suspicious transactions"
    ]):

        # Purpose
        if any(phrase in q for phrase in [
            "why did you build",
            "purpose",
            "problem does",
            "why is fraud",
            "objective"
        ]):
            return "fraud_project_purpose"


        # Evaluation
        if any(phrase in q for phrase in [
            "evaluate",
            "evaluation",
            "test the model",
            "prediction accuracy",
            "accuracy"
        ]):
            return "fraud_project_evaluation"


        # Role / contribution
        if any(phrase in q for phrase in [
            "what did you do",
            "your role",
            "your contribution",
            "what did you implement"
        ]):
            return "fraud_project_work"


        # Technologies / algorithms
        if any(phrase in q for phrase in [
            "technologies",
            "algorithms",
            "machine learning techniques",
            "what did you use"
        ]):
            return "fraud_project_technologies"


        return "fraud_project"


    # --------------------------------------------------------
    # General project questions
    # --------------------------------------------------------

    if any(phrase in q for phrase in [
        "tell me about your projects",
        "what projects have you worked on",
        "what are your main projects",
        "walk me through your projects",
        "describe your projects",
        "which projects have you built"
    ]):
        return "projects_overview"


    # --------------------------------------------------------
    # Project challenges
    # --------------------------------------------------------

    if any(phrase in q for phrase in [
        "challenges did you face in your projects",
        "technical challenges did you face",
        "problems did you face while building your projects",
        "overcome challenges in your projects"
    ]):
        return "project_challenges"


    # --------------------------------------------------------
    # Project learning
    # --------------------------------------------------------

    if any(phrase in q for phrase in [
        "what did you learn from your projects",
        "what did you learn while building your projects",
        "what skills did you gain from your projects",
        "what did your projects teach you"
    ]):
        return "project_learning"


    # ========================================================
    # TECHNICAL SKILLS
    # ========================================================

    if any(phrase in q for phrase in [
        "technical skills",
        "technologies do you know",
        "programming languages do you know",
        "programming languages are you familiar",
        "technical background",
        "tools and technologies"
    ]):
        return "technical_skills"


    # Python
    if any(phrase in q for phrase in [
        "experience with python",
        "used python",
        "comfortable with python",
        "done using python"
    ]):
        return "python"


    # Java
    if any(phrase in q for phrase in [
        "experience with java",
        "do you know java",
        "comfortable with java"
    ]):
        return "java"


    # SQL / MySQL
    if any(phrase in q for phrase in [
        "experience with sql",
        "do you know sql",
        "what databases do you know",
        "experience with mysql",
        "familiar with databases"
    ]):
        return "sql_database"


    # AI / ML
    if any(phrase in q for phrase in [
        "experience in ai",
        "experience in machine learning",
        "ai ml skills",
        "ai technologies",
        "machine learning skills"
    ]):
        return "ai_ml"


    # ========================================================
    # CERTIFICATIONS
    # ========================================================

    if any(phrase in q for phrase in [
        "certifications",
        "certificates",
        "technical certifications"
    ]):
        return "certifications"


    # ========================================================
    # SOFT SKILLS
    # ========================================================

    if any(phrase in q for phrase in [
        "soft skills",
        "your strengths",
        "key strengths",
        "interpersonal skills"
    ]):
        return "soft_skills"


    # ========================================================
    # CAREER INTERESTS
    # ========================================================

    if any(phrase in q for phrase in [
        "career interests",
        "what are you interested in",
        "area do you want to work",
        "what kind of role",
        "career goals",
        "type of work interests"
    ]):
        return "career_interests"


    # ========================================================
    # WHY AI
    # ========================================================

    if any(phrase in q for phrase in [
        "why are you interested in ai",
        "why did you choose ai",
        "why did you choose artificial intelligence",
        "why do you want to work in ai",
        "why ai engineering"
    ]):
        return "why_ai"


    return None


# ============================================================
# FIND ANSWER FOR INTENT
# ============================================================

def get_answer_for_intent(intent):

    if not intent:
        return None

    category = INTERVIEW_KNOWLEDGE.get(intent)

    if not category:
        return None

    return category.get("answer")


# ============================================================
# MATCH STORED QUESTIONS
# ============================================================

def find_question_match(question):

    normalized_question = normalize_text(question)

    if not normalized_question:
        return None

    best_score = 0
    best_answer = None

    for category_name, category_data in INTERVIEW_KNOWLEDGE.items():

        questions = category_data.get("questions", [])

        for stored_question in questions:

            normalized_stored = normalize_text(stored_question)

            # Exact match
            if normalized_question == normalized_stored:
                return category_data.get("answer")


            # Simple word overlap
            user_words = set(normalized_question.split())
            stored_words = set(normalized_stored.split())

            if not user_words or not stored_words:
                continue

            common_words = user_words & stored_words

            score = len(common_words) / max(len(user_words), 1)

            if score > best_score:
                best_score = score
                best_answer = category_data.get("answer")


    # Only accept reasonably strong matches
    if best_score >= 0.70:
        return best_answer

    return None


# ============================================================
# GUARDRAIL
# ============================================================

def unrelated_response():

    return (
        "I'm designed to answer questions about Srija's "
        "background, education, skills, internships, "
        "projects, experience, and technical work. "
        "I can't help with unrelated topics."
    )


# ============================================================
# MAIN AGENT
# ============================================================

def ask_agent(question):

    if not question or not question.strip():

        return "Please ask me a question about Srija."


    question = question.strip()


    # --------------------------------------------------------
    # STEP 1: INTENT DETECTION
    # --------------------------------------------------------

    intent = detect_intent(question)


    # --------------------------------------------------------
    # STEP 2: DIRECT INTENT ANSWER
    # --------------------------------------------------------

    if intent:

        answer = get_answer_for_intent(intent)

        if answer:
            return answer


    # --------------------------------------------------------
    # STEP 3: STORED QUESTION MATCH
    # --------------------------------------------------------

    answer = find_question_match(question)

    if answer:
        return answer


    # --------------------------------------------------------
    # STEP 4: UNKNOWN / OUT OF SCOPE
    # --------------------------------------------------------

    return unrelated_response()