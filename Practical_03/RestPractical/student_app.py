from flask import Flask, jsonify, request
app = Flask(__name__)

students = [{'id': 1, 'Student_Name': 'John Doe', 'age': 20, 'Phone_no': '9876543210', 'Subject': 'Computer Science'}]

@app.route('/students', methods=['GET'])
def get_students(): return jsonify({'students': students})

@app.route('/students/<int:s_id>', methods=['GET'])
def get_student(s_id):
    student = next((s for s in students if s['id'] == s_id), None)
    return jsonify(student) if student else (jsonify({'message': 'Not found'}), 404)

@app.route('/students', methods=['POST'])
def add_student():
    new_student = {'id': students[-1]['id'] + 1 if students else 1, **request.json}
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/students/<int:s_id>', methods=['PUT'])
def update_student(s_id):
    student = next((s for s in students if s['id'] == s_id), None)
    if student: student.update(request.json); return jsonify(student)
    return jsonify({'message': 'Not found'}), 404

@app.route('/students/<int:s_id>', methods=['DELETE'])
def delete_student(s_id):
    global students; students = [s for s in students if s['id'] != s_id]
    return jsonify({'message': 'Deleted'})

if __name__ == '__main__': app.run(debug=True, port=5000)
