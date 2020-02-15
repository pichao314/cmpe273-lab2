from flask import Flask, escape, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


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
        if student['id']==id:
            return jsonify(student), 200
    return "Not Found!",202


@app.route('/students', methods=['POST'])
def post():
    if not request.json:
        return "Wrong Value"
    info = request.json
    for student in students:
        if info['id']==student['id']:
            return "ID existed!", 202
    students.append({'id': info['id'], 'name': info['name']})
    return "Added!", 201

classes = [
    {
        "id":273,
        "name":"CMPE-273",
        "students":[]
    }
]



