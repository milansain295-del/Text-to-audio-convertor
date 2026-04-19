from flask import Flask, render_template, request
from gtts import gTTS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None

    if request.method == "POST":
        text = request.form.get("text")
        file = request.files.get("file")

        if file and file.filename != "":
            text = file.read().decode("utf-8")
        if not text:
            return render_template("index.html", audio_file=None)

        lang = request.form["lang"]
        speed = request.form["speed"]

        tts = gTTS(text=text, lang=lang, slow=(speed == "slow"))
        audio_file = "static/output.mp3"
        tts.save(audio_file)

    return render_template("index.html", audio_file=audio_file)

if __name__ == "__main__":
    app.run(debug=True)