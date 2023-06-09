from flask import Flask, render_template, request

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)