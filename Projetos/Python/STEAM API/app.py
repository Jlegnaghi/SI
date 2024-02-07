from flask import Flask, render_template, request
from steam import Steam
from decouple import config

app = Flask(__name__)

# Configurando a chave da API da Steam
KEY = config("STEAM_API_KEY")
steam = Steam(KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    username = None
    if request.method == "POST":
        user_id = request.form["user_id"]
        user_info = steam.users.get_user_info(user_id)
        if user_info:
            username = user_info["personaname"]
    return render_template("index.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
