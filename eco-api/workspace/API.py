from flask import Flask, request, jsonify
from database import get_user_points, add_points_to_user, login_user, get_user_info, register_user

app = Flask(__name__)

@app.route('/add_points', methods=['POST'])
def add_points():
    url = request.json.get('url')
    email = request.json.get('email')
    points = add_points_to_user(url, email)
    return jsonify({'points': points})

@app.route('/get_points', methods=['GET'])
def get_points():
    email = request.args.get('email')
    points = get_user_points(email)
    return jsonify({'points': points})

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    success = login_user(email, password)
    return jsonify({'success': success})

@app.route('/dashboard', methods=['GET'])
def dashboard():
    email = request.args.get('email')
    user_info = get_user_info(email)
    return jsonify(user_info)

@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    success = register_user(email, password)
    return jsonify({'success': success})

if __name__ == '__main__':
    app.run()
