# 🎓 College Helpdesk Chatbot

An AI-powered college helpdesk chatbot built with **Flask** and **Google Gemini AI**.  
It answers questions strictly related to college information like courses, fees, admissions, facilities, and more.

---

## 📁 Project Structure

```
chatbot-demo/
│
├── main.py            # Main Flask app with Gemini AI chatbot
├── .env               # Environment variables (API key, port, etc.)
├── requirements.txt   # Python dependencies
├── templates/
│   └── index.html     # Frontend chat UI
└── README.md          # This file
```

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- Python 3.8 or above
- pip (Python package manager)

---

## 🚀 How to Run

### Step 1 — Get a Gemini API Key

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key

---

### Step 2 — Set Up the `.env` File

Open the `.env` file in the project folder and replace the placeholder with your actual API key:

```
GEMINI_API_KEY=your_actual_api_key_here
FLASK_DEBUG=True
FLASK_PORT=5000
```

---

### Step 3 — Install Dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

This will install:
- `flask` — web server
- `google-generativeai` — Gemini AI SDK
- `python-dotenv` — to load `.env` variables

---

### Step 4 — Run the Chatbot

```bash
python main.py
```

You should see:

```
🎓 College Helpdesk Chatbot is running...
   Visit: http://localhost:5000
```

---

### Step 5 — Open in Browser

Go to: [http://localhost:5000](http://localhost:5000)

Start chatting! You can ask questions like:
- *"What courses are offered?"*
- *"What is the BCA fee?"*
- *"When do admissions start?"*
- *"Is transport available?"*
- *"What are the college timings?"*

---

## 🔒 Important Notes

- The chatbot **only answers college-related questions**.
- If you ask anything outside college info, it will politely refuse.
- Never share your `.env` file or API key publicly.
- Add `.env` to `.gitignore` before pushing to GitHub.

---

## 🛑 How to Stop the Server

Press `Ctrl + C` in the terminal to stop the Flask server.
