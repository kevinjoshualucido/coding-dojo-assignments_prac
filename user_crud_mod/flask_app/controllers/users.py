from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User


@app.route("/")
def index():
    users = User.show_all()
    return render_template("read_all.html", users=users)


@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "email": request.form["email"],
    }
    if not User.validate_user(request.form):
        return redirect("/create_user/new")
    User.create_user(data)
    return redirect("/")


@app.route("/create_user/new")
def add_user():
    return render_template("create.html")


@app.route("/user/show/<int:id>")
def show_user(id):
    user = User.show_one(id)
    return render_template("read_one.html", user=user)


@app.route("/user/<int:id>/edit")
def edit_user(id):
    user = User.show_one(id)
    return render_template("edit.html", user=user)


@app.route("/user/update", methods=["POST"])
def update_user():
    User.update_user(request.form)
    return redirect("/")


@app.route("/delete/<int:id>")
def delete_user(id):
    User.delete_user(id)
    return redirect("/")
