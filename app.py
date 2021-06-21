from flask import Flask, render_template, request, redirect, send_file
from example_blueprint import example_blueprint

app = Flask(__name__)
app.register_blueprint(example_blueprint)



@app.get("/")
def upload_image():

    return render_template("upload.html")

def filename_allowed(filename : str) -> bool:
    if filename == "":
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() != "TXT":
        return False
    return True


@app.post("/upload_files")
def upload_files():
    report = ""
    
    for f in request.files.getlist("files[]"):
        if filename_allowed(f.filename):
            txt = f.read().decode("utf-8")
            report += f"{f.filename} : {txt} \n"
        else:
            report += f"{f.filename} nicht gültig. \n"
        
        with open("Output.txt", "w") as text_file:
            text_file.write(report)
 

    return send_file("Output.txt",  as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)