import speech_recognition as sr


class SpeechToText:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        # Settings for better microphone recognition
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.5


    def listen(self):

        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            try:

                # Adjust microphone to surrounding noise
                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=15
                )

            except sr.WaitTimeoutError:

                print("⏱️ No speech detected.")

                return None


        print("🔄 Converting speech to text...")


        try:

            text = self.recognizer.recognize_google(
                audio
            )

            print(f"📝 You said: {text}")

            return text


        except sr.UnknownValueError:

            print("❌ I couldn't understand the speech.")

            return None


        except sr.RequestError as error:

            print(
                f"❌ Speech recognition service error: {error}"
            )

            return None


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":

    stt = SpeechToText()

    print("=" * 50)
    print("SRIJA AI - SPEECH TO TEXT TEST")
    print("=" * 50)

    print("\nSpeak a question after the microphone starts.")

    text = stt.listen()

    if text:

        print("\nFinal transcription:")
        print(text)

    else:

        print("\nNo transcription received.")