from flask import Flask, render_template
from exchange import Exchange

app = Flask(__name__)

ex = Exchange()

@app.route('/')
def index():
    return render_template('index.html', tickers = ex.getAllTickers())

if __name__ == '__main__':
    app.run(debug=True)