from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from exchange import Exchange

app = Flask(__name__)
CORS(app)
ex = Exchange()

@app.route('/')
def index():
    return render_template('index.html', title="API")

@app.route('/api/v1/ticker/price', methods=['GET'])
def api():
    if request.method == "GET":
        #print(ex.getAllTickers())
        return jsonify(ex.getAllTickers())
    else:
        return None

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)