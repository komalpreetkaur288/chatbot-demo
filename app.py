from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def get_bot_response(message):
    message = message.lower()

    if "hi" in message:
        return "Hello,How can I help you?"
    if "hello" in message:
        return "Hello,How can I help you?"
    elif "course" in message:
        return "We offer BCA, BBA, MCA , MBA."
    elif "bca" in message:
        return "BCA fee is ₹30,000 per year."
    elif "mca" in message:
        return "MCA fee is ₹95,000 per year."
    elif "bba" in message:
        return "BBA fee is ₹35,000 per year."
    elif "mba" in message:
        return "MBA fee is ₹50,000 per year."
    elif "admission" in message:
        return "Admissions start in July,You can apply online through the college website or You can visit College Campus.."
    elif "transport" in message:
        return "Yes, transport services are available ."
    elif "timing" in message:
        return "College timing is from 9 AM to 4 PM.."
    elif "thanks" in message:
        return "You're welcome!."
    elif "bye" in message:
        return "Good Bye, Have A Nice Day!."
    else:
        return "Sorry, I didn't understand. Ask another question"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.json.get("message")
    response = get_bot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)