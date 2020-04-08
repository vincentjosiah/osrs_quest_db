import json

quest_list = []

data = {"quests":[]}

# data["quests"].append({"name": "test_name"})

f = open("questlist.txt", "r")
for line in f:
    qline = line.strip()
    qline_list = qline.split('\t')
    quest_list.append(qline_list)

for quest in quest_list:
    data["quests"].append({
        "name": quest[0],
        "difficulty": quest[1],
        "length": quest[2],
        "points": quest[3]
    })

with open('questlist.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)