# knowledge_loader.py

import json
from pathlib import Path


# Find the project folder
BASE_DIR = Path(__file__).resolve().parent

# Find the knowledge folder
KNOWLEDGE_DIR = BASE_DIR / "knowledge"


def load_json(filename):
    """
    Loads one JSON file from the knowledge folder.
    """

    file_path = KNOWLEDGE_DIR / filename

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"ERROR: File not found: {file_path}")
        return {}

    except json.JSONDecodeError:
        print(f"ERROR: Invalid JSON in: {file_path}")
        return {}


def load_knowledge():
    """
    Loads all of Srija's knowledge files
    and combines them into one dictionary.
    """

    knowledge = {}

    knowledge["profile"] = load_json("profile.json")
    knowledge["education"] = load_json("education.json")
    knowledge["skills"] = load_json("skills.json")
    knowledge["experience"] = load_json("experience.json")
    knowledge["projects"] = load_json("projects.json")
    knowledge["certifications"] = load_json("certifications.json")

    return knowledge


def get_knowledge_text():
    """
    Converts the complete knowledge base into
    readable text that can later be given to the LLM.
    """

    knowledge = load_knowledge()

    return json.dumps(
        knowledge,
        indent=2,
        ensure_ascii=False
    )


# Test the knowledge loader
if __name__ == "__main__":

    print("=" * 60)
    print("SRIJA AI - KNOWLEDGE BASE TEST")
    print("=" * 60)

    knowledge = load_knowledge()

    print("\nKnowledge sections loaded:")

    for section in knowledge:
        print(f"✓ {section}")

    print("\nTotal sections:", len(knowledge))

    print("\nSample profile information:")

    print(
        json.dumps(
            knowledge["profile"],
            indent=2,
            ensure_ascii=False
        )
    )

    print("\n" + "=" * 60)
    print("KNOWLEDGE LOADER WORKING SUCCESSFULLY")
    print("=" * 60)