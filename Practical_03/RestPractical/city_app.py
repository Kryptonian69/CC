from flask import Flask, jsonify, request
app = Flask(__name__)

cities = [{'id': 1, 'City_Name': 'Mumbai', 'District_Name': 'Mumbai City', 'Population': 12000000}]

@app.route('/cities', methods=['GET'])
def get_cities(): return jsonify({'cities': cities})

@app.route('/cities/<int:c_id>', methods=['GET'])
def get_city(c_id):
    city = next((c for c in cities if c['id'] == c_id), None)
    return jsonify(city) if city else (jsonify({'message': 'Not found'}), 404)

@app.route('/cities', methods=['POST'])
def add_city():
    new_city = {'id': cities[-1]['id'] + 1 if cities else 1, **request.json}
    cities.append(new_city)
    return jsonify(new_city), 201

@app.route('/cities/<int:c_id>', methods=['PUT'])
def update_city(c_id):
    city = next((c for c in cities if c['id'] == c_id), None)
    if city: city.update(request.json); return jsonify(city)
    return jsonify({'message': 'Not found'}), 404

@app.route('/cities/<int:c_id>', methods=['DELETE'])
def delete_city(c_id):
    global cities; cities = [c for c in cities if c['id'] != c_id]
    return jsonify({'message': 'Deleted'})

if __name__ == '__main__': app.run(debug=True, port=5004)
