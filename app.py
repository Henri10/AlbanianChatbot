from flask import Flask, render_template, request, jsonify
import requests


RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"
app = Flask(__name__)

@app.route("/static/index.html")
def index():
    return render_template("index.html")

@app.route("/static/belsh.html")
def belsh():
    return render_template("belsh.html")

@app.route("/static/dibra.html")
def dibra():
    return render_template("dibra.html")

@app.route("/static/bulqiza.html")
def bulqiza():
    return render_template("bulqiza.html")

@app.route("/static/durres.html")
def durres():
    return render_template("durres.html")

@app.route("/static/elbasan.html")
def elbasan():
    return render_template("elbasan.html")

@app.route("/static/ersek.html")
def ersek():
    return render_template("ersek.html")

@app.route("/static/fier.html")
def fier():
    return render_template("fier.html")


@app.route("/static/gjirokaster.html")
def gjirokaster():
    return render_template("gjirokaster.html")


@app.route("/static/gramsh.html")
def gramsh():
    return render_template("gramsh.html")

@app.route("/static/himare.html")
def himare():
    return render_template("himare.html")

@app.route("/static/korce.html")
def korce():
    return render_template("korce.html")

@app.route("/static/kucov.html")
def kucov():
    return render_template("kucov.html")


@app.route("/static/kuksi.html")
def kuksi():
    return render_template("kuksi.html")

@app.route("/static/leskovik.html")
def leskovik():
    return render_template("leskovik.html")

@app.route("/static/lezha.html")
def lezha():
    return render_template("lezha.html")

@app.route("/static/lushnje.html")
def lushnje():
    return render_template("lushnje.html")

@app.route("/static/malsiamadhe.html")
def malsiamadhe():
    return render_template("malsiamadhe.html")

@app.route("/static/rj.html")
def rj():
    return render_template("rj.html")

@app.route("/static/rjl.html")
def rjl():
    return render_template("rjl.html")

@app.route("/static/rp.html")
def rp():
    return render_template("rp.html")

@app.route("/static/rv.html")
def rv():
    return render_template("rv.html")

@app.route("/static/rvl.html")
def rvl():
    return render_template("rvl.html")


@app.route("/")
def berat():
    return render_template("berat.html")

@app.route('/webhook', methods=["POST"])
def webhook():
    user_message = request.json["message"]
    print("User Message:", user_message)

    # send user message to rasa
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response:", rasa_response_json)

    bot_response = rasa_response_json[0]["text"] if rasa_response_json else "Me falni nuk e kuptova!!!"

    return jsonify({"response": bot_response})


if __name__ == "__main__":
    app.run(debug=True, port=3000)