import json
def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list
score = 0
with open("quiz.json", "r") as quiz:
    data = json.load(quiz)
sub = data["quiz"]
print (getList(sub))
choice = input ("Enter Subject:")
if choice == "sport":
    question = sub["sport"]
    q1 = question["q1"]
    print(q1["question"])
    print(q1["options"])
    ans = input("Enter answer:")

    if ans == "Huston Rocket":
        score = score+1
    else:
        score = score + 0
elif choice == "maths":
    question = sub["maths"]
    q1 = question["q1"]
    q2 = question["q2"]
    print(q1["question"])
    print(q1["options"])
    ans = input("Enter answer:")
    if ans == "12":
        score = score+1
    else:
        score = score+0
    print(q2["question"])
    print(q2["options"])
    ans =input("Enter answer:")
    if ans == "4":
        score = score+1
    else:
        score = score+0
    print("Result:", score)
else:
    print("Incorrect Selection")


