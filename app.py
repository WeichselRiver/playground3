from flask import Flask, render_template
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def upload_image():
    return render_template("upload.html")