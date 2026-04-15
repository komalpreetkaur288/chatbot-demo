# ============================================================
# College Helpdesk Chatbot - Powered by Groq AI (Llama 3)
# ============================================================
# Groq is a FREE alternative to Gemini with no billing needed.
# It uses the Llama 3 model (by Meta) via the Groq cloud API.
# Get your free API key at: https://console.groq.com
# ============================================================

import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

# ── Load environment variables from .env file ──────────────
load_dotenv()

# ── Initialize Flask app ───────────────────────────────────
app = Flask(__name__)

# ── Initialize Groq client with API key from .env ─────────
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ── College Information (System Prompt) ────────────────────
# This is sent to the AI as a "system" instruction before every chat.
# It tells the AI everything about the college and restricts it
# to only answer college-related questions.
COLLEGE_SYSTEM_PROMPT = """
You are a helpful college helpdesk assistant for "Guru Nanak Dev University College" (GNDUC).
You only answer questions strictly related to the college information provided below.
If a user asks anything NOT related to this college, reply with:
"I'm sorry, I can only answer questions related to our college. Please ask about admissions, courses, fees, facilities, or other college-related topics."

=== COLLEGE INFORMATION ===

1. COLLEGE NAME & LOCATION
   - Name: Guru Nanak Dev University College (GNDUC)
   - Address: GT Road, Punjab, India - 143001
   - Phone: +91-183-2258802
   - Email: info@gnduc.ac.in
   - Website: www.gnduc.ac.in
   - Established: 1969

2. COURSES OFFERED
   Undergraduate:
   - BCA (Bachelor of Computer Applications) — 3 years
   - BBA (Bachelor of Business Administration) — 3 years
   - B.Com (Bachelor of Commerce) — 3 years
   - B.Sc (Bachelor of Science - IT) — 3 years

   Postgraduate:
   - MCA (Master of Computer Applications) — 2 years
   - MBA (Master of Business Administration) — 2 years
   - M.Com (Master of Commerce) — 2 years

3. FEES STRUCTURE (Per Year)
   - BCA: Rs.30,000 per year
   - BBA: Rs.35,000 per year
   - B.Com: Rs.20,000 per year
   - B.Sc IT: Rs.28,000 per year
   - MCA: Rs.95,000 per year
   - MBA: Rs.50,000 per year
   - M.Com: Rs.25,000 per year

4. ADMISSION PROCESS
   - Admissions open every year in July-August.
   - Students can apply online at www.gnduc.ac.in or visit the campus.
   - Required documents: 10th & 12th marksheets, ID proof, passport photos.
   - Entrance test may be required for MCA and MBA.
   - Merit-based admission for undergraduate programs.
   - Last date for admission: typically 31st August each year.

5. COLLEGE TIMINGS
   - College Hours: 9:00 AM to 4:00 PM (Monday to Saturday)
   - Library: 8:30 AM to 5:00 PM
   - Office Hours: 10:00 AM to 3:00 PM

6. FACILITIES
   - Computer Labs with 200+ systems and high-speed internet
   - Central Library with 50,000+ books and e-journals
   - Sports complex (cricket, football, basketball, badminton)
   - Canteen with affordable food
   - Girls Hostel available (Boys hostel under construction)
   - Medical room with first-aid facility
   - Wi-Fi campus
   - Smart classrooms with projectors

7. TRANSPORT
   - College buses available from major city routes.
   - Routes cover: Amritsar, Gurdaspur, Pathankot, Batala.
   - Transport fee: Rs.5,000-Rs.8,000 per year depending on distance.

8. SCHOLARSHIPS
   - SC/ST scholarship: Fully funded by Punjab Government.
   - Merit scholarship: For students scoring above 85% in 12th.
   - Sports quota: For students with district/state level certificates.

9. IMPORTANT CONTACTS
   - Principal Office: +91-183-2258802
   - Admission Cell: +91-183-2258803
   - Exam Department: +91-183-2258804
   - Placement Cell: placement@gnduc.ac.in

10. EXAM & RESULTS
    - Exams conducted by Guru Nanak Dev University (GNDU), Amritsar.
    - End-semester exams in November and April/May.
    - Results declared on gndu.ac.in within 60 days.
    - Internal assessment: 20 marks | External exam: 80 marks

11. PLACEMENT
    - Active placement cell with tie-ups with 50+ companies.
    - Average package: Rs.3-5 LPA for IT graduates.
    - Companies: Infosys, TCS, Wipro, HCL, Cognizant, and more.

=== END OF COLLEGE INFORMATION ===

Always be polite, professional, and helpful. Keep answers concise and clear.
Only respond based on the above college information.
"""


# ── Route: Home Page ───────────────────────────────────────
@app.route("/")
def home():
    # Render the chat UI from templates/index.html
    return render_template("index.html")


# ── Route: Chat API Endpoint ───────────────────────────────
@app.route("/get", methods=["POST"])
def chatbot_response():
    # Get the user's message from the POST request
    user_message = request.json.get("message", "").strip()

    # If message is empty, return a prompt
    if not user_message:
        return jsonify({"response": "Please type a message."})

    try:
        # Send message to Groq API using Llama 3 model
        # "system" role = college instructions
        # "user" role = the student's question
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # Current free Llama 3.1 model on Groq
            messages=[
                {"role": "system", "content": COLLEGE_SYSTEM_PROMPT},
                {"role": "user",   "content": user_message}
            ],
            temperature=0.5,   # Lower = more focused and factual answers
            max_tokens=512,    # Limit response length to keep it concise
        )

        # Extract the AI's reply text from the response object
        answer = chat_completion.choices[0].message.content

    except Exception as e:
        error_message = str(e)
        # Handle rate limit error with a friendly message
        if "429" in error_message or "rate" in error_message.lower():
            answer = "⚠️ Too many requests. Please wait a few seconds and try again."
        else:
            # For any other error, show a generic message
            answer = "Sorry, something went wrong. Please try again later."

    # Return the AI response as JSON to the frontend
    return jsonify({"response": answer})


# ── Start the Flask Server ─────────────────────────────────
if __name__ == "__main__":
    # Read port and debug mode from .env
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "True").lower() == "true"

    print("🎓 College Helpdesk Chatbot is running...")
    print(f"   Visit: http://localhost:{port}")

    app.run(host="0.0.0.0", port=port, debug=debug)
