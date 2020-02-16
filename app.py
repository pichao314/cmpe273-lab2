from flask import Flask, escape, request, jsonify

app = Flask(__name__)

# the default path would return hello msg
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!', 200


students = [{
    'id': 0,
    'name': "Chao Pi",
}]


@app.route('/students')
def sums():
    p = "" if len(students) <= 1 else "s"
    return "Totally %d student" % len(students) + p, 200


@app.route('/students/<int:id>')
def get(id):
    for student in students:
        if student['id'] == id:
            return jsonify(student), 200
    return "Not Found!", 204


@app.route('/students', methods=['POST'])
def post():
    if not request.json:
        return "Wrong Value"
    info = request.json
    for student in students:
        if info['id'] == student['id']:
            return "ID existed!", 204
    students.append({'id': info['id'], 'name': info['name']})
    return "Added!", 201


classes = [{
    "id": 273,
    "name": "CMPE-273",
    "students": [],
}]


@app.route('/classes')
def sumc():
    p = "" if len(classes) <= 1 else "s"
    return "Totally %d classes" % len(classes) + p, 200


@app.route('/classes/<int:id>')
def getc(id):
    for cl in classes:
        if cl['id'] == id:
            return jsonify(cl), 200
    return "Not Found!", 204


@app.route('/classes', methods=['POST'])
def postc():
    if not request.json:
        return "Wrong Value"
    info = request.json
    for cl in classes:
        if info['id'] == cl['id']:
            return "ID existed!", 204
    classes.append({'id': info['id'], 'name': info['name'], 'students': []})
    return "Added!", 201


@app.route('/classes/<int:id>', methods=['PATCH'])
def patc(id):
    if not request.json:
        return "Wrong Value"
    info = request.json
    for cl in classes:
        if id == cl['id']:
            for cs in cl['students']:
                if cs['id'] == info['id']:
                    return "Student already in class!", 204
            for st in students:
                if info['id'] == st['id']:
                    cl['students'].append(st)
                    return jsonify(cl), 201
            return "Student ID Not Found!", 204
    return "Class ID not found!", 204


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
