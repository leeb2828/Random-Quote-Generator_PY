from quotes import printQuote
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    quotes = printQuote()
    return render_template("index.html", quotes_list=quotes)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)