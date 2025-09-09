from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask backend!"})

# Add /api/data POST endpoint
@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.get_json()
    return jsonify({"received": data}), 200

if __name__ == '__main__':
    app.run(debug=True)