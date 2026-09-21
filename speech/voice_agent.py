import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from speech.speech_to_text import SpeechToText
from speech.text_to_speech import TextToSpeech
from agent import ask_agent


def main():

    print("=" * 60)
    print("          SRIJA AI - DEVELOPER VOICE AGENT")
    print("=" * 60)

    print("\n🎤 Microphone: Ready")
    print("🧠 AI Agent: Ready")
    print("🔊 Voice: Ready")
    print("\nSpeak your question.")
    print("Say 'exit' to stop.\n")

    # Create voice components
    stt = SpeechToText()
    tts = TextToSpeech()

    while True:

        try:

            # -----------------------------------------
            # 1. LISTEN TO INTERVIEWER
            # -----------------------------------------

            question = stt.listen()

            if not question:
                continue

            # -----------------------------------------
            # 2. CHECK EXIT
            # -----------------------------------------

            if question.lower().strip() in [
                "exit",
                "quit",
                "stop"
            ]:

                goodbye = "Goodbye. Thank you for speaking with me."

                print(f"\n🧠 Srija AI: {goodbye}")

                tts.speak(goodbye)

                break

            # -----------------------------------------
            # 3. SEND QUESTION TO AI
            # -----------------------------------------

            print("\n🤖 Srija AI is thinking...")

            answer = ask_agent(question)

            # -----------------------------------------
            # 4. DISPLAY ANSWER
            # -----------------------------------------

            print(f"\n🧠 Srija AI: {answer}")

            # -----------------------------------------
            # 5. SPEAK ANSWER
            # -----------------------------------------

            tts.speak(answer)

            print("\n" + "-" * 60)

        except KeyboardInterrupt:

            print("\n\nSrija AI: Session ended.")
            break

        except Exception as error:

            print(f"\n❌ Error: {error}")


if __name__ == "__main__":
    main()