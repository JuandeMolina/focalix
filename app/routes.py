from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Task
from . import db

main = Blueprint("main", __name__)


# Main page
@main.route("/")
def home():
    return render_template("inicio.html")


@main.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        due_date = request.form.get("due_date")
        if not title:
            flash("Title is required.", "error")
        else:
            new_task = Task(title=title, description=description, due_date=due_date)
            db.session.add(new_task)
            db.session.commit()
            flash("Task created successfully!", "success")
        return redirect(url_for("main.tasks"))
    all_tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("tasks.html", tasks=all_tasks)


@main.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == "POST":
        task.title = request.form.get("title")
        task.description = request.form.get("description")
        task.due_date = request.form.get("due_date")
        db.session.commit()
        flash("Task updated!", "success")
        return redirect(url_for("main.tasks"))
    return render_template("edit_task.html", task=task)


@main.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted!", "success")
    return redirect(url_for("main.tasks"))


@main.route("/settings")
def settings():
    return render_template("settings.html")
