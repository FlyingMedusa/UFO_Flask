from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/historia")
def history():
    return render_template("historia.html")

@app.route("/dzien1", methods=["POST", "GET"])
def day1():
    if request.method == "POST":
        the_key = request.form["kluczyk"]
        return redirect(url_for("stage2"))
    else:
        return render_template("dzien1.html")

@app.route("/dzien1/korytarz")
def stage2():
    return "działa"

@app.route("/dzien2")
def day2():
    return render_template("dzien2.html")

@app.route("/dzien3")
def day3():
    return render_template("dzien3.html")

@app.route("/materialy")
def materials():
    return render_template("materialy.html")

@app.route("/dni")
def all_days():
    return render_template("dni.html")

if __name__ == "__main__":
    app.run(debug=True)