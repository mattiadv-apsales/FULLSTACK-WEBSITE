# --------------- LIBRARYS ------------------

from flask import Flask, jsonify, request, send_file, redirect, render_template, session
from lib import create_user, return_name, login, save_todo, reload_todos, delete_todo, set_checked
from datetime import timedelta
from dotenv import load_dotenv
import os

# --------------- START VAR ------------------

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")
app.permanent_session_lifetime = timedelta(days=1)


# --------------- GET METHODS ------------------

@app.route("/", methods = ["GET"])
def get_index():
    return send_file("index.html")

@app.route("/sbem", methods=["GET"])
def success_page():
    email = session.get('email')

    if not email:
        return redirect("/")
    
    name = return_name(email)
    todos = reload_todos(email)
    return render_template("sbem.html", email = name, todos = todos)


# --------------- POST METHODS ------------------

@app.route("/register", methods = ["POST"])
def register_user():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    c = create_user(name, email, password)

    if c == "User already registered":
        return jsonify({"error": "User already registered"}), 400
    else: 
        session.permanent = True
        session['email'] = email
        return jsonify({"redirect": "/sbem", "email": email})
    
@app.route("/login", methods = ["POST"])
def login_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    ris = login(email, password)

    if ris == "The password is incorrect":
        return jsonify({"error": "The password is incorrect"}), 401
    if ris == "User not found":
        return jsonify({"error": "User not found"}), 404
    else:
        session.permanent = True
        session['email'] = email
        return jsonify({"redirect": "/sbem", "email": email})

@app.route("/add_todo", methods = ["POST"])
def add_todo():
    data = request.json
    email = session.get('email')

    if not email:
        return jsonify({"error": "User not logged in"}), 401
    
    todo = data.get("todo")

    save_todo(email, todo)
    return jsonify({"message": "Todo added successfully"}), 200

@app.route("/logout", methods = ["POST"])
def logout():
    session.pop("email")
    return jsonify({"redirect": "/"}), 200

@app.route("/delete_todo", methods = ["POST"])
def remove_todo():
    data = request.json
    email = session.get('email')

    if not email:
        return jsonify({"error": "User not logged in"}), 401

    todo = data.get("todo")

    delete_todo(email, todo)
    return jsonify({"message": "Todo deleted successfully"}), 200

@app.route("/checked", methods = ["POST"])
def check_todo():
    data = request.json
    email = session.get('email')

    if not email:
        return jsonify({"error": "User not logged in"}), 401
    
    todo = data.get("todo")
    is_checked = data.get("is_checked")

    set_checked(email, todo, is_checked)

    return jsonify({"message": "Todo status updated successfully"}), 200


# --------------- ERROR ------------------

@app.errorhandler(404)
def error(e):
    return render_template("error.html"), 404


# --------------- RUN APP ------------------

if __name__ == "__main__":
    app.run(debug=False)