from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def prioritizer():
    button1 = "This"
    button2 = "That"
    if request.method == "POST":
        if request.form.get("x"):
            print("You submitted a!")
        elif request.form.get("y"):
            print("You submitted b!")
    elif request.method == "GET":
        print("You submitted nothing!")

    return render_template("index.html", button1=button1, button2=button2,)

