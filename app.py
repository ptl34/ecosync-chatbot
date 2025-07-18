from flask import Flask, render_template, request, session, redirect, url_for
import google.generativeai as genai
import os
from dotenv import load_dotenv
from datetime import datetime
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Gemini configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# File to store persistent history
HISTORY_FILE = "chat_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file)

def eco_chatbot(prompt_text):
    prompt = (
        "You are EcoSync, a smart and friendly sustainability chatbot.\n"
        "Reply concisely (3-5 sentences) unless the question clearly asks for detail.\n"
        f"User: {prompt_text}"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

@app.route("/", methods=["GET", "POST"])
def home():
    if "history" not in session:
        session["history"] = load_history()
    if "sessions" not in session:
        session["sessions"] = []

    if request.method == "POST":
        if "clear_chat" in request.form:
            session["history"] = []
            session["sessions"] = []
            save_history([])
        elif "new_chat" in request.form:
            session["history"] = []
            timestamp = datetime.now().strftime("%I:%M %p")
            session["sessions"].append(f"Chat - {timestamp}")
            save_history([])
        else:
            user_input = request.form.get("question", "").strip()
            if user_input:
                timestamp = datetime.now().strftime("%I:%M %p")
                bot_response = eco_chatbot(user_input)
                session["history"].append({
                    "question": user_input,
                    "answer": bot_response,
                    "time": timestamp
                })
                session.modified = True
                if len(session["sessions"]) == 0:
                    session["sessions"].append(f"Chat - {timestamp}")
                save_history(session["history"])

    return render_template("index.html", history=session.get("history", []), chat_sessions=session.get("sessions", []))

if __name__ == "__main__":
    app.run(debug=True)
