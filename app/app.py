from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def prioritizer():
    # refactor these four lines (tuple destructuring?)
    pairs = file_reader()
    options = get_next_pair(pairs)
    button1 = options[0]
    button2 = options[1]
    if request.method == "POST":
        if request.form.get("a"):
            choice = request.form.get("a")
        elif request.form.get("b"):
            choice = request.form.get("b")
        update(pairs, options, choice)
        pairs = file_reader()
        options = get_next_pair(pairs)
        button1 = options[0]
        button2 = options[1]
    return render_template("index.html", button1=button1, button2=button2,)


def get_next_pair(pairs):
    for pair in pairs:
        if len(pair) == 2:
            return pair


def update(pairs, options, result):
    for i, pair in enumerate(pairs):
        if pair == options:
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