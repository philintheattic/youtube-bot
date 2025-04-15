from flask import Flask, render_template, request
import random

app = Flask(__name__)

def blackout_poem(text: str, reveal_chance=0.5):
    words = text.split()
    output = []
    for word in words:
        if random.random() < reveal_chance:
            output.append(word)
        else:
            output.append("█" * len(word))
    return " ".join(output)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        poem = blackout_poem(request.form.get("poem"))
        return render_template("index.html", poem=poem)  
    else: 
        return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    poem = blackout_poem(request.form.get("poem"))
    return render_template("index.html", poem=poem)

# app.run(host="0.0.0.0", port=80)