from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from exchange import Exchange
import threading
import time

########## SIGMALEAF API ##########

ex 		= Exchange()
prices 	= ex.getAllTickers()
app 	= Flask(__name__)
CORS(app)

"""
Refreshes CCXT prices every minute.
"""
def refreshPrices(s):
	mins = False
	while True:
		if mins == True:
			print("tickers updated.")
			prices = ex.getAllTickers()
			mins = False
		else:
			time.sleep(s)
			mins = True

"""
Root directory router.
@route='/'
"""
@app.route('/')
def index():
    return render_template('index.html', title="API")

"""
Retreive all tickers.
@route='/api/v1/ticker/price'
"""
@app.route('/api/v1/ticker/price', methods=['GET'])
def api():
    if request.method == "GET":
        #print(ex.getAllTickers())
        return jsonify(prices)
        #return 
    else:
        return None

"""
404 error handler
"""
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

"""
MAIN
"""
if __name__ == '__main__':
	pThread = threading.Thread(target=refreshPrices, args=(60,))
	pThread.start()
	app.run(debug=True)
