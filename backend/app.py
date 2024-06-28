import threading
import time
from repositories.DataRepository import DataRepository
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
# from helpers.main import Main

available_ingredients = [99, 83, 7, 236]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'DionyShakeItBaby!'

# custom endpoint
endpoint = '/api/v1'

CORS(app)

# ping interval forces rapid B2F communication
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent', ping_interval=0.5)

# m = Main()

# def read_temperature():
#     count = 0

#     while True:
#         # Reading temperature
#         result = m.get_temp()
#         # Sending temperature to frontend
#         socketio.emit("BTF_temp", { "temp": result })
#         count =+ 1
#         # Inserting temperature in database
#         if count == 6:
#             DataRepository.create_temp_log(result)
#             count = 0
#         # Delay between reads
#         time.sleep(5)


# def start_thread():
#     threading.Thread(target=read_temperature, daemon=True).start()
#     print("thread started")


# API ENDPOINTS
@app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."

@app.route('/get_temp_history/', methods=['GET'])
def get_temp_history():
    data = DataRepository.read_temp_history()
    return jsonify(data)

@app.route(endpoint + '/history/', methods=['GET'])
def get_history():
    data = DataRepository.read_history()
    return jsonify(data)

@app.route(endpoint + '/cocktails/available/', methods=['GET'])
def get_available_cocktails():
    global available_ingredients
    categories = []
    for i in available_ingredients:
        categories.append(DataRepository.get_category_by_ingredient_id(i))
    data = DataRepository.read_possible_cocktails(categories[0]["category_id"], categories[1]["category_id"], categories[2]["category_id"], categories[3]["category_id"])
    return jsonify(data)

@app.route(endpoint + '/cocktails/', methods=['GET'])
def get_cocktails():
    data = DataRepository.read_all_cocktails()
    return jsonify(data)

@app.route(endpoint + '/ingredients/current/', methods=['GET'])
def get_current_ingredients():
    global available_ingredients
    data = []
    for i in available_ingredients:
        data.append(DataRepository.read_ingredient_by_id(i))
    return jsonify(data)

@app.route(endpoint + '/ingredients/', methods=['GET'])
def get_ingredients():
    data = DataRepository.read_ingredients()
    return jsonify(data)

@app.route(endpoint + '/cocktail/<cocktail_id>/', methods=['GET'])
def get_cocktail_by_id(cocktail_id):
    data = DataRepository.read_cocktail_by_id(cocktail_id)
    return jsonify(data)

# @app.route(endpoint + '/cocktail/<cocktail_id>/make/', methods=['GET'])
# def make_cocktail(cocktail_id):
#     cocktail_id
#     # m.make_cocktail()
#     # Start the process of making a cocktail
#     return jsonify({ "success": True })

# @app.route(endpoint + '/update-ingredients/', methods=['POST'])
# def update_ingredients():
#     global available_ingredients
#     body = DataRepository.json_or_formdata(request)
#     available_ingredients = [body["ingredient1"], body["ingredient2"], body["ingredient3"], body["ingredient4"]]
#     print(body["ingredient1"])
#     print(body["ingredient2"])
#     print(body["ingredient3"])
#     print(body["ingredient4"])

#     # Start the process of making a cocktail
#     return jsonify({ "success": True })

# SOCKET IO
@socketio.on('connect')
def initial_connection():
    print('A new client connect')

@socketio.on('F2B_clean_pumps')
def clean_pumps():
    # Main.cleanPumps()
    print('Cleaning the pumps')

@socketio.on('F2B_start_cocktail')
def start_cocktail(data):
    print(DataRepository.read_cocktail_instructions_by_id(data["idDrink"]))

    time.sleep(10)
    emit("B2F_cocktail_done")

@socketio.on('F2B_update_ingredients')
def start_cocktail(data):
    global available_ingredients
    available_ingredients = [data["ingredient1"], data["ingredient2"], data["ingredient3"], data["ingredient4"]]


if __name__ == '__main__':
    try:
        # start_thread()
        print("**** Starting APP ****")
        socketio.run(app, debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        print('KeyboardInterrupt exception is caught')
    finally:
        print("finished")
