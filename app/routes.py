from flask import Blueprint, render_template
from .models import Task
from . import db

main = Blueprint("main", __name__)


# Main page
@main.route("/")
def home():
    return render_template("inicio.html")


@main.route("/tasks")
def tasks():
    return render_template("tasks.html")


@main.route("/settings")
def settings():
    return render_template("settings.html")
