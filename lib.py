import json
import bcrypt

class User:
    _all_users = []
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.todos = []

        new_user = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "todos": []
        }

        User._all_users.append(new_user)

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_user(name, email, password):
    d = []
    already_registered = False
    with open("db.json", "r") as f:
        d = json.load(f)
        for u in d:
            if u["email"] == email:
                already_registered = True

    if already_registered:
        return "User already registered"
    else:
        pasw_hash = hash_password(password)
        new_user = User(name, email, pasw_hash)
        save_new_user(name, email, pasw_hash)

def save_todo(email, todo):
    d = []
    t = {
        "todo": todo,
        "is_checked": False
    }
    with open("db.json", "r") as f:
        d = json.load(f)

        for u in d:
            if u["email"] == email:
                u["todos"].append(t)
    
    with open("db.json", "w") as f:
        json.dump(d, f, indent=4)

def reload_todos(email):
    d = []
    with open("db.json", "r") as f:
        d = json.load(f)

        for u in d:
            if u["email"] == email:
                return u["todos"]
            
def set_checked(email, todo_text, is_checked):
    with open("db.json", "r") as f:
        d = json.load(f)

    for u in d:
        if u["email"] == email:
            for t in u["todos"]:
                if t["todo"] == todo_text:
                    t["is_checked"] = is_checked

    with open("db.json", "w") as f:
        json.dump(d, f, indent=4)
            
def delete_todo(email, todo_text):
    with open("db.json", "r") as f:
        d = json.load(f)

    for u in d:
        if u["email"] == email:
            u["todos"] = [t for t in u["todos"] if t["todo"] != todo_text]

    with open("db.json", "w") as f:
        json.dump(d, f, indent=4)

def login(email, password):
    d = []
    with open("db.json", "r") as f:
        d = json.load(f)

        exist = False
        em = False
        p = False

        for u in d:
            if u["email"] == email:
                email = True
                if check_password(password, u["password"]):
                    p = True
                    exist = True
        
        if p == False and email == True:
            return "The password is incorrect"
        elif exist == False:
            return "User not found"
        elif exist == True:
            return True
        else:
            return "User not found"

def refill_user():
    with open("db.json", "r") as f:
        data = json.load(f)
        User._all_users = data

def return_name(email):
    d = []
    with open("db.json", "r") as f:
        d = json.load(f)
        for u in d:
            if u["email"] == email:
                return u["name"].title()

def save_new_user(name, email, password):
    with open("db.json", "r") as f:
        data = json.load(f)

    new_user = {
        "name": name,
        "email": email,
        "password": password,
        "todos": []
    }
    data.append(new_user)

    with open("db.json", "w") as f:
        json.dump(data, f, indent=4)

    User._all_users = data
