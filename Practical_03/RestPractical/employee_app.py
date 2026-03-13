from flask import Flask, jsonify, request
app = Flask(__name__)

employees = [{'id': 1, 'Employee_Name': 'Alice Smith', 'age': 30, 'Phone_no': '9123456780', 'Department': 'HR'}]

@app.route('/employees', methods=['GET'])
def get_employees(): return jsonify({'employees': employees})

@app.route('/employees/<int:e_id>', methods=['GET'])
def get_employee(e_id):
    employee = next((e for e in employees if e['id'] == e_id), None)
    return jsonify(employee) if employee else (jsonify({'message': 'Not found'}), 404)

@app.route('/employees', methods=['POST'])
def add_employee():
    new_employee = {'id': employees[-1]['id'] + 1 if employees else 1, **request.json}
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/employees/<int:e_id>', methods=['PUT'])
def update_employee(e_id):
    employee = next((e for e in employees if e['id'] == e_id), None)
    if employee: employee.update(request.json); return jsonify(employee)
    return jsonify({'message': 'Not found'}), 404

@app.route('/employees/<int:e_id>', methods=['DELETE'])
def delete_employee(e_id):
    global employees; employees = [e for e in employees if e['id'] != e_id]
    return jsonify({'message': 'Deleted'})

if __name__ == '__main__': app.run(debug=True, port=5001)
