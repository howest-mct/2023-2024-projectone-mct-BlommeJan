import threading
import time
from repositories.DataRepository import DataRepository
from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from helpers.onewire import OneWire

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DionyShakeItBaby!'

# ping interval forces rapid B2F communication
socketio = SocketIO(app, cors_allowed_origins="*",
                    async_mode='gevent', ping_interval=0.5)
CORS(app)

def read_temperature():
    w1 = OneWire("28-8590fd1d64ff")
    
    while True:
        # Reading temperature
        result = w1.read_temperature()

        # Sending temperature to frontend
        socketio.emit("BTF_temp", { "temp": result })

        # Inserting temperature in database
        DataRepository.insert_temperature(result)

        # Delay between reads
        time.sleep(1)


def start_thread():
    threading.Thread(target=read_temperature, daemon=True).start()
    print("thread started")


# API ENDPOINTS
@app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."


# SOCKET IO
@socketio.on('connect')
def initial_connection():
    print('A new client connect')


@socketio.on('F2B_switch_light')
def switch_light(data):
    print('licht gaat aan/uit', data)
    lamp_id = data['lamp_id']
    new_status = data['new_status']
    # spreek de hardware aan
    # stel de status in op de DB
    res = DataRepository.update_status_lamp(lamp_id, new_status)
    print(res)
    # vraag de (nieuwe) status op van de lamp
    data = DataRepository.read_status_lamp_by_id(lamp_id)
    socketio.emit('B2F_verandering_lamp',  {'lamp': data})
    # Indien het om de lamp van de TV kamer gaat, dan moeten we ook de hardware aansturen.
    if lamp_id == '3':
        print(f"TV kamer moet switchen naar {new_status} !")
        # Do something


if __name__ == '__main__':
    try:
        start_thread()
        print("**** Starting APP ****")
        socketio.run(app, debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        print('KeyboardInterrupt exception is caught')
    finally:
        print("finished")
