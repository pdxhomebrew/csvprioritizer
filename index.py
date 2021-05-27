import csv
from itertools import combinations


file_input = str(input("Please input the path where your CSV file is located: "))
if not ".csv" in file_input:
    file_input += ".csv"

with open(file_input, newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
        data.append(row[0])

    unsorted = []
    for i in data:
        if i not in unsorted:
            unsorted.append(i)

    priorities = {i : 0 for i in unsorted}
    pairs = combinations(unsorted, 2)
    for thing in pairs: 
        print(thing)
    for i in list(pairs):
        choice = input("\n Choose between these two options: \n 1: {0} \n 2: {1} \n ".format(i[0], i[1]))
        while choice not in ["1", "2"]:
            choice = input("\n You may only input '1' or '2': \n 1: {0} \n 2: {1} \n Input: ".format(i[0], i[1]))
        if choice == "1":
            priorities[i[0]] += 1
        elif choice == "2":
            priorities[i[1]] += 1

    with open("priorities.csv", "w", newline="") as writefile:
        writer = csv.writer(writefile)
        for p in sorted(priorities, key=priorities.get, reverse=True):
            writer.writerow([p])