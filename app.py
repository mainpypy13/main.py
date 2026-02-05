from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "secretkey"

# Geçici veri depoları
users = {}      # iş arayanlar
employers = {}  # işverenler


@app.route("/")
def home():
    return render_template("login.html")


# ---------------- REGISTER ----------------
@app.route("/register/<role>", methods=["GET", "POST"])
def register(role):
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if role == "user":
            users[email] = {
                "password": password,
                "name": request.form["name"],
                "surname": request.form["surname"],
                "scores": []
            }
        else:
            employers[email] = {
                "password": password,
                "company": request.form["company"],
                "position": request.form["position"]
            }

        return redirect(url_for("home"))

    return render_template("register.html", role=role)


# ---------------- LOGIN ----------------
@app.route("/login/<role>", methods=["POST"])
def login(role):
    email = request.form["email"]
    password = request.form["password"]

    data = users if role == "user" else employers

    if email in data and data[email]["password"] == password:
        session["email"] = email
        session["role"] = role
        return redirect("/dashboard")

    return "Hatalı giriş"


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "email" not in session:
        return redirect("/")

    email = session["email"]
    role = session["role"]

    profile = users[email] if role == "user" else employers[email]

    return render_template("dashboard.html", role=role, profile=profile)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
