from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def prioritizer():
    print(file_reader())
    pairs = file_reader()
    if request.method == "POST":
        # figure out how to surface the next pair to each button
        button1 = "A"
        button2 = "B"
        if request.form.get("a"):
            choice = request.form.get("a")
            position = 0
        elif request.form.get("b"):
            choice = request.form.get("b")
            position = 1
        update(pairs, position, choice)
    elif request.method == "GET":
        options = []
        for pair in pairs:
            if len(pair) == 2:
                options = pair
                button1 = options[0]
                button2 = options[1]
                break


    return render_template("index.html", button1=button1, button2=button2,)


def update(pairs, position, result):
    for i, pair in enumerate(pairs):
        if pair[position] == str(result) and len(pair) == 2:
            pairs[i].append(result)
            break
    save_csv(pairs)


def file_reader():
    with open("../pairs.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, quoting = csv.QUOTE_NONE)
        data = []
        for row in reader:
            data.append(row)
        return data


def save_csv(priorities):
    with open("../pairs.csv", "w", newline="") as writefile:
        writer = csv.writer(writefile)
        for p in priorities:
            writer.writerow(p)