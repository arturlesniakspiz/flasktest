from flask import Flask, jsonify
import random

app = Flask(__name__)

# Endpoint zwracający losowe dane
@app.route('/random-data', methods=['GET'])
def random_data():
    data = {
        "random_number": random.randint(1, 100),
        "random_float": round(random.uniform(1, 100), 2),
        "random_choice": random.choice(["apple", "banana", "cherry", "date"]),
        "status": "success"
    }
    return jsonify(data)

if __name__ == '__main__':
    # Nasłuchiwanie na 0.0.0.0 i porcie 5000
    app.run(host='0.0.0.0', port=5000)
