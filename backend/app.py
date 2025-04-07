from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    # For now, just echo the message back
    response = {'reply': f'You said: {user_message}'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
