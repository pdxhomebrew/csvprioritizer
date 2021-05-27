from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def prioritizer():
    print(file_reader())
    pairs = file_reader()
    index = 0
    options = []
    for i, pair in enumerate(pairs):
        if len(pair) == 2:
            index = i
            options = pair
            button1 = options[0]
            button2 = options[1]
            break
    if request.method == "POST":
        if request.form.get("a"):
            options.append(options[0])
            print("You submitted a!")
        elif request.form.get("b"):
            options.append(options[1])
            print("You submitted b!")
        pairs[index] = options
        save_csv(pairs)
    elif request.method == "GET":
        # check if we need to import options on GET everytime
        button1 = None
        button2 = None
        print("You submitted nothing!")


    return render_template("index.html", button1=button1, button2=button2,)


def file_reader():
    with open("../pairs.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data


def save_csv(priorities):
    with open("../pairs.csv", "w", newline="") as writefile:
        writer = csv.writer(writefile)
        for p in priorities:
            writer.writerow([p])