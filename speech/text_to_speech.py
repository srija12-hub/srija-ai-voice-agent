import pyttsx3


class TextToSpeech:

    def __init__(self):
        # No persistent engine.
        # We create a fresh engine for every response.
        pass

    def speak(self, text):

        print("🔊 Srija AI is speaking...")

        try:

            engine = pyttsx3.init()

            # Speaking speed
            engine.setProperty("rate", 165)

            # Volume
            engine.setProperty("volume", 1.0)

            # Speak
            engine.say(text)

            # Wait until speech finishes
            engine.runAndWait()

            # Completely stop this engine
            engine.stop()

            del engine

        except Exception as error:

            print(f"❌ Text-to-speech error: {error}")


# -----------------------------------------
# TEST
# -----------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("SRIJA AI - TEXT TO SPEECH TEST")
    print("=" * 50)

    tts = TextToSpeech()

    tts.speak(
        "Hello, I'm Srija AI. "
        "I am a voice agent representing Srija."
    )

    print("\n✅ Text-to-speech test completed.")