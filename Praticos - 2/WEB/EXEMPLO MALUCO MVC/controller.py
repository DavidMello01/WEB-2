from flask import Flask, render_template, request, redirect, url_for
from model import TodoModel

app = Flask(__name__)
model = TodoModel()

@app.route('/')
def index():
    tasks = model.get_tasks()
    return render_template('view.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:
        model.add_task(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
