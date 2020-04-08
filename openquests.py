import json

# Using this to make edits to the quest list

with open('questlist.json') as f:
  data = json.load(f)

quests = data["quests"]

for quest in quests[:21]:
    quest["ismem"] = False

for quest in quests[21:]:
    quest["ismem"] = True

with open('questlist.json', 'w') as outfile:
    json.dump(quests, outfile, indent=2)