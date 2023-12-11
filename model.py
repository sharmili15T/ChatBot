from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    # Add your chatbot logic here (e.g., using a chatbot library or API)
    bot_response = "I'm a simple bot. I don't understand complex queries!"
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
