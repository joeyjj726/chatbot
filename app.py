
import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"


# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Call OpenAI GPT API with the updated syntax
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model you want to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for favicon.ico to suppress 404 warnings
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content

if __name__ == "__main__":
    app.run(debug=True)
