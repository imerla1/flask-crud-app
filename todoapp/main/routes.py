from flask import render_template, url_for, redirect, Blueprint

main = Blueprint("main", __name__)

# Delete, update

@main.route("/", methods=["GET", "POST"])
@main.route("/index")
def index():
    return "Index Page"