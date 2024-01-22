from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

def generate_random_numbers():
    while True:
        number = random.randint(1, 100)
        socketio.emit('random_number', {'number': number}, namespace='/test')
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    # Start the thread for generating random numbers
    number_thread = Thread(target=generate_random_numbers)
    number_thread.daemon = True
    number_thread.start()

    # Start the Flask application with SocketIO support
    socketio.run(app, debug=True)
