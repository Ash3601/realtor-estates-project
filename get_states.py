f = open("states.txt", "r")
contents = f.read()
states_list = contents.split("\n")
new_list = []
for state in states_list:
    print("@" + state + "@" + ":" + "@" + state + "@")
f.close()
