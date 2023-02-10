# Added request and redirect
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # Set a secret key for security purposes


@app.route("/")
def index():
    return render_template("index.html")


# We have an acton attribute that will be handled by our route "/users"
# Our methods attribute is specified as POST
@app.route("/users", methods=["POST"])
def create_user():
    print("Post Info Received")
    ### print(request.form) ###
    session["username"] = request.form["name"]
    session["useremail"] = request.form["email"]
    return redirect("/show")  # Redirect to form
    # Never render template on a POST request
    # Redirect to form instead

# Adding this GET method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True, port=5005)
