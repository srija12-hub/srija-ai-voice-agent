# guardrails.py

# Topics that our AI agent is designed to answer.
ALLOWED_TOPICS = [
    "profile",
    "background",
    "education",
    "skills",
    "technical skills",
    "programming",
    "internship",
    "experience",
    "projects",
    "project",
    "certifications",
    "career",
    "artificial intelligence",
    "ai",
    "machine learning",
    "ml",
    "deep learning",
    "nlp",
    "generative ai",
    "software development",
    "developer",
    "work",
    "responsibilities",
    "achievements"
]


def check_guardrail(question):
    """
    Checks whether the question is related to Srija's
    professional background and technical work.
    """

    question = question.lower().strip()

    # Empty question
    if not question:
        return False

    # Check whether the question contains an allowed topic
    for topic in ALLOWED_TOPICS:
        if topic in question:
            return True

    return False


def guardrail_response(question):
    """
    Returns a response if the question is outside
    the intended scope of the AI agent.
    """

    if check_guardrail(question):
        return None

    return (
        "I'm designed to answer questions about Srija's "
        "background, skills, projects, experience, education, "
        "and technical work. I can't help with unrelated topics."
    )


# Test the guardrail
if __name__ == "__main__":

    questions = [
        "Tell me about Srija's skills",
        "What projects has Srija worked on?",
        "Tell me about her AI internship",
        "What is the weather today?",
        "Who is the Prime Minister of India?"
    ]

    for question in questions:

        result = guardrail_response(question)

        print("\nQuestion:", question)

        if result:
            print("Guardrail:", result)
        else:
            print("Guardrail: ALLOWED")