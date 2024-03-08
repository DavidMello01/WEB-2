from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return """
    <h1>Todo List</h1>
    <ul>
        {% for task in tasks %}
        <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <form action="/add" method="post">
        <input type="text" name="task" placeholder="Add a new task">
        <button type="submit">Add</button>
    </form>
    """

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
