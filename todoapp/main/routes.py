from flask import render_template, url_for, redirect, Blueprint
from todoapp.models import Todo
from todoapp import db

main = Blueprint("main", __name__)

# Delete, update

@main.route("/", methods=["GET", "POST"])
@main.route("/index")
def index():
    t = Todo(data="Running")
    db.session.add(t)
    db.session.commit()
    return "Index Page"