from flask import Flask, jsonify, request
app = Flask(__name__)

players = [{'id': 1, 'Player_Name': 'Virat Kohli', 'age': 35, 'Country': 'India', 'Runs': 13000}]

@app.route('/players', methods=['GET'])
def get_players(): return jsonify({'players': players})

@app.route('/players/<int:p_id>', methods=['GET'])
def get_player(p_id):
    player = next((p for p in players if p['id'] == p_id), None)
    return jsonify(player) if player else (jsonify({'message': 'Not found'}), 404)

@app.route('/players', methods=['POST'])
def add_player():
    new_player = {'id': players[-1]['id'] + 1 if players else 1, **request.json}
    players.append(new_player)
    return jsonify(new_player), 201

@app.route('/players/<int:p_id>', methods=['PUT'])
def update_player(p_id):
    player = next((p for p in players if p['id'] == p_id), None)
    if player: player.update(request.json); return jsonify(player)
    return jsonify({'message': 'Not found'}), 404

@app.route('/players/<int:p_id>', methods=['DELETE'])
def delete_player(p_id):
    global players; players = [p for p in players if p['id'] != p_id]
    return jsonify({'message': 'Deleted'})

if __name__ == '__main__': app.run(debug=True, port=5003)
