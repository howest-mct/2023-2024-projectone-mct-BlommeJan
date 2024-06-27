import threading
import time
from repositories.DataRepository import DataRepository
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from helpers.main import Main

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DionyShakeItBaby!'

# custom endpoint
endpoint = '/api/v1'

# ping interval forces rapid B2F communication
socketio = SocketIO(app, cors_allowed_origins="*",
                    async_mode='gevent', ping_interval=0.5)
CORS(app)

m = Main()

def read_temperature():
    count = 0

    while True:
        # Reading temperature
        result = m.get_temp()

        # Sending temperature to frontend
        socketio.emit("BTF_temp", { "temp": result })

        count =+ 1

        # Inserting temperature in database
        if count == 6:
            DataRepository.create_temp_log(result)
            count = 0

        # Delay between reads
        time.sleep(5)


def start_thread():
    threading.Thread(target=read_temperature, daemon=True).start()
    print("thread started")


# API ENDPOINTS
@app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."

@app.route('/get_temp_history/', methods=['GET'])
def get_temp_history():
    data = DataRepository.read_temp_history()
    return jsonify(data)
0
@app.route(endpoint + '/history/', methods=['GET'])
def get_history():
    data = DataRepository.read_history()
    return jsonify(data)

@app.route(endpoint + '/cocktails/', methods=['GET'])
def get_cocktails():
    data = DataRepository.read_all_cocktails()
    return jsonify(data)

@app.route(endpoint + '/cocktail/<cocktail_id>', methods=['GET'])
def get_cocktail_by_id(cocktail_id):
    data = DataRepository.read_cocktail_by_id(cocktail_id)
    return jsonify(data)

@app.route(endpoint + '/cocktail/<cocktail_id>/make', methods=['POST'])
def make_cocktail(cocktail_id):
    cocktail_id
    m.make_cocktail()
    # Start the process of making a cocktail
    return jsonify({ "success": True })

@app.route(endpoint + '/update-ingredients', methods=['POST'])
def update_ingredients():
    body = DataRepository.json_or_formdata(request)
    print(body["ingredient1"])
    print(body["ingredient2"])
    print(body["ingredient3"])
    print(body["ingredient4"])

    # Start the process of making a cocktail
    return jsonify({ "success": True })

# SOCKET IO
@socketio.on('connect')
def initial_connection():
    print('A new client connect')


# @socketio.on('F2B_switch_light')
# def switch_light(data):
#     print('licht gaat aan/uit', data)
#     lamp_id = data['lamp_id']
#     new_status = data['new_status']
#     # spreek de hardware aan
#     # stel de status in op de DB
#     res = DataRepository.update_status_lamp(lamp_id, new_status)
#     print(res)
#     # vraag de (nieuwe) status op van de lamp
#     data = DataRepository.read_status_lamp_by_id(lamp_id)
#     socketio.emit('B2F_verandering_lamp',  {'lamp': data})
#     # Indien het om de lamp van de TV kamer gaat, dan moeten we ook de hardware aansturen.
#     if lamp_id == '3':
#         print(f"TV kamer moet switchen naar {new_status} !")
#         # Do something


if __name__ == '__main__':
    try:
        start_thread()
        print("**** Starting APP ****")
        socketio.run(app, debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        print('KeyboardInterrupt exception is caught')
    finally:
        print("finished")
