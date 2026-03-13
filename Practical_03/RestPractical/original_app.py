from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
students = [
    {
        'id': 1,
        'Student_Name': 'John Doe',
        'age': 20,
        'Phone_no': '9876543210',
        'Subject': 'Computer Science'
    }
]

# 1. READ (GET all)
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({'students': students})

# 2. READ (GET by ID)
@app.route('/students/<int:s_id>', methods=['GET'])
def get_student(s_id):
    student = next((s for s in students if s['id'] == s_id), None)
    if student:
        return jsonify(student)
    return jsonify({'message': 'Student not found'}), 404

# 3. CREATE (POST)
@app.route('/students', methods=['POST'])
def add_student():
    if not request.json or 'Student_Name' not in request.json:
        return jsonify({'error': 'Missing required fields'}), 400
    new_student = {
        'id': students[-1]['id'] + 1 if students else 1,
        'Student_Name': request.json['Student_Name'],
        'age': request.json['age'],
        'Phone_no': request.json['Phone_no'],
        'Subject': request.json['Subject']
    }
    students.append(new_student)
    return jsonify({'message': 'Student added', 'student': new_student}), 201

# 4. UPDATE (PUT)
@app.route('/students/<int:s_id>', methods=['PUT'])
def update_student(s_id):
    student = next((s for s in students if s['id'] == s_id), None)
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    
    student['Student_Name'] = request.json.get('Student_Name', student['Student_Name'])
    student['age'] = request.json.get('age', student['age'])
    student['Phone_no'] = request.json.get('Phone_no', student['Phone_no'])
    student['Subject'] = request.json.get('Subject', student['Subject'])
    
    return jsonify({'message': 'Student updated', 'student': student})

# 5. DELETE
@app.route('/students/<int:s_id>', methods=['DELETE'])
def delete_student(s_id):
    global students
    students = [s for s in students if s['id'] != s_id]
    return jsonify({'message': 'Student deleted'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
