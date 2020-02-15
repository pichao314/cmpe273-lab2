from flask import Flask, escape, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

student = [
    {
        'id': 0,
        'name': "Chao Pi",
    }
]

@app.route('/students')
def sums():
    p = "" if len(student) <= 1 else "s"
    return "Totally %d student" % len(student) + p,200

@app.route('/students/<int:id>')
def get(id):
    return jsonify(student[id]),200