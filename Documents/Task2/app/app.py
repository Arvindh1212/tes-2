from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%A, %B %d, %Y — %I:%M %p")
    return render_template("index.html", time2=current_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)