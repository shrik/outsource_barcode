from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import sys
from waitress import serve

from service import decode_barcode

app = Flask(__name__, static_folder='.')
CORS(app)  # Enable CORS for all routes


@app.route('/index')
def index():
    return send_from_directory('.', 'barcode.html')

@app.route('/', methods=['GET'])
def camera():
    return send_from_directory('.', 'camara.html')

@app.route('/rec', methods=['POST'])
def rec():
    # get the image from the request
    # process the image
    # return the result
    request_data = request.get_json()
    image = request_data['image']
    result = decode_barcode(image)
    return jsonify([data.decode() for data in result ])

#app.run(debug=True, host="0.0.0.0", port=5051)
port = int(sys.argv[1])

serve(app, host="0.0.0.0", port=port)
#app.run(debug=False, host="0.0.0.0", port=port)
