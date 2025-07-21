# 🌿 EcoSync Chatbot

EcoSync is a smart and friendly sustainability chatbot built with **Flask** and powered by **Google Gemini 1.5 Flash** via the `google-generativeai` API.

It helps users with:
- 🌱 Eco-friendly product suggestions  
- 🔄 Recycling and upcycling tips  
- 🗑️ Waste reduction techniques  
- 🏡 Sustainable living advice  

---

## ⚙️ Features

- 🧠 AI-powered answers via Gemini API  
- 🎙️ Voice input + Speak response  
- 📜 Chat history saved in session  
- 💬 WhatsApp-like conversation layout  
- 👍👎 Like/dislike emoji feedback  
- 🔁 Manual clear/reset chat  
- 🎯 Auto-scroll and responsive design  
- 📁 Sidebar with history, new chat, and toggle  

---

## 📁 Project Structure

ecosync-chatbot/
├── app.py
├── .env
├── requirements.txt
├── static/
│ └── (CSS, JS, icons if any)
├── templates/
│ └── index.html
└── README.md

yaml
Copy
Edit

---

## 🔐 .env Setup

Create a `.env` file in your root directory:

GEMINI_API_KEY=your_google_generativeai_key
FLASK_SECRET_KEY=your_random_flask_secret_key

css
Copy
Edit

You can generate a secure secret key using:

```python
import secrets
print(secrets.token_hex(32))
🚀 Setup Instructions
1. Clone this Repo
git clone https://github.com/YOUR_USERNAME/ecosync-chatbot.git
cd ecosync-chatbot

2. Create Virtual Environment
python -m venv ecoenv
source ecoenv/bin/activate  # On Windows: ecoenv\Scripts\activate

3. Install Requirements
pip install -r requirements.txt
Flask
python-dotenv
google-generativeai

4. Run the App
python app.py
Open browser: http://127.0.0.1:5000

🧪 Technologies Used
Python 3.11+

Flask

Google Generative AI (google-generativeai)

HTML/CSS/JS (Vanilla)

Web Speech API (for voice input/output)

🧠 Example Questions
"Suggest eco-friendly alternatives to plastic."

"How to recycle old clothes?"

"Tips for reducing kitchen waste?"

"Point-by-point advice on sustainable travel."

⚠️ Browser Support
Voice input uses webkitSpeechRecognition — best supported on Chrome and some Android browsers.
