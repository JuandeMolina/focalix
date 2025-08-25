from flask import Blueprint, render_template
from .models import Task
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def home():
    tasks = Task.query.all()
    return render_template("app/templates/base.html", tasks=tasks)
