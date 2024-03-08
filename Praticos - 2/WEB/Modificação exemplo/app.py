from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id_counter = 1

@app.route('/')
def add_task():
    global task_id_counter
    description = request.form['task']
    task = 