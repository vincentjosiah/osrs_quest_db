import json

def current_points(quests):
	points_obtained = 0

	for quest in data["quests"]:
		if quest["completed"] == True:
			points_obtained += quest["points"]
	return points_obtained

def points_remaining(points_needed, quests):
	return points_needed - current_points(quests)

def next_quest(quests):
	for quest in quests:
		if quest["completed"] == False:
			return quest["name"]

def print_menu():
	print("What would you like to do?")
	print("1. Show current quest points")
	print("2. Show current quest needed")
	print("3. Show next quest")
	print("q. Quit")


quest_list = []

points_needed = 175

data = {}

with open('quests.json') as json_file:
    data = json.load(json_file)

loop = True

while(loop):	
	print_menu()
	menu_input = input()

	if menu_input == "1":
		print(current_points(data["quests"]))
	elif menu_input == "2":
		print(points_remaining(points_needed, data["quests"]))
	elif menu_input == "3":
		print(next_quest(data["quests"]))
	elif menu_input == "q" or menu_input == "Q":
		loop = False

with open('quests.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)