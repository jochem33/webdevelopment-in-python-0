from flask import Flask, render_template
import time


app = Flask(__name__)

gameslijst = [
    {
        "naam": "Roblox",
        "plaatje": "https://images.rbxcdn.com/6c27cb9db1779888868bf7d87e6d3709.jpg"
    },
    {
        "naam": "Frotnite",
        "plaatje": "https://i.ytimg.com/vi/rIJK8S2IFUc/hqdefault.jpg"
    },
    {
        "naam": "Minecraft",
        "plaatje": "https://minecraft.net/static/pages/img/minecraft-hero-og.c5517b7973e1.jpg"
    }
]

@app.route("/games")
def games():
    return render_template("games.html", games = gameslijst)


@app.route("/")
def hello():
    return "GAMER DUB"

@app.route("/welcome/<name>")
def contact(name):
    return render_template("gamer.html", namePerson=name)

@app.route("/tijd/<gamer>")
def tijd(gamer):
    return time.strftime("%R") + " " + gamer

@app.route("/tafel/<int:tafel>/<string:otto>")
def tafel(tafel, otto):
    tafellijst = "tafel van " + str(tafel) + ":\n"
    for i in range(1, 10):
        som = int(tafel) * i
        tafellijst = tafellijst + " " + str(som)
    return tafellijst + " " + str(otto)

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

app.run(debug=True)
