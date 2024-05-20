from flask import Flask, jsonify, request

app = Flask(__name__)

# サンプルデータ
users = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35}
]

# 全てのユーザーを取得するエンドポイント
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# 特定のユーザーをIDで取得するエンドポイント
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# 新しいユーザーを追加するエンドポイント
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

# アプリケーションを実行する
if __name__ == '__main__':
    app.run(debug=True)
