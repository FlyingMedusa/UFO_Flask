from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = ''

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/historia")
def history():
    return render_template("historia.html")

@app.route("/dzien1", methods=["POST", "GET"])
def day1():
    DOOR_3_PASSWORD = 'abc'
    if request.method == "POST":
        # body = request.json
        # pass_key = body['pass']
        # print('json',request.json)
        print('form',request.form)
        if 'klucz' in request.form:
            flash("⚠️ ODMOWA WSTĘPU ⚠️", "info")
            return render_template("dzien1.html")
        if 'kluczyk' in request.form:
            pass_key_correct_door = request.form['kluczyk']
            
            if pass_key_correct_door == DOOR_3_PASSWORD:
                return redirect(url_for("stage2"), 302)
            else:
                flash("⚠️ ODMOWA WSTĘPU ⚠️", "info")
                return render_template("dzien1.html")
    else:
        return render_template("dzien1.html")

@app.route("/dzien1/korytarz")
def stage2():
    return render_template("korytarz.html")

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