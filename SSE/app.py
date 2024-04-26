from flask import Flask, render_template, request, jsonify, Response
import threading

app = Flask(__name__)

# Lista para armazenar as mensagens do chat
chat_messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    if message:
        # Adiciona a mensagem à lista de mensagens
        chat_messages.append(message)
    return '', 204

@app.route('/stream')
def stream():
    def event_stream():
        # Transmite as mensagens do chat para o cliente em tempo real
        last_index = len(chat_messages)
        while True:
            if len(chat_messages) > last_index:
                for message in chat_messages[last_index:]:
                    yield f"data: {message}\n\n"
                last_index = len(chat_messages)
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True)
