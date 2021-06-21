from flask import Blueprint, render_template

example_blueprint = Blueprint('example_blueprint', __name__, template_folder="templates1", url_prefix="/bp")

@example_blueprint.route("/")
def index():
    return render_template("index.html")