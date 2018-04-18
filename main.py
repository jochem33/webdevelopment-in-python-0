from flask import Flask
import time


app = Flask(__name__)

@app.route("/")
def hello():
    return "GAMER DUB"

@app.route("/contact")
def contact():
    return ("""Pietje Puk <br>
                Flaskstraat 21 <br>
                1092AD Amsterdam""")

@app.route("/tijd/<gamer>")
def tijd(gamer):
    return (time.strftime("%R") + " " + gamer)

@app.route("/tafel/<int:tafel>/<string:otto>")
def tafel(tafel, otto):
    tafellijst = "tafel van " + str(tafel) + ":\n"
    for i in range(1, 10):
        som = int(tafel) * i
        tafellijst = tafellijst + " " + str(som)
    return (tafellijst + " " + str(otto))


app.run(debug=True)
