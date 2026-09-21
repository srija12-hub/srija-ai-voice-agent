import { useState, useRef } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [listening, setListening] = useState(false);
  const [speaking, setSpeaking] = useState(false);

  const recognitionRef = useRef(null);

  // =========================
  // BROWSER TEXT TO SPEECH
  // =========================

  const speakAnswer = (text) => {
    if (!text || !text.trim()) {
      setSpeaking(false);
      return;
    }

    if (!("speechSynthesis" in window)) {
      console.log("Speech synthesis is not supported.");
      setSpeaking(false);
      return;
    }

    window.speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(text);

    speech.lang = "en-IN";
    speech.rate = 0.95;
    speech.pitch = 1;
    speech.volume = 1;

    speech.onstart = () => {
      setSpeaking(true);
    };

    speech.onend = () => {
      setSpeaking(false);
    };

    speech.onerror = () => {
      setSpeaking(false);
    };

    window.speechSynthesis.speak(speech);
  };


  // =========================
  // ASK AI
  // =========================

  const askAI = async (text = question) => {
    if (!text.trim() || loading) {
      return;
    }

    setLoading(true);
    setAnswer("");

    try {
      const response = await fetch(
        "/ask",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question: text,
          }),
        }
      );

      const data = await response.json();

      if (data.success) {
        setAnswer(data.answer);
        speakAnswer(data.answer);
      } else {
        const errorAnswer =
          data.answer ||
          "Sorry, I couldn't process that question.";

        setAnswer(errorAnswer);
        speakAnswer(errorAnswer);
      }

    } catch (error) {

      console.error("AI connection error:", error);

      const errorAnswer =
        "I couldn't connect to the Srija AI backend. Please make sure the backend is running.";

      setAnswer(errorAnswer);
    }

    setLoading(false);
  };


  // =========================
  // MICROPHONE
  // =========================

  const startListening = () => {

    const SpeechRecognition =
      window.SpeechRecognition ||
      window.webkitSpeechRecognition;

    if (!SpeechRecognition) {

      alert(
        "Speech recognition is not supported in this browser. Please use Google Chrome."
      );

      return;
    }

    if (speaking) {

      window.speechSynthesis.cancel();

      setSpeaking(false);
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-IN";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = () => {

      setListening(true);
      setAnswer("");
    };

    recognition.onresult = (event) => {

      const transcript =
        event.results[0][0].transcript;

      console.log(
        "Interviewer:",
        transcript
      );

      setQuestion(transcript);

      askAI(transcript);
    };

    recognition.onerror = (event) => {

      console.error(
        "Speech recognition error:",
        event.error
      );

      setListening(false);

      if (event.error === "not-allowed") {

        alert(
          "Microphone permission was denied. Please allow microphone access in Chrome."
        );
      }
    };

    recognition.onend = () => {

      setListening(false);
    };

    recognitionRef.current = recognition;

    recognition.start();
  };


  // =========================
  // STOP LISTENING
  // =========================

  const stopListening = () => {

    if (recognitionRef.current) {

      recognitionRef.current.stop();

      setListening(false);
    }
  };


  // =========================
  // STOP SPEAKING
  // =========================

  const stopSpeaking = () => {

    if ("speechSynthesis" in window) {

      window.speechSynthesis.cancel();
    }

    setSpeaking(false);
  };


  // =========================
  // KEYBOARD
  // =========================

  const handleKeyDown = (event) => {

    if (event.key === "Enter") {

      askAI();
    }
  };


  // =========================
  // QUICK QUESTIONS
  // =========================

  const selectQuestion = (text) => {

    setQuestion(text);

    askAI(text);
  };


  // =========================
  // RENDER
  // =========================

  return (

    <div className="app">

      {/* =========================
          TOP BAR
      ========================= */}

      <header className="topbar">

        <div className="brand">

          <div className="brand-logo">
            S
          </div>

          <div>

            <h1>Srija AI</h1>

            <p>
              Developer Voice Agent
            </p>

          </div>

        </div>


        <div className="online-status">

          <span className="online-dot"></span>

          AI ONLINE

        </div>

      </header>


      {/* =========================
          DASHBOARD
      ========================= */}

      <main className="dashboard">


        {/* =========================
            HERO
        ========================= */}

        <section className="hero-section">

          <div className="hero-badge">

            <span>✦</span>

            AI-POWERED DEVELOPER ASSISTANT

          </div>


          <h2>

            Meet

            <span>
              Srija AI
            </span>

          </h2>


          <p>

            Ask questions about Srija's education,
            technical skills, internships, projects,
            experience, and career interests.

          </p>

        </section>


        {/* =========================
            AI PANEL
        ========================= */}

        <section className="ai-panel">


          {/* PANEL HEADER */}

          <div className="ai-panel-top">

            <div className="panel-label">

              <span className="green-dot"></span>

              VOICE INTERVIEW SESSION

            </div>


            <div className="session-status">

              {listening
                ? "LISTENING"
                : loading
                ? "THINKING"
                : speaking
                ? "SPEAKING"
                : "READY"}

            </div>

          </div>


          {/* =========================
              ORB
          ========================= */}

          <div className="orb-area">

            <div
              className={`orb-wrapper ${
                listening
                  ? "orb-listening"
                  : loading
                  ? "orb-thinking"
                  : speaking
                  ? "orb-speaking"
                  : ""
              }`}
            >

              <div className="orb-ring ring-one"></div>

              <div className="orb-ring ring-two"></div>


              <div className="ai-orb">

                <span className="orb-letter">
                  S
                </span>

                <div className="orb-wave wave-one"></div>

                <div className="orb-wave wave-two"></div>

                <div className="orb-wave wave-three"></div>

              </div>

            </div>


            <h3>

              {listening
                ? "Listening..."
                : loading
                ? "Thinking..."
                : speaking
                ? "Speaking..."
                : "Ask Srija AI"}

            </h3>


            <p>

              {listening
                ? "Speak your interview question"
                : loading
                ? "Finding the answer..."
                : speaking
                ? "Srija AI is answering"
                : "Your AI-powered interview assistant"}

            </p>

          </div>


          {/* =========================
              MICROPHONE
          ========================= */}

          <button
            className={`main-mic ${
              listening ? "mic-active" : ""
            }`}
            onClick={
              listening
                ? stopListening
                : startListening
            }
            disabled={loading}
          >

            {listening
              ? "⏹"
              : "🎙️"}

          </button>


          <div className="mic-caption">

            {listening
              ? "Click to stop listening"
              : "Click the microphone to speak"}

          </div>


          {/* =========================
              STOP SPEAKING
          ========================= */}

          {speaking && (

            <div
              style={{
                textAlign: "center",
                marginBottom: "18px"
              }}
            >

              <button
                onClick={stopSpeaking}
                style={{
                  border: "1px solid rgba(255,255,255,0.1)",
                  background: "rgba(255,255,255,0.04)",
                  color: "#aab2c3",
                  padding: "8px 14px",
                  borderRadius: "9px",
                  fontSize: "11px",
                  cursor: "pointer"
                }}
              >

                🔇 Stop speaking

              </button>

            </div>

          )}


          {/* =========================
              TEXT INPUT
          ========================= */}

          <div className="question-input">

            <div className="input-icon">
              💬
            </div>


            <input
              type="text"
              placeholder="Or type your interview question..."
              value={question}
              onChange={(event) =>
                setQuestion(event.target.value)
              }
              onKeyDown={handleKeyDown}
              disabled={loading}
            />


            <button
              className="send-button"
              onClick={() => askAI()}
              disabled={
                loading ||
                !question.trim()
              }
            >

              {loading
                ? "Thinking..."
                : "Ask AI"}

              <span>→</span>

            </button>

          </div>


          {/* =========================
              QUICK QUESTIONS
          ========================= */}

          <div className="quick-area">

            <div className="quick-title">

              QUICK INTERVIEW QUESTIONS

            </div>


            <div className="quick-buttons">


              <button
                onClick={() =>
                  selectQuestion(
                    "Tell me about yourself"
                  )
                }
              >

                👤

                Tell me about yourself

              </button>


              <button
                onClick={() =>
                  selectQuestion(
                    "What are your technical skills?"
                  )
                }
              >

                💻

                Technical skills

              </button>


              <button
                onClick={() =>
                  selectQuestion(
                    "Tell me about your AI internship"
                  )
                }
              >

                🤖

                AI internship

              </button>


              <button
                onClick={() =>
                  selectQuestion(
                    "Tell me about your projects"
                  )
                }
              >

                🚀

                Projects

              </button>


            </div>

          </div>


          {/* =========================
              INTERVIEWER MESSAGE
          ========================= */}

          {question && (

            <div className="message-card interviewer-card">

              <div className="message-header">

                <div className="message-avatar interviewer-avatar">
                  🎤
                </div>


                <div>

                  <strong>
                    INTERVIEWER
                  </strong>

                  <span>
                    Your question
                  </span>

                </div>

              </div>


              <p>
                {question}
              </p>

            </div>

          )}


          {/* =========================
              AI ANSWER
          ========================= */}

          {(answer || loading) && (

            <div className="message-card answer-card">

              <div className="message-header">

                <div className="message-avatar ai-avatar">
                  S
                </div>


                <div>

                  <strong>
                    SRIJA AI
                  </strong>

                  <span>
                    {loading
                      ? "Preparing answer"
                      : speaking
                      ? "Speaking response"
                      : "AI Assistant"}
                  </span>

                </div>


                {!loading && (

                  <div className="answer-state">

                    ● READY

                  </div>

                )}

              </div>


              {loading ? (

                <div className="thinking-box">

                  <span></span>
                  <span></span>
                  <span></span>

                  <p>
                    Srija AI is preparing your answer...
                  </p>

                </div>

              ) : (

                <div className="answer-content">

                  <p>
                    {answer}
                  </p>


                  {speaking && (

                    <div className="voice-indicator">

                      <div className="sound-bars">

                        <i></i>
                        <i></i>
                        <i></i>
                        <i></i>
                        <i></i>

                      </div>

                      <span>
                        🔊 Speaking response
                      </span>

                    </div>

                  )}

                </div>

              )}

            </div>

          )}

        </section>


        {/* =========================
            PROFILE INFORMATION
        ========================= */}

        <section className="profile-grid">


          <div className="profile-card">

            <div className="profile-icon">
              🎓
            </div>

            <div>

              <span>
                EDUCATION
              </span>

              <h4>
                Computer Science & Engineering
              </h4>

              <p>
                AI & ML Specialization
              </p>

            </div>

          </div>


          <div className="profile-card">

            <div className="profile-icon">
              💻
            </div>

            <div>

              <span>
                TECHNICAL FOCUS
              </span>

              <h4>
                AI • ML • Software
              </h4>

              <p>
                Python • Java • SQL
              </p>

            </div>

          </div>


          <div className="profile-card">

            <div className="profile-icon">
              🤖
            </div>

            <div>

              <span>
                AI INTERESTS
              </span>

              <h4>
                Generative AI & NLP
              </h4>

              <p>
                AI Engineering • Machine Learning
              </p>

            </div>

          </div>


        </section>

      </main>


      {/* =========================
          FOOTER
      ========================= */}

      <footer className="footer">

        <div>

          <strong>
            Srija AI
          </strong>

          <span>
            Developer Voice Agent
          </span>

        </div>


        <p>
          Built with React • FastAPI • AI
        </p>

      </footer>

    </div>
  );
}

export default App;