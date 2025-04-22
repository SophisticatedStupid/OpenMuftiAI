from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def home():
    return "Islamic Mufti AI is up."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're an Islamic scholar AI helping users learn Islam through authentic sources."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

