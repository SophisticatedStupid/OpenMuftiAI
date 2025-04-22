from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("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
")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an Islamic Mufti AI. Provide authentic guidance from Quran, Hadith, and scholarly consensus."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
