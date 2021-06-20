from flask import Flask, render_template, request, redirect, Response
app = Flask(__name__)



@app.get("/")
def upload_image():

    return render_template("upload.html")

@app.post("/upload_files")
def upload_files():
    report = ""
    for f in request.files.getlist("files[]"):
        txt = f.read().decode("utf-8")
        report += f.filename
        report += txt
        report += "\n"

    print(report)
    response = Response(report, mimetype="text/csv")
    response.headers['Content-Disposition'] = 'attachment; filename=fehlerreport.txt'
    return response

if __name__ == "__main__":
    app.run(debug=True)