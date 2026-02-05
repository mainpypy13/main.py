from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# MOCK CV DATA (5 adet)
cvs = [
    {"id": 1, "name": "Ahmet Yılmaz", "skill": "Python, ML"},
    {"id": 2, "name": "Elif Kaya", "skill": "Data Science"},
    {"id": 3, "name": "Mehmet Demir", "skill": "Frontend Developer"},
    {"id": 4, "name": "Zynep Arslan", "skill": "AI Engineer"},
    {"id": 5, "name": "Can Özkan", "skill": "Backend Developer"},
]

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/user")
def user_panel():
    return render_template("user.html")

@app.route("/employer")
def employer_panel():
    return render_template("employer.html", cvs=cvs)

@app.route("/rate/<int:cv_id>/<int:score>")
def rate(cv_id, score):
    print(f"CV {cv_id} {score} puan aldı")
    return redirect(url_for("employer_panel"))

if __name__ == "__main__":
    app.run(debug=True)
