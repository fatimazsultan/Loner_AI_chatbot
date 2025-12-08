from flask import Flask, render_template, request
from lonerai import generate_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    bot_reply = ""
    user_message = ""

    if request.method == "POST":
        user_message = request.form.get("message")
        bot_reply = generate_response(user_message)

    return render_template("index.html", user_message=user_message, bot_reply=bot_reply)

if __name__ == "__main__":
    app.run(debug=False)
