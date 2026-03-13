from flask import Flask, jsonify, request
app = Flask(__name__)

products = [{'id': 1, 'Product_Name': 'Laptop', 'Quantity': 10, 'Expiry_date': '2027-12-31'}]

@app.route('/products', methods=['GET'])
def get_products(): return jsonify({'products': products})

@app.route('/products/<int:p_id>', methods=['GET'])
def get_product(p_id):
    product = next((p for p in products if p['id'] == p_id), None)
    return jsonify(product) if product else (jsonify({'message': 'Not found'}), 404)

@app.route('/products', methods=['POST'])
def add_product():
    new_product = {'id': products[-1]['id'] + 1 if products else 1, **request.json}
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:p_id>', methods=['PUT'])
def update_product(p_id):
    product = next((p for p in products if p['id'] == p_id), None)
    if product: product.update(request.json); return jsonify(product)
    return jsonify({'message': 'Not found'}), 404

@app.route('/products/<int:p_id>', methods=['DELETE'])
def delete_product(p_id):
    global products; products = [p for p in products if p['id'] != p_id]
    return jsonify({'message': 'Deleted'})

if __name__ == '__main__': app.run(debug=True, port=5002)
